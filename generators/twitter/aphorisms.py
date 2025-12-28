#!/usr/bin/env python3
"""
Aphorisms Generator - Hard-hitting takes for intellectual Twitter.

This monad generates engagement-optimized aphorisms/takes/tweets that maximize
impact through deliberate syntax, capitalization, and precision while
maintaining intellectual rigor. Maps each take to its target micro-demographic.
"""

import os
import sys
from datetime import datetime

# Import shared utilities - the common protocol for all generators
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from utils import (
    get_llm_client,
    get_default_model,
    get_completion_params,
    parse_llm_json_response,
    save_output,
    run_generation
)

# ============ CONFIGURATION ============

GENERATOR_CONFIG = {
    "name": "x_aphorisms",
    "item_keys": ["aphorisms", "takes", "tweets"],
    "max_tokens": 8000,
    "temperature": 0.7,
}

SYSTEM_PROMPT = """You are a master of intellectual discourse on Twitter/X. You make complex ideas hit hard through varied rhetorical forms, not templates. Capitalization is a cultural signal (lowercase = humility/coolness, CAPS = emphasis, proper = authority). Vary punctuation and rhythm. Use the guidance as vectors, not molds. Always respond with valid JSON only."""


def build_prompt(num_aphorisms: int, structure_mode: str) -> str:
    """Build the aphorism generation prompt with configurable structure mode."""
    prompt_header = f"""You are a master of intellectual Twitter discourse with deep knowledge of:
- Cultural criticism (Paglia, Hitchens, CEBK-style comparative analysis)
- Economic theory (mechanism design, auction theory, Schumpeterian frameworks)
- Tech/AI discourse (Ribbonfarm, rationalist-adjacent, ML theory)
- Philosophy (game theory, epistemology, phenomenology)
- Systems thinking and interdisciplinary synthesis

Generate {num_aphorisms} HARD-HITTING aphorisms/takes/tweets that maximize engagement while maintaining intellectual rigor.
"""

    if structure_mode == "diverse":
        prompt_body = """
TREAT ALL GUIDANCE AS VECTORS, NOT TEMPLATES. Do NOT repeat a single rhetorical skeleton across items.

FORMAT STYLES TAXONOMY (pick a mix per batch; label each item with format_style):
- question: a genuine question
- imperative: direct command/advice
- very_short_maxim: <= 80 chars, no commas
- analogy_metaphor: vivid metaphor/analogy
- x_vs_y: explicit contrast (X vs Y) without em-dash crutch
- if_then: conditional structure
- qa_turn: Q -> A in one line
- checklist: 3 bullets with separators like "." or " * " (but still one tweet line)
- quote_twist: quote/aphorism then twist
- stat_led: number/metric leads the line
- micro_parable: 2 short sentences, second reframes the first

BATCH DIVERSITY CONTRACT:
- Minimum quotas (approximate if count is small):
  - >=2 questions, >=2 imperatives, >=2 very_short_maxims
  - >=2 from {analogy_metaphor, x_vs_y}
  - >=2 from {if_then, qa_turn}
  - >=2 from {quote_twist, stat_led, micro_parable}
- Casing: mix lowercase, proper, and sparse ALL-CAPS; ALL-CAPS in <=25% of items.
- Punctuation: em-dash in <=30% of items; semicolons in <=30%; end punctuation varied (periods allowed but not required).
- Length: include at least 3 items <= 80 chars and 3 items >= 180 chars (within 280 char limit).
- No repeated openings across more than 3 items (avoid starting many with "the", "actually", "been").

PER-ITEM FIELDS (JSON object):
- take: the tweet text (<= 280 chars)
- format_style: one of the taxonomy values above
- capitalization_strategy: brief rationale for casing choice
- intellectual_scaffolding: 1-3 specific concepts (keep tight)
- why_it_hits: 1 short clause
- target_demographic: micro-community
- formatting_notes: any relevant punctuation/structure notes

IMPORTANT:
- Prefer originality over patterning. Do not mirror the examples; vary rhythm, openings, and clause structure.
- Avoid overuse of em-dash and semicolons; use commas, slashes, parentheses, or line-break-like separators (" * ") where helpful.
"""
    else:
        # Legacy schema/template body for backward compatibility
        prompt_body = """
CAPITALIZATION STRATEGIES - vary these strategically:
1. **Strategic CAPS for emphasis**: "one theorem ALONE is what paid for google"
2. **All lowercase for thoughtful/humble affect**: "actually think the sortition people might be onto something here"
3. **Proper case for authoritative takes**: "The liquidity of discipline isn't discipline."
4. **Mixed case for thread-style reflection**: "been thinking about this... the REAL question isn't alignment but what selects FOR alignment"

Each aphorism should:
1. **The Take** (280 chars max)
2. **Capitalization Strategy**
3. **Intellectual Scaffolding** (2-3 specific items)
4. **Why It Hits**
5. **Target Demographic**
6. **Thread Potential** (optional)
7. **Formatting Notes**
8. **Intellectual Rigor Score** (1-10)
9. **Engagement Vectors**
10. **Aesthetic Tribe**
"""

    prompt_footer = """
Make them GENUINELY SMART but Twitter-optimized. Use the guidelines as vectors; avoid repeating any single template.
Cover domains: econ, AI/ML, cultural criticism, philosophy, systems thinking, tech, institutional design, epistemology.

Return as a JSON array of objects. Always respond with valid JSON only.
"""

    return f"{prompt_header}\n\n{prompt_body}\n\n{prompt_footer}"


# ============ MARKDOWN FORMATTER ============

def format_markdown(data: dict, f) -> None:
    """Format aphorisms as markdown - the unique output form of this monad."""
    f.write("# Hard-Hitting Aphorisms for Intellectual Twitter\n\n")
    f.write(f"*Generated on {data['generated_at']} using {data['model_used']}*\n\n")
    f.write(f"**Total Aphorisms:** {data['num_aphorisms']}\n\n")
    f.write("---\n\n")

    for i, aph in enumerate(data['aphorisms'], 1):
        f.write(f"## {i}.\n\n")

        if 'take' in aph:
            f.write("### THE TAKE\n\n")
            f.write(f"> {aph['take']}\n\n")

        if 'capitalization_strategy' in aph:
            f.write(f"**Capitalization Strategy:** {aph['capitalization_strategy']}\n\n")

        if 'format_style' in aph:
            f.write(f"**Format Style:** {aph['format_style']}\n\n")

        if 'aesthetic_tribe' in aph:
            f.write(f"**Aesthetic Tribe:** {aph['aesthetic_tribe']}\n\n")

        if 'target_demographic' in aph:
            f.write(f"**Target Demographic:** {aph['target_demographic']}\n\n")

        if 'intellectual_scaffolding' in aph:
            f.write("**Intellectual Scaffolding:**\n")
            scaffolding = aph['intellectual_scaffolding']
            if isinstance(scaffolding, list):
                for item in scaffolding:
                    f.write(f"- {item}\n")
            else:
                f.write(f"{scaffolding}\n")
            f.write("\n")

        if 'why_it_hits' in aph:
            f.write(f"**Why It Hits:** {aph['why_it_hits']}\n\n")

        if 'rigor_score' in aph:
            f.write(f"**Intellectual Rigor Score:** {aph['rigor_score']}/10\n\n")

        if 'engagement_vectors' in aph:
            f.write("**Engagement Vectors:** ")
            vectors = aph['engagement_vectors']
            if isinstance(vectors, list):
                f.write(", ".join(vectors))
            else:
                f.write(str(vectors))
            f.write("\n\n")

        if 'formatting_notes' in aph:
            f.write(f"**Formatting Notes:** {aph['formatting_notes']}\n\n")

        if 'thread_potential' in aph:
            f.write(f"**Thread Potential:** {aph['thread_potential']}\n\n")

        f.write("---\n\n")


# ============ CORE FUNCTIONS ============

def generate_aphorisms(
    num_aphorisms=20,
    output_format="markdown",
    model=None,
    structure_mode: str = "diverse"
):
    """
    Generate intellectually rigorous, engagement-optimized aphorisms/tweets.

    Args:
        num_aphorisms: Number of distinct takes to generate
        output_format: 'markdown' or 'json'
        model: LLM model to use
        structure_mode: 'diverse' for varied formats, 'legacy' for original schema

    Returns:
        Dictionary containing the generated aphorisms, or None on failure
    """
    client = get_llm_client()
    model = model or get_default_model()

    print(f"Starting generation: {num_aphorisms} aphorisms (model: {model})")

    # Base params with optional temperature boost for diversity
    base_temp = GENERATOR_CONFIG["temperature"]
    temp = max(0.85, base_temp) if structure_mode == "diverse" else base_temp

    params = get_completion_params(
        model,
        max_tokens=GENERATOR_CONFIG["max_tokens"],
        temperature=temp
    )

    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": build_prompt(num_aphorisms, structure_mode)}
        ],
        **params
    )

    content = response.choices[0].message.content
    aphorisms, error = parse_llm_json_response(content, GENERATOR_CONFIG["item_keys"])

    if error:
        print(f"Error: {error}")
        return None

    return {
        "generated_at": datetime.now().isoformat(),
        "model_used": model,
        "num_aphorisms": len(aphorisms),
        "aphorisms": aphorisms
    }


def save_aphorisms(data, output_format="markdown"):
    """Save aphorisms to file."""
    return save_output(
        data,
        prefix=GENERATOR_CONFIG["name"],
        format_markdown=format_markdown,
        output_format=output_format
    )


def main():
    """Standalone execution entry point."""
    run_generation(
        generate_aphorisms,
        save_aphorisms,
        success_message="Aphorisms generated! Ready to dominate intellectual Twitter.",
        num_aphorisms=25
    )


if __name__ == "__main__":
    main()
