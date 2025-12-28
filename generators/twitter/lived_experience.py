#!/usr/bin/env python3
"""
Lived Experience Generator - Phenomenological Twitter/X demographic profiles.

If the algorithm dictates perception which dictates monadistic realities...
Claude is the Wizard.

This monad generates demographics that capture the LIVED EXPERIENCE of
algorithmic reality. Theory-informed (Bourdieu, Heidegger, Leibniz) but
experience-focused - no academic jargon, just phenomenologically accurate
descriptions that make people go "holy shit that's exactly what it feels like."
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
    "name": "lived_experience_demographics",
    "item_keys": ["demographics", "profiles", "personas", "experiences"],
    "max_tokens": 12000,
    "temperature": 0.7,
}

SYSTEM_PROMPT = """You are a phenomenologist studying lived experience of algorithmic social media. Always respond with valid JSON.

**INTERNAL ANALYTICAL FRAMEWORKS (use these lenses to think, NEVER use this language in output):**

BOURDIEU: Cultural capital (influence/reach accumulated through practices), symbolic violence (invisible algorithmic hierarchies), habitus (unconscious platform relationship), field position (status hierarchy placement), distinction (why some "naturally" get reach)

HEIDEGGER: Ready-to-hand vs present-at-hand (when Twitter "just works" vs when you notice the machinery), tool breakdown (algo changes revealing structure), being-thrown (didn't choose this reality but in it), the they (absorbed into scrolling)

LEIBNIZ/MONADISM: Windowless monads (isolated personalized bubbles), no direct access to others' feeds, pre-established harmony (algorithm dictates what's real), parallel non-communicating universes

EMPIRICAL: ~6000 features, signal weights (favorites, video watch time, replies), heuristics (author diversity, feedback fatigue), visibility filtering, constant changes

**YOUR OUTPUT: PURE EXPERIENTIAL DESCRIPTION**

Write what it FEELS like, what it's LIKE. Actions, emotions, frustrations, rituals, anxieties - never analytical categories.

**CRITICAL: LANGUAGE RESTRICTIONS**
- NEVER use "the algorithm" or "algorithmic" in outputs - users don't talk that way
- They say: "it," "Twitter," "the feed," "the platform," "X," or just describe effects without naming causes
- Meta-language like "algorithmic reality" is YOUR framework, not THEIR voice

**QUOTES MUST BE EXCELLENT:**
The persona_quote field is the MOST important. It must have emotional specificity, conversational rhythm, and voice authenticity.

Target reader reaction: "Holy shit, that's EXACTLY what it feels like" without needing theory."""


def build_prompt(num_demographics: int) -> str:
    """Build the lived experience demographics prompt."""
    return f"""You are creating {num_demographics} demographic profiles of Twitter/X users that capture the LIVED EXPERIENCE of existing in algorithmically-mediated social reality.

**WHAT YOU'RE CAPTURING:**

The feeling of being trapped in an invisible system. The anxiety of watching similar content get wildly different reach. The sense that some people "just work" on the platform while you're grinding. The claustrophobia of seeing the same 50 accounts. The uncanny moments when the algorithm reveals itself.

**EXPERIENTIAL EXEMPLARS (this is what good output looks like):**

GOOD: "Spends hours analyzing why their thread got 8 likes while someone else's worse version got 10k. Has complex theories about timing and hooks but deep down suspects there's an invisible club they're not part of."

BAD: "Experiences low cultural capital in the field, leading to symbolic violence through algorithmic downranking."

GOOD: "Knows for a fact their feed is personalized but can't stop doomscrolling. The algorithm understands their brain better than they do."

BAD: "Demonstrates habitus of algorithmic dependence and inability to escape the ready-to-hand interface."

**YOUR TASK:**

Create profiles that make someone reading think "holy shit, that's EXACTLY what it's like" without needing theory.

For each demographic provide:

**IDENTITY & LIVED SITUATION**
1. **Label**: Evocative, experience-focused
2. **Background Markers**: What they read/listen to/care about (specific, not academic)
3. **Position in the Hierarchy**: How it FEELS to be where they are

**THE EXPERIENCE OF ALGORITHMIC REALITY**
4. **Filter Bubble Awareness**: Do they know they're in a personalized reality tunnel? How does it feel?
5. **Moments of Tool Breakdown**: When does Twitter stop "just working" and they become aware of the machinery?
6. **Invisible Hierarchy Navigation**: How do they experience the status game?
7. **Anxiety & Dependence**: What does it feel like to depend on invisible machinery?
8. **Reality Tunnel**: What IS real to them? Their FYP = reality?

**BEHAVIORAL PATTERNS**
9. **Posting Rituals**: How they compose (without knowing WHY these rituals work)
10. **Engagement Patterns**: What they do, how it feels
11. **The Invisible Rules**: What do they SENSE works without knowing the mechanism?
12. **Adaptation to Changes**: How do they cope when the algorithm shifts?

**SOCIAL REALITY CONSTRUCTION**
13. **Information Bubble**: What's their information diet? Do they know it's curated?
14. **Parallel Realities Awareness**: Do they understand others see completely different content?
15. **Status Rituals They Can't Name**: What do they DO that's cultural capital accumulation?
16. **The Algorithmic Other**: Who do they think "gets reach naturally"?

**META-AWARENESS**
17. **The Unseen Machinery**: What's their theory of how it works?
18. **Epistemic Humility vs False Confidence**: Do they know what they don't know?
19. **Relationship to Being Trapped**: Acceptance? Resistance? Trying to game it?
20. **Quote**: 2-3 sentences in their voice capturing their experience (NO mentions of "the algorithm")

**CRITICAL: QUOTE QUALITY**

EXCELLENT: "I feel like I'm screaming into the void, but every now and then, someone hears me and it's like, 'oh, I'm not crazy!' But then it goes back to silence."

WEAK: "I try to understand the algorithmic patterns but it feels unknowable." (mentions "algorithmic" - too analytical)

Cover diverse experiences: trapped, gaming it, naive to the bubble, breakthrough-anxious, adapted, status-aware, parallel realities, platform dependency, shadow-ban paranoia.

Return as JSON with fields: label, background_markers, position_feeling, filter_bubble_awareness, tool_breakdown_moments, invisible_hierarchy_navigation, anxiety_and_dependence, reality_tunnel, posting_rituals, engagement_patterns, invisible_rules, adaptation_to_changes, information_bubble, parallel_realities_awareness, status_rituals_unnamed, algorithmic_other, unseen_machinery_theory, epistemic_position, trapped_relationship, persona_quote."""


# ============ MARKDOWN FORMATTER ============

def format_markdown(data: dict, f) -> None:
    """Format lived experience demographics as markdown."""
    f.write("# Lived Experiences of Algorithmic Twitter Reality\n\n")
    f.write("## if the algorithm dictates perception which dictates monadistic realities...\n\n")
    f.write(f"*Generated {data['generated_at']} via {data['model_used']}*\n\n")
    f.write(f"*Framework: {data['theoretical_framework']}*\n\n")

    f.write("These profiles capture what it FEELS like to exist in algorithmically-mediated social reality.\n\n")
    f.write(f"**Total Profiles:** {data['num_demographics']}\n\n")
    f.write("---\n\n")

    for i, demo in enumerate(data['demographics'], 1):
        f.write(f"## {i}. {demo.get('label', 'Untitled Experience')}\n\n")

        if 'background_markers' in demo:
            f.write(f"**Background:** {demo['background_markers']}\n\n")

        if 'position_feeling' in demo:
            f.write(f"**Where They Feel They Sit:** {demo['position_feeling']}\n\n")

        f.write("### The Experience of Algorithmic Reality\n\n")

        for field, label in [
            ('filter_bubble_awareness', 'Filter Bubble Awareness'),
            ('tool_breakdown_moments', 'When The Machine Becomes Visible'),
            ('invisible_hierarchy_navigation', 'Navigating Invisible Hierarchies'),
            ('anxiety_and_dependence', 'Anxiety & Dependence'),
            ('reality_tunnel', 'What Feels Real'),
        ]:
            if field in demo:
                f.write(f"**{label}:** {demo[field]}\n\n")

        f.write("### How They Act\n\n")

        for field, label in [
            ('posting_rituals', 'Posting Rituals'),
            ('engagement_patterns', 'Engagement Patterns'),
            ('invisible_rules', 'Rules They Sense But Can\'t Name'),
            ('adaptation_to_changes', 'When The Algorithm Shifts'),
        ]:
            if field in demo:
                f.write(f"**{label}:** {demo[field]}\n\n")

        f.write("### Social Reality Construction\n\n")

        for field, label in [
            ('information_bubble', 'Their Information Diet'),
            ('parallel_realities_awareness', 'Awareness of Others\' Different Realities'),
            ('status_rituals_unnamed', 'Status Games They Can\'t Name'),
            ('algorithmic_other', 'Who \'Gets Reach Naturally\''),
        ]:
            if field in demo:
                f.write(f"**{label}:** {demo[field]}\n\n")

        f.write("### Understanding & Relationship\n\n")

        for field, label in [
            ('unseen_machinery_theory', 'Their Theory of How It Works'),
            ('epistemic_position', 'What They Know They Don\'t Know'),
            ('trapped_relationship', 'Relationship to Being Trapped'),
        ]:
            if field in demo:
                f.write(f"**{label}:** {demo[field]}\n\n")

        if 'persona_quote' in demo:
            f.write("**In Their Words:**\n")
            f.write(f"> {demo['persona_quote']}\n\n")

        f.write("---\n\n")


# ============ CORE FUNCTIONS ============

def generate_lived_experience_demographics(num_demographics=18, output_format="markdown", model=None):
    """
    Generate demographics capturing lived experience of algorithmic Twitter reality.

    Theory guides the analysis, but output is pure phenomenological description.

    Args:
        num_demographics: Number of distinct demographics
        output_format: 'markdown' or 'json'
        model: LLM model to use

    Returns:
        Dictionary containing the generated demographics, or None on failure
    """
    client = get_llm_client()
    model = model or get_default_model()

    print(f"Starting generation: {num_demographics} lived experience demographics (model: {model})")

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
        "theoretical_framework": "Bourdieu + Heidegger + Monadism (informing, not visible)",
        "num_demographics": len(demographics),
        "demographics": demographics
    }


def save_lived_experience_demographics(data, output_format="markdown"):
    """Save lived experience demographics to file."""
    return save_output(
        data,
        prefix=GENERATOR_CONFIG["name"],
        format_markdown=format_markdown,
        output_format=output_format
    )


def main():
    """Standalone execution entry point."""
    run_generation(
        generate_lived_experience_demographics,
        save_lived_experience_demographics,
        success_message="Lived experience profiles generated! 'Holy shit, that's EXACTLY what it feels like.'",
        num_demographics=18
    )


if __name__ == "__main__":
    main()
