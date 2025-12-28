#!/usr/bin/env python3
"""
Soft + Hard + Algorithmic Demographics Generator - Three-dimensional Twitter profiles.

This monad generates granular Twitter/X demographic profiles mapping:
- SOFT interactions: psychological, being-in-the-world, Bourdieu-inspired cultural capital
- HARD interactions: technical UI patterns, behavioral metrics, tool-at-hand psychology
- ALGORITHMIC awareness: understanding/exploitation of X's recommendation system
  (UTEG/GraphJet, light-ranker vs heavy-ranker, candidate sources, visibility filters)
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
    "name": "twitter_demographics",
    "item_keys": ["demographics", "profiles", "personas", "tribes"],
    "max_tokens": 10000,
    "temperature": 0.7,
}

SYSTEM_PROMPT = """You are an expert in digital sociology, Bourdieu's theories of cultural and symbolic capital, phenomenology of technology, and platform psychology. You understand Twitter as both a technical system and a social field where status games play out through specific behavioral and aesthetic patterns. Always respond with valid JSON."""


def build_prompt(num_demographics: int) -> str:
    """Build the soft+hard+algorithmic demographics prompt."""
    return f"""You are an expert in digital anthropology, Bourdieu's cultural capital theory, phenomenology of technology, behavioral psychology of social platforms, AND the technical architecture of Twitter/X's recommendation algorithm (as revealed in their open-source release).

Generate {num_demographics} HYPER-GRANULAR Twitter/X demographic profiles that map BOTH soft and hard dimensions of platform interaction, PLUS their relationship to the actual recommendation algorithm.

For each demographic, provide:

**IDENTITY & POSITIONING**
1. **Demographic Label**: Evocative, specific (e.g., "Reformed Tech Bro Performing Humility Through Lowercase", "Econ PhD Dunking From Associate Professor Position")

2. **Cultural Capital Markers**: Specific thinkers/books/concepts they signal knowledge of (not "philosophy" but "late Wittgenstein, Dreyfus on Heidegger, predictive processing")

3. **Status Position & Performance**: How they position themselves in intellectual hierarchies

**SOFT INTERACTIONS (Being-in-the-World)**
4. **Habitus on Platform**: Their embodied relationship to Twitter
5. **Cultural Capital Strategy**: How they accumulate/display/convert capital
6. **Symbolic Boundaries**: What/who they distance themselves from
7. **Anxiety Patterns**: What threatens their position
8. **Subliminal Motivations**: What they're REALLY doing

**HARD INTERACTIONS (Technical/Behavioral)**
9. **Composition Patterns**: How they write tweets
10. **UI Interaction Signature**: Specific behavioral patterns
11. **Temporal Patterns**: When/how they post
12. **Engagement Calculus**: How they decide to interact
13. **Tool-at-Hand Psychology**: How Twitter interfaces with cognition

**ALGORITHMIC AWARENESS (Based on X's Open-Source Algorithm)**
14. **Algorithmic Literacy Level**: Scale: Folk Theory -> Partial Understanding -> Technical Mastery
15. **Graph Positioning Strategy**: How they position in UTEG. Strategic replies to mutuals?
16. **Candidate Source Optimization**: Optimizing for In-Network or Out-of-Network?
17. **Ranking Signal Awareness**: Light-ranker vs Heavy-ranker optimization
18. **Engagement Prediction Gaming**: Strategic hooks? Thread structures for dwell time?
19. **Visibility Filter Navigation**: How close to content moderation boundaries?
20. **Feed Composition Theory**: Correct or incorrect mental models?

**CROSS-CUTTING DIMENSIONS**
21. **Capitalization Aesthetic**: ALL CAPS, lowercase, proper - and what this signals
22. **Quote-Tweet vs Reply Ethics**: Philosophy on dunking vs good-faith engagement
23. **Ratioing Relationship**: Do they ratio? Fear it? Seek it?
24. **Thread Culture**: Solo threads, collaborative, reply-guy, thread-reader
25. **Persona Quote**: 2-3 sentences capturing their voice

Make each DEEPLY SPECIFIC and SOCIOLOGICALLY RICH. Cover tribes: rationalists, econ theory, ML/AI, cultural criticism, academic, reformed tech, philosophy, systems thinking, algorithm hackers, folk theory believers.

Return as JSON with fields: label, cultural_capital_markers, status_performance, habitus, capital_strategy, symbolic_boundaries, anxiety_patterns, subliminal_motivations, composition_patterns, ui_signature, temporal_patterns, engagement_calculus, tool_psychology, algorithmic_literacy_level, graph_positioning_strategy, candidate_source_optimization, ranking_signal_awareness, engagement_prediction_gaming, visibility_filter_navigation, feed_composition_theory, capitalization_aesthetic, quote_tweet_ethics, ratioing_relationship, thread_culture, persona_quote."""


# ============ MARKDOWN FORMATTER ============

def format_markdown(data: dict, f) -> None:
    """Format soft+hard+algorithmic demographics as markdown."""
    f.write("# Twitter/X Demographics: Soft + Hard + Algorithmic Awareness Mapping\n\n")
    f.write(f"*Generated on {data['generated_at']} using {data['model_used']}*\n\n")
    f.write("*Mapping three dimensions:*\n")
    f.write("- **SOFT**: Cultural capital, habitus, being-in-the-world (Bourdieu-inspired)\n")
    f.write("- **HARD**: UI patterns, behavioral metrics, technical interactions\n")
    f.write("- **ALGORITHMIC**: Understanding/exploitation of X's recommendation system\n\n")
    f.write(f"**Total Demographics:** {data['num_demographics']}\n\n")
    f.write("---\n\n")

    for i, demo in enumerate(data['demographics'], 1):
        f.write(f"## {i}. {demo.get('label', 'Untitled Demographic')}\n\n")

        # SOFT INTERACTIONS
        f.write("### SOFT INTERACTIONS (Being-in-the-World)\n\n")

        if 'cultural_capital_markers' in demo:
            f.write("**Cultural Capital Markers:**\n")
            markers = demo['cultural_capital_markers']
            if isinstance(markers, list):
                for marker in markers:
                    f.write(f"- {marker}\n")
            else:
                f.write(f"{markers}\n")
            f.write("\n")

        for field, label in [
            ('status_performance', 'Status Position & Performance'),
            ('habitus', 'Habitus on Platform'),
            ('capital_strategy', 'Cultural Capital Strategy'),
            ('symbolic_boundaries', 'Symbolic Boundaries'),
            ('anxiety_patterns', 'Anxiety Patterns'),
            ('subliminal_motivations', 'Subliminal Motivations'),
        ]:
            if field in demo:
                f.write(f"**{label}:** {demo[field]}\n\n")

        # HARD INTERACTIONS
        f.write("### HARD INTERACTIONS (Technical/Behavioral)\n\n")

        for field, label in [
            ('composition_patterns', 'Composition Patterns'),
            ('ui_signature', 'UI Interaction Signature'),
            ('temporal_patterns', 'Temporal Patterns'),
            ('engagement_calculus', 'Engagement Calculus'),
            ('tool_psychology', 'Tool-at-Hand Psychology'),
        ]:
            if field in demo:
                f.write(f"**{label}:** {demo[field]}\n\n")

        # ALGORITHMIC AWARENESS
        f.write("### ALGORITHMIC AWARENESS (X's Recommendation System)\n\n")

        for field, label in [
            ('algorithmic_literacy_level', 'Algorithmic Literacy Level'),
            ('graph_positioning_strategy', 'Graph Positioning Strategy (UTEG/GraphJet)'),
            ('candidate_source_optimization', 'Candidate Source Optimization'),
            ('ranking_signal_awareness', 'Ranking Signal Awareness'),
            ('engagement_prediction_gaming', 'Engagement Prediction Gaming'),
            ('visibility_filter_navigation', 'Visibility Filter Navigation'),
            ('feed_composition_theory', 'Feed Composition Theory'),
        ]:
            if field in demo:
                f.write(f"**{label}:** {demo[field]}\n\n")

        # CROSS-CUTTING
        f.write("### CROSS-CUTTING DIMENSIONS\n\n")

        for field, label in [
            ('capitalization_aesthetic', 'Capitalization Aesthetic'),
            ('quote_tweet_ethics', 'Quote-Tweet vs Reply Ethics'),
            ('ratioing_relationship', 'Ratioing Relationship'),
            ('thread_culture', 'Thread Culture'),
        ]:
            if field in demo:
                f.write(f"**{label}:** {demo[field]}\n\n")

        if 'persona_quote' in demo:
            f.write("**Persona Quote:**\n")
            f.write(f"> {demo['persona_quote']}\n\n")

        f.write("---\n\n")


# ============ CORE FUNCTIONS ============

def generate_twitter_demographics(num_demographics=12, output_format="markdown", model=None):
    """
    Generate detailed Twitter demographic profiles with soft + hard + algorithmic mapping.

    Args:
        num_demographics: Number of distinct demographics
        output_format: 'markdown' or 'json'
        model: LLM model to use

    Returns:
        Dictionary containing the generated demographics, or None on failure
    """
    client = get_llm_client()
    model = model or get_default_model()

    print(f"Starting generation: {num_demographics} Twitter demographics (model: {model})")

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


def save_twitter_demographics(data, output_format="markdown"):
    """Save Twitter demographics to file."""
    return save_output(
        data,
        prefix=GENERATOR_CONFIG["name"],
        format_markdown=format_markdown,
        output_format=output_format
    )


def main():
    """Standalone execution entry point."""
    run_generation(
        generate_twitter_demographics,
        save_twitter_demographics,
        success_message="Deep sociological + algorithmic mapping complete!",
        num_demographics=15
    )


if __name__ == "__main__":
    main()
