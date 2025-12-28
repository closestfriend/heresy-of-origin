#!/usr/bin/env python3
"""
Writing Styles Generator - Literary style descriptions for Substack content.

This monad generates distinct writing style archetypes that can guide
AI assistants in article writing with specific voice and tone.
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
    "name": "writing_styles",
    "item_keys": ["styles", "writing_styles"],
    "max_tokens": 4000,
    "temperature": 0.7,
}

SYSTEM_PROMPT = """You are an expert in literary analysis and writing styles. You provide detailed, nuanced descriptions that capture the essence of different writing approaches. Always respond with valid JSON."""


def build_prompt(num_styles: int) -> str:
    """Build the user prompt for this generator."""
    return f"""You are a literary expert and writing coach with deep knowledge of various writing traditions, from classical to contemporary.

Generate {num_styles} DISTINCT and sophisticated writing styles that would appeal to literary nerds reading Substack newsletters. For each style, provide:

1. **Style Name**: A memorable, evocative name
2. **Core Characteristics**: 3-5 defining features of this style
3. **Tone & Voice**: The emotional and intellectual register
4. **Sentence Structure**: Typical patterns and rhythms
5. **Vocabulary & Diction**: Word choice preferences
6. **Literary Influences**: Key authors or movements that exemplify this style
7. **Best Used For**: Topics or contexts where this style shines
8. **Example Opening**: A sample 2-3 sentence opening demonstrating the style

Make each style genuinely DISTINCT - avoid overlap. Include both classic and contemporary approaches. Think of styles like:
- The erudite essayist (Didion, Sontag)
- The lyrical poet-journalist (Gay Talese, John McPhee)
- The sharp cultural critic (Paglia, Hitchens)
- The intimate confessionalist (Baldwin, Sedaris)
- The maximalist baroque (Pynchon, Wallace)
- The minimalist precision (Carver, Hemingway)
- And others you find compelling...

Return the response as a JSON array where each style is an object with fields: name, characteristics, tone_voice, sentence_structure, vocabulary, influences, best_for, example_opening."""


# ============ MARKDOWN FORMATTER ============

def format_markdown(data: dict, f) -> None:
    """Format writing styles as markdown - the unique output form of this monad."""
    f.write("# Literary Writing Styles for Substack\n\n")
    f.write(f"*Generated on {data['generated_at']} using {data['model_used']}*\n\n")
    f.write(f"**Total Styles:** {data['num_styles']}\n\n")
    f.write("---\n\n")

    for i, style in enumerate(data['styles'], 1):
        f.write(f"## {i}. {style.get('name', 'Untitled Style')}\n\n")

        if 'characteristics' in style:
            f.write("### Core Characteristics\n")
            chars = style['characteristics']
            if isinstance(chars, list):
                for char in chars:
                    f.write(f"- {char}\n")
            else:
                f.write(f"{chars}\n")
            f.write("\n")

        if 'tone_voice' in style:
            f.write(f"**Tone & Voice:** {style['tone_voice']}\n\n")

        if 'sentence_structure' in style:
            f.write(f"**Sentence Structure:** {style['sentence_structure']}\n\n")

        if 'vocabulary' in style:
            f.write(f"**Vocabulary & Diction:** {style['vocabulary']}\n\n")

        if 'influences' in style:
            f.write("**Literary Influences:** ")
            influences = style['influences']
            if isinstance(influences, list):
                f.write(", ".join(influences))
            else:
                f.write(str(influences))
            f.write("\n\n")

        if 'best_for' in style:
            f.write(f"**Best Used For:** {style['best_for']}\n\n")

        if 'example_opening' in style:
            f.write("**Example Opening:**\n")
            f.write(f"> {style['example_opening']}\n\n")

        f.write("---\n\n")


# ============ CORE FUNCTIONS ============

def generate_writing_styles(num_styles=10, output_format="markdown", model=None):
    """
    Generate diverse writing style descriptions.

    Args:
        num_styles: Number of distinct styles to generate
        output_format: 'markdown' or 'json'
        model: LLM model to use (defaults to configured default)

    Returns:
        Dictionary containing the generated styles, or None on failure
    """
    client = get_llm_client()
    model = model or get_default_model()

    print(f"Starting generation: {num_styles} writing styles (model: {model})")

    params = get_completion_params(
        model,
        max_tokens=GENERATOR_CONFIG["max_tokens"],
        temperature=GENERATOR_CONFIG["temperature"]
    )

    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": build_prompt(num_styles)}
        ],
        **params
    )

    content = response.choices[0].message.content
    styles, error = parse_llm_json_response(content, GENERATOR_CONFIG["item_keys"])

    if error:
        print(f"Error: {error}")
        return None

    return {
        "generated_at": datetime.now().isoformat(),
        "model_used": model,
        "num_styles": len(styles),
        "styles": styles
    }


def save_styles(data, output_format="markdown"):
    """Save writing styles to file."""
    return save_output(
        data,
        prefix=GENERATOR_CONFIG["name"],
        format_markdown=format_markdown,
        output_format=output_format
    )


def main():
    """Standalone execution entry point."""
    run_generation(
        generate_writing_styles,
        save_styles,
        success_message="Writing styles generated! Use these to guide article writing.",
        num_styles=12
    )


if __name__ == "__main__":
    main()
