#!/usr/bin/env python3
"""
About Page Generator - Compelling Substack About pages that convert.

This monad generates About pages optimized for subscriber conversion.
Unlike other generators, this one composes with demographic and style
inputs to create targeted, authentic copy.

About pages are critical conversion points. This generator creates content that:
- Hooks the reader immediately with relatable positioning
- Builds credibility without seeming desperate
- Creates FOMO/urgency around subscribing
- Matches the writer's style and target demographic
- Feels authentically human (anti-AI-tell embedded)
"""

import os
import sys
import json
from datetime import datetime

# Import shared utilities - the common protocol for all generators
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from utils import (
    get_llm_client,
    get_default_model,
    get_completion_params,
    clean_json_response,
    save_output,
    check_api_key
)

# ============ CONFIGURATION ============

GENERATOR_CONFIG = {
    "name": "about_page",
    "max_tokens": 3000,
    "temperature": 0.75,
}

SYSTEM_PROMPT = """You are an expert at writing compelling Substack About pages that convert readers into subscribers. You understand psychological triggers, audience targeting, and authentic voice. You NEVER use generic marketing language or AI tells. Always respond with valid JSON only."""


def build_targeted_prompt(demographic_json: dict, style_json: dict, newsletter_topic: str, target_words: int) -> str:
    """Build prompt when demographic and style inputs are provided."""
    return f"""You are creating a compelling Substack About page that will convert readers into subscribers.

TARGET READER DEMOGRAPHIC:
{json.dumps(demographic_json, indent=2)}

WRITING STYLE TO MATCH:
{json.dumps(style_json, indent=2)}

NEWSLETTER TOPIC: {newsletter_topic or "inferred from demographic interests"}

TARGET LENGTH: ~{target_words} words

YOUR TASK:

Create an About page that:

1. **IMMEDIATE HOOK** (first 1-2 sentences)
   - Speak directly to the target demographic's pain points/desires
   - Make them feel seen/understood instantly
   - Create curiosity about what you offer

2. **POSITIONING** (next paragraph)
   - What this newsletter is (and crucially, what it's NOT)
   - Why it exists / what gap it fills
   - Your unique angle/perspective

3. **CREDIBILITY** (subtle, not desperate)
   - Why you're qualified to write this
   - Evidence of expertise (without bragging)
   - Social proof if relevant (but not forced)

4. **WHAT THEY'LL GET** (concrete value prop)
   - Specific types of content
   - Frequency expectations
   - Unique insights/access they can't get elsewhere

5. **CONVERSION CLOSE** (final paragraph)
   - Clear CTA to subscribe
   - Create slight FOMO (what they'll miss if they don't)
   - Remove friction (free, easy to unsubscribe, etc.)

CRITICAL REQUIREMENTS:

- Match the writing style EXACTLY (voice, rhythm, vocabulary, humor level)
- Speak to the demographic's specific worldview and interests
- NO generic startup/marketing speak ("join our community", "on a mission to", etc.)
- NO desperation or over-promising
- Feel authentically human (varied sentence lengths, natural transitions, personality)
- Use "I" or "we" appropriately based on style
- Be specific, not abstract

Return as JSON with these fields:
- about_page_text: the full About page content
- hook_strategy: brief note on the opening strategy
- positioning_angle: what makes this newsletter unique
- conversion_elements: what psychological triggers are used
- authenticity_notes: how human authenticity is maintained
- word_count: actual word count"""


def build_standalone_prompt(topic_desc: str, target_words: int) -> str:
    """Build prompt for standalone generation without demographic/style inputs."""
    return f"""You are creating a compelling Substack About page for a newsletter about: {topic_desc}

TARGET LENGTH: ~{target_words} words

YOUR TASK:

Create an About page that converts curious visitors into subscribers.

STRUCTURE:

1. **IMMEDIATE HOOK** (first 1-2 sentences)
   - Speak to a specific reader pain point or desire
   - Make them feel understood
   - Create curiosity

2. **POSITIONING** (next paragraph)
   - What this newsletter is (and what it's NOT)
   - Why it exists
   - Unique angle

3. **CREDIBILITY** (subtle)
   - Why you're qualified
   - Evidence without bragging

4. **VALUE PROPOSITION** (concrete)
   - Specific content types
   - Frequency
   - Unique insights

5. **CONVERSION CLOSE** (final paragraph)
   - Clear subscribe CTA
   - Slight FOMO
   - Remove friction

CRITICAL REQUIREMENTS:

- Authentically human voice (no AI-speak or marketing jargon)
- Varied sentence structure and rhythm
- Specific, not abstract
- Personality and perspective
- NO: "join the community", "on a mission", "deep dives", "navigate", etc.

Return as JSON with these fields:
- about_page_text: the full About page
- hook_strategy: opening strategy used
- positioning_angle: unique newsletter angle
- conversion_elements: psychological triggers
- authenticity_notes: human authenticity maintenance
- target_demographic_inferred: who this would appeal to most
- word_count: actual word count"""


# ============ MARKDOWN FORMATTER ============

def format_markdown(data: dict, f) -> None:
    """Format about page as markdown - the unique output form of this monad."""
    f.write("# Substack About Page\n\n")
    f.write(f"*Generated on {data['generated_at']} using {data['model_used']}*\n\n")

    if data.get('newsletter_topic'):
        f.write(f"**Newsletter Topic:** {data['newsletter_topic']}\n\n")

    f.write(f"**Target Length:** {data['target_length']} (~{data['target_words']} words)\n")
    f.write(f"**Actual Word Count:** {data.get('word_count', 'N/A')}\n\n")

    f.write("---\n\n")
    f.write("## THE ABOUT PAGE\n\n")
    f.write(data['about_page_text'])
    f.write("\n\n---\n\n")

    f.write("## GENERATION STRATEGY\n\n")
    f.write(f"**Hook Strategy:** {data['hook_strategy']}\n\n")
    f.write(f"**Positioning Angle:** {data['positioning_angle']}\n\n")
    f.write(f"**Conversion Elements:** {data['conversion_elements']}\n\n")
    f.write(f"**Authenticity Notes:** {data['authenticity_notes']}\n\n")

    if data.get('target_demographic_inferred'):
        f.write(f"**Inferred Target Demographic:** {data['target_demographic_inferred']}\n\n")

    if data.get('used_demographic'):
        f.write("*Generated using targeted reader demographic*\n\n")

    if data.get('used_style'):
        f.write("*Generated using specific writing style*\n\n")


# ============ CORE FUNCTIONS ============

def generate_about_page(
    demographic_json=None,
    style_json=None,
    newsletter_topic=None,
    length="medium",
    model=None
):
    """
    Generate a Substack About page.

    This generator composes with other monad outputs - it can take
    demographic and style JSONs from reader_demographics and writing_styles
    to create targeted, styled About pages.

    Args:
        demographic_json: Optional reader demographic dict (from reader_demographics.py)
        style_json: Optional writing style dict (from writing_styles.py)
        newsletter_topic: Topic/focus of the newsletter
        length: "short" (~200 words), "medium" (~400 words), "long" (~600 words)
        model: LLM model to use

    Returns:
        Dictionary containing the generated about page, or None on failure
    """
    client = get_llm_client()
    model = model or get_default_model()

    word_count_map = {"short": 200, "medium": 400, "long": 600}
    target_words = word_count_map.get(length, 400)

    # Build prompt based on what's provided
    if demographic_json and style_json:
        prompt = build_targeted_prompt(demographic_json, style_json, newsletter_topic, target_words)
    else:
        topic_desc = newsletter_topic or "a cultural/intellectual newsletter"
        prompt = build_standalone_prompt(topic_desc, target_words)

    print(f"Generating About page (~{target_words} words, model: {model})")

    params = get_completion_params(
        model,
        max_tokens=GENERATOR_CONFIG["max_tokens"],
        temperature=GENERATOR_CONFIG["temperature"]
    )

    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ],
        **params
    )

    content = response.choices[0].message.content
    content = clean_json_response(content)

    try:
        about_data = json.loads(content)
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}")
        print(f"Raw content: {content[:500]}...")
        return None

    return {
        "generated_at": datetime.now().isoformat(),
        "model_used": model,
        "target_length": length,
        "target_words": target_words,
        "used_demographic": bool(demographic_json),
        "used_style": bool(style_json),
        "newsletter_topic": newsletter_topic,
        **about_data
    }


def save_about_page(data, output_format="markdown"):
    """Save about page to file."""
    return save_output(
        data,
        prefix=GENERATOR_CONFIG["name"],
        format_markdown=format_markdown,
        output_format=output_format
    )


def main():
    """Standalone execution entry point."""
    if not check_api_key():
        return

    about_data = generate_about_page(
        newsletter_topic="Critical analysis of tech culture, AI hype, and Silicon Valley ideology",
        length="medium"
    )

    if about_data:
        print("\nSaving results...\n")
        save_about_page(about_data, output_format="markdown")
        save_about_page(about_data, output_format="json")
        print(f"\nAbout page generated! ({about_data.get('word_count', 'N/A')} words)")
    else:
        print("Generation failed")


if __name__ == "__main__":
    main()
