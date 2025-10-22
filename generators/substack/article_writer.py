#!/usr/bin/env python3
"""
Generate long-form Substack articles optimized for specific reader demographics and writing styles.
Includes embedded human authenticity validation to avoid AI tells.
"""

import os
import json
from datetime import datetime
from openai import OpenAI

def generate_article(
    demographic_json: dict,
    style_json: dict,
    topic: str,
    word_count: str = "medium",
    model: str = "gpt-4o"
):
    """
    Generate a long-form article targeted to a specific demographic using a specific style.

    Args:
        demographic_json: Full demographic profile from reader_demographics
        style_json: Full writing style from writing_styles
        topic: Article topic/prompt from user
        word_count: "short" (~1500), "medium" (~3000), "long" (~5000)
        model: OpenAI model to use

    Returns:
        Dictionary containing the generated article and metadata
    """

    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    # Map word count to target
    word_targets = {
        "short": 1500,
        "medium": 3000,
        "long": 5000
    }
    target_words = word_targets.get(word_count, 3000)

    # Extract key demographic info
    demographic_label = demographic_json.get('label', 'Unknown Demographic')
    auxiliary_interests = demographic_json.get('auxiliary_interests', [])
    psychographic = demographic_json.get('psychographic_profile', '')

    # Extract key style info
    style_name = style_json.get('name', 'Unknown Style')
    tone_voice = style_json.get('tone_voice', '')
    sentence_structure = style_json.get('sentence_structure', '')
    vocabulary = style_json.get('vocabulary', '')

    prompt = f"""You are writing a long-form Substack article for publication.

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
   - Speaks to their interests: {', '.join(auxiliary_interests[:5]) if isinstance(auxiliary_interests, list) else auxiliary_interests}
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
   ❌ "It's important to note" / "It's important to remember"
   ❌ "Certainly"
   ❌ "Delve" / "delving"
   ❌ "Navigating the [X]"
   ❌ "Based on the information provided"
   ❌ Hedge words: "typically", "often", "might be", "could be", "tends to"
   ❌ Generic transitions: "Furthermore", "Moreover", "Additionally"

   **REQUIRED ELEMENTS:**
   ✓ Make DEFINITIVE claims without hedging
   ✓ Include specific numbers, names, sensory details
   ✓ Reference CONCRETE examples, not abstract categories
   ✓ Take strong positions rather than "balanced perspectives"
   ✓ Include ONE intentional minor inconsistency or quirk (imperfection is human)
   ✓ Use colloquialisms and informal constructions
   ✓ Include observational asides
   ✓ Reference the writing process itself occasionally
   ✓ Let thoughts develop non-linearly where natural
   ✓ Include at least one unexpected word choice or neologism

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

    print(f"📝 Generating article using {model}...")
    print(f"🎯 Target: {demographic_label}")
    print(f"✍️  Style: {style_name}")
    print(f"📊 Length: ~{target_words} words\n")

    # Call OpenAI API
    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "system",
                "content": "You are an expert long-form writer for Substack. You write authentic, human-feeling content that resonates deeply with specific reader demographics. You never produce generic AI-sounding text."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        max_tokens=8000 if model == "gpt-4o" else None,
        max_completion_tokens=8000 if model != "gpt-4o" else None,
        temperature=0.9  # Higher temp for more creative, less formulaic output
    )

    article_content = response.choices[0].message.content

    # Build result with metadata
    result = {
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

    return result


def save_article(article_data, output_format="markdown"):
    """Save the generated article to a file."""

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    # Clean demographic and style names for filename
    demo_slug = article_data['target_demographic'].lower().replace(' ', '_')[:30]
    style_slug = article_data['writing_style'].lower().replace(' ', '_')[:30]

    if output_format == "json":
        filename = f"article_{demo_slug}_{style_slug}_{timestamp}.json"
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(article_data, f, indent=2, ensure_ascii=False)
        print(f"✅ Saved article to {filename}")

    else:  # markdown
        filename = f"article_{demo_slug}_{style_slug}_{timestamp}.md"
        with open(filename, "w", encoding="utf-8") as f:
            # Write metadata header
            f.write("---\n")
            f.write("GENERATION METADATA\n")
            f.write(f"Target Demographic: {article_data['target_demographic']}\n")
            f.write(f"Writing Style: {article_data['writing_style']}\n")
            f.write(f"Topic: {article_data['topic']}\n")
            f.write(f"Target Word Count: {article_data['target_word_count']}\n")
            f.write(f"Actual Word Count: {article_data['actual_word_count']}\n")
            f.write(f"Authenticity Validation: {article_data['authenticity_validation']}\n")
            f.write(f"Model: {article_data['model_used']}\n")
            f.write(f"Generated: {article_data['generated_at']}\n")
            f.write("---\n\n")

            # Write article content
            f.write(article_data['article'])

            # Write validation notice
            f.write("\n\n---\n\n")
            f.write("*This article was generated using monad-optimized cultural production with embedded human authenticity validation.*\n")

        print(f"✅ Saved article to {filename}")

    return filename


def main():
    """Test function - not used in production."""
    print("Article writer generator loaded successfully.")
    print("Use via API endpoint, not directly.")


if __name__ == "__main__":
    main()
