#!/usr/bin/env python3
"""
Reader Demographics Generator - Granular Substack/Medium reader profiles.

This monad generates hyper-specific micro-demographic profiles that capture
real behavioral patterns and interest networks for content targeting.
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
    "name": "reader_demographics",
    "item_keys": ["demographics", "reader_demographics", "profiles"],
    "max_tokens": 6000,
    "temperature": 0.8,
}

SYSTEM_PROMPT = """You are an expert in demographic analysis, cultural anthropology, and digital media consumption patterns. You create detailed, nuanced reader personas that capture authentic behavioral patterns and interest networks. Always respond with valid JSON."""


def build_prompt(num_demographics: int) -> str:
    """Build the user prompt for this generator."""
    return f"""You are an expert in digital media demographics, sociology, and cultural analysis with deep knowledge of online reading communities.

Generate {num_demographics} HIGHLY SPECIFIC and GRANULAR demographic profiles of Substack and Medium readers. These should be SUPER NICHE micro-demographics that capture real behavioral patterns.

For each demographic, provide:

1. **Demographic Label**: A memorable, evocative name (e.g., "Reformed Tech Bro Seeking Meaning", "Cottagecore Philosophy PhD Dropout")

2. **Core Identity Markers**: 3-5 defining characteristics (age range, profession, life stage, cultural positioning)

3. **Primary Reading Motivations**: What drives them to Substack/Medium specifically

4. **Content Preferences**: Types of articles/newsletters they gravitate toward

5. **Auxiliary Interest Vectors**: 8-12 SPECIFIC secondary interests that serve as semantic bridges (be granular - not just "technology" but "open-source municipal infrastructure projects" or "vintage synthesizer repair")

6. **Media Diet**: Other platforms, podcasts, books, or media they consume

7. **Engagement Patterns**: How they interact with content (lurker vs commenter, sharing behavior, subscription habits)

8. **Psychographic Profile**: Values, worldview, aspirations, anxieties

9. **Discovery Pathways**: How they find new content (algorithmic, social, word-of-mouth, etc.)

10. **Quote/Persona Snapshot**: A characteristic 2-3 sentence quote that captures their voice and perspective

Make each demographic GENUINELY DISTINCT and HYPER-SPECIFIC. Avoid generic categories. Think in terms of:
- The "Rationalist-Adjacent Indie Game Dev Who Reads Ribbonfarm"
- The "Burned Out Social Worker Exploring Contemplative Practice and Systems Thinking"
- The "Second-Career Data Analyst Obsessed With Urban Planning and Train Infrastructure"
- The "Millennial Classics Professor Moonlighting as a Perfume Blogger"
- The "Ex-Finance Bro Building a Permaculture Homestead Who Still Reads Economics Papers"

Create genuinely interesting, realistic, multi-dimensional reader personas with RICH auxiliary interest profiles.

Return as a JSON object with a 'demographics' key containing an array of demographic objects. Each demographic object should have fields: label, identity_markers, reading_motivations, content_preferences, auxiliary_interests, media_diet, engagement_patterns, psychographic_profile, discovery_pathways, persona_quote."""


# ============ MARKDOWN FORMATTER ============

def format_markdown(data: dict, f) -> None:
    """Format reader demographics as markdown - the unique output form of this monad."""
    f.write("# Substack & Medium Reader Demographics\n\n")
    f.write(f"*Generated on {data['generated_at']} using {data['model_used']}*\n\n")
    f.write(f"**Total Demographics:** {data['num_demographics']}\n\n")
    f.write("---\n\n")

    for i, demo in enumerate(data['demographics'], 1):
        f.write(f"## {i}. {demo.get('label', 'Untitled Demographic')}\n\n")

        if 'identity_markers' in demo:
            f.write("### Core Identity Markers\n")
            markers = demo['identity_markers']
            if isinstance(markers, list):
                for marker in markers:
                    f.write(f"- {marker}\n")
            else:
                f.write(f"{markers}\n")
            f.write("\n")

        if 'reading_motivations' in demo:
            f.write(f"**Primary Reading Motivations:** {demo['reading_motivations']}\n\n")

        if 'content_preferences' in demo:
            f.write(f"**Content Preferences:** {demo['content_preferences']}\n\n")

        if 'auxiliary_interests' in demo:
            f.write("### Auxiliary Interest Vectors\n")
            interests = demo['auxiliary_interests']
            if isinstance(interests, list):
                for interest in interests:
                    f.write(f"- {interest}\n")
            else:
                f.write(f"{interests}\n")
            f.write("\n")

        if 'media_diet' in demo:
            f.write(f"**Media Diet:** {demo['media_diet']}\n\n")

        if 'engagement_patterns' in demo:
            f.write(f"**Engagement Patterns:** {demo['engagement_patterns']}\n\n")

        if 'psychographic_profile' in demo:
            f.write(f"**Psychographic Profile:** {demo['psychographic_profile']}\n\n")

        if 'discovery_pathways' in demo:
            f.write(f"**Discovery Pathways:** {demo['discovery_pathways']}\n\n")

        if 'persona_quote' in demo:
            f.write("**Persona Quote:**\n")
            f.write(f"> {demo['persona_quote']}\n\n")

        f.write("---\n\n")


# ============ CORE FUNCTIONS ============

def generate_reader_demographics(num_demographics=10, output_format="markdown", model=None):
    """
    Generate diverse reader demographic profiles.

    Args:
        num_demographics: Number of distinct demographics to generate
        output_format: 'markdown' or 'json'
        model: LLM model to use (defaults to configured default)

    Returns:
        Dictionary containing the generated demographics, or None on failure
    """
    client = get_llm_client()
    model = model or get_default_model()

    print(f"Starting generation: {num_demographics} reader demographics (model: {model})")

    params = get_completion_params(
        model,
        max_tokens=GENERATOR_CONFIG["max_tokens"],
        temperature=GENERATOR_CONFIG["temperature"]
    )

    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": build_prompt(num_demographics)}
        ],
        **params
    )

    content = response.choices[0].message.content

    if not content:
        print("Error: API returned empty content")
        return None

    demographics, error = parse_llm_json_response(content, GENERATOR_CONFIG["item_keys"])

    if error:
        print(f"Error: {error}")
        return None

    return {
        "generated_at": datetime.now().isoformat(),
        "model_used": model,
        "num_demographics": len(demographics),
        "demographics": demographics
    }


def save_demographics(data, output_format="markdown"):
    """Save reader demographics to file."""
    return save_output(
        data,
        prefix=GENERATOR_CONFIG["name"],
        format_markdown=format_markdown,
        output_format=output_format
    )


def main():
    """Standalone execution entry point."""
    run_generation(
        generate_reader_demographics,
        save_demographics,
        success_message="Reader demographics generated! Use these to target specific personas.",
        num_demographics=15
    )


if __name__ == "__main__":
    main()
