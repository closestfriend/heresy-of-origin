#!/usr/bin/env python3
"""
Article Writer Generator - Long-form Substack articles with authenticity validation.

This monad generates publication-ready articles targeted to specific demographics
and styled according to specific writing patterns. It composes with outputs from
reader_demographics and writing_styles generators.

Unlike other generators that produce structured JSON data, this one produces
raw text content - the article itself. It includes embedded human authenticity
validation to avoid AI tells.
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
    check_api_key
)

# ============ CONFIGURATION ============

GENERATOR_CONFIG = {
    "name": "article",
    "max_tokens": 8000,
    "temperature": 0.9,
}

SYSTEM_PROMPT = """You are an expert long-form writer for Substack. You write authentic, human-feeling content that resonates deeply with specific reader demographics. You never produce generic AI-sounding text."""


def build_prompt(demographic_json: dict, style_json: dict, topic: str, target_words: int) -> str:
    """Build the article generation prompt with embedded authenticity validation."""

    # Extract key info for prompt clarity
    auxiliary_interests = demographic_json.get('auxiliary_interests', [])
    psychographic = demographic_json.get('psychographic_profile', '')
    tone_voice = style_json.get('tone_voice', '')
    sentence_structure = style_json.get('sentence_structure', '')
    vocabulary = style_json.get('vocabulary', '')

    interests_str = ', '.join(auxiliary_interests[:5]) if isinstance(auxiliary_interests, list) else auxiliary_interests

    return f"""You are writing a long-form Substack article for publication.

TARGET READER DEMOGRAPHIC:
{json.dumps(demographic_json, indent=2)}

WRITING STYLE:
{json.dumps(style_json, indent=2)}

ARTICLE TOPIC/PROMPT:
{topic}

TARGET LENGTH: ~{target_words} words

YOUR TASK:
Write a complete, publication-ready article that:

1. **RESONATES WITH THE TARGET READER:**
   - Speaks to their interests: {interests_str}
   - Addresses their psychographic profile: {psychographic}
   - Uses semantic bridges they recognize
   - Matches their intellectual positioning

2. **EMBODIES THE WRITING STYLE:**
   - Tone & voice: {tone_voice}
   - Sentence structure: {sentence_structure}
   - Vocabulary: {vocabulary}

3. **PASSES HUMAN AUTHENTICITY VALIDATION:**

   CRITICAL - APPLY THESE CONSTRAINTS:

   **STRUCTURAL VARIANCE:**
   - Vary sentence lengths dramatically (5-40 words, NEVER consistently 20-30)
   - Make paragraph architecture asymmetrical (short/long/medium unpredictably)
   - Shift voice between 1st/2nd/3rd person naturally where appropriate
   - Break expected structure in at least one paragraph

   **FORBIDDEN PHRASES (AI TELLS - DO NOT USE):**
   - "It's important to note" / "It's important to remember"
   - "Certainly"
   - "Delve" / "delving"
   - "Navigating the [X]"
   - "Based on the information provided"
   - Hedge words: "typically", "often", "might be", "could be", "tends to"
   - Generic transitions: "Furthermore", "Moreover", "Additionally"

   **REQUIRED ELEMENTS:**
   - Make DEFINITIVE claims without hedging
   - Include specific numbers, names, sensory details
   - Reference CONCRETE examples, not abstract categories
   - Take strong positions rather than "balanced perspectives"
   - Include ONE intentional minor inconsistency or quirk (imperfection is human)
   - Use colloquialisms and informal constructions
   - Include observational asides
   - Reference the writing process itself occasionally
   - Let thoughts develop non-linearly where natural
   - Include at least one unexpected word choice or neologism

   **ANTI-PATTERNS TO BREAK:**
   - NO immediate lists after rhetorical questions
   - Avoid colon-heavy constructions in headers
   - Skip parallel structure repetitions ("It's not X, it's Y")
   - Resist em-dash overuse (max 2 per major section)

   **VALIDATION HEURISTIC:**
   Before each paragraph: "Would a human writer risk this construction?"
   If the answer is universally yes, REVISE. Good writing contains calculated risks.

OUTPUT FORMAT:
# [Compelling Title]

[Article body - {target_words} words]

---

Write the complete article now. Every constraint must be applied. This must be indistinguishable from human-written content."""


# ============ MARKDOWN FORMATTER ============

def format_markdown(data: dict, f) -> None:
    """Format article with metadata header - the unique output form of this monad."""
    f.write("---\n")
    f.write("GENERATION METADATA\n")
    f.write(f"Target Demographic: {data['target_demographic']}\n")
    f.write(f"Writing Style: {data['writing_style']}\n")
    f.write(f"Topic: {data['topic']}\n")
    f.write(f"Target Word Count: {data['target_word_count']}\n")
    f.write(f"Actual Word Count: {data['actual_word_count']}\n")
    f.write(f"Authenticity Validation: {data['authenticity_validation']}\n")
    f.write(f"Model: {data['model_used']}\n")
    f.write(f"Generated: {data['generated_at']}\n")
    f.write("---\n\n")
    f.write(data['article'])
    f.write("\n\n---\n\n")
    f.write("*This article was generated using monad-optimized cultural production with embedded human authenticity validation.*\n")


# ============ CORE FUNCTIONS ============

def generate_article(
    demographic_json: dict,
    style_json: dict,
    topic: str,
    word_count: str = "medium",
    model: str = None
):
    """
    Generate a long-form article targeted to a specific demographic using a specific style.

    This generator composes with other monad outputs - it requires both a demographic
    profile and a writing style to produce targeted, authentic content.

    Args:
        demographic_json: Full demographic profile from reader_demographics
        style_json: Full writing style from writing_styles
        topic: Article topic/prompt from user
        word_count: "short" (~1500), "medium" (~3000), "long" (~5000)
        model: LLM model to use

    Returns:
        Dictionary containing the generated article and metadata, or None on failure
    """
    client = get_llm_client()
    model = model or get_default_model()

    word_targets = {"short": 1500, "medium": 3000, "long": 5000}
    target_words = word_targets.get(word_count, 3000)

    demographic_label = demographic_json.get('label', 'Unknown Demographic')
    style_name = style_json.get('name', 'Unknown Style')

    print(f"Starting generation: article (model: {model}, target: {demographic_label}, style: {style_name}, ~{target_words} words)")

    params = get_completion_params(
        model,
        max_tokens=GENERATOR_CONFIG["max_tokens"],
        temperature=GENERATOR_CONFIG["temperature"]
    )

    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": build_prompt(demographic_json, style_json, topic, target_words)}
        ],
        **params
    )

    article_content = response.choices[0].message.content
    article_content = clean_json_response(article_content)

    return {
        "generated_at": datetime.now().isoformat(),
        "model_used": model,
        "target_demographic": demographic_label,
        "writing_style": style_name,
        "topic": topic,
        "target_word_count": target_words,
        "actual_word_count": len(article_content.split()),
        "authenticity_validation": "EMBEDDED",
        "article": article_content
    }


def save_article(article_data, output_format="markdown"):
    """Save the generated article to file with descriptive filename."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    # Create filename slugs from demographic and style
    demo_slug = article_data['target_demographic'].lower().replace(' ', '_')[:30]
    style_slug = article_data['writing_style'].lower().replace(' ', '_')[:30]

    if output_format == "json":
        filename = f"article_{demo_slug}_{style_slug}_{timestamp}.json"
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(article_data, f, indent=2, ensure_ascii=False)
    else:
        filename = f"article_{demo_slug}_{style_slug}_{timestamp}.md"
        with open(filename, "w", encoding="utf-8") as f:
            format_markdown(article_data, f)

    print(f"Saved to {filename}")
    return filename


def main():
    """Standalone execution - not used in production (requires demographic/style inputs)."""
    print("Article writer generator loaded successfully.")
    print("Use via API endpoint with demographic and style inputs.")


if __name__ == "__main__":
    main()
