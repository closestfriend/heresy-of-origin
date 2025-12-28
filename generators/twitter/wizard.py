#!/usr/bin/env python3
"""
The Wizard Generator - Implementation-level Twitter/X demographic profiles.

If the algorithm dictates perception which dictates monadistic realities...
Claude is the Wizard.

This monad generates hyper-granular demographic profiles mapping:
- SOFT: Bourdieu-inspired cultural capital, habitus, being-in-the-world
- HARD: Technical UI patterns, behavioral metrics, tool-at-hand psychology
- ALGORITHMIC: Deep understanding of X's recommendation system
  Based on actual implementation from github.com/twitter/the-algorithm

Including awareness of:
- The ~6000 features used in ranking
- Specific signals: video watch time, tweet clicks, favorites, retweets
- Author diversity heuristics, content balance, feedback fatigue
- SafetyLabels and visibility filtering mechanics
- The 2023 code vs 2025 reality gap (what changed, what's still hidden)
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
    "name": "wizard_demographics",
    "item_keys": ["demographics", "profiles", "personas", "tribes", "wizards"],
    "max_tokens": 12000,
    "temperature": 0.7,
}

SYSTEM_PROMPT = """You are THE WIZARD - a master of digital sociology, Bourdieu's theories, phenomenology, AND the actual implementation of X's recommendation algorithm. Always respond with valid JSON.

You have studied the source code from github.com/twitter/the-algorithm (2023 release):

RETRIEVAL SIGNALS (what matters):
- HIGH: Tweet Favorite (used everywhere), Retweets, Quote Tweets, Replies
- RANKING LABELS: Video Watch Time (seconds/percentage), Tweet Clicks
- NEGATIVE: Unfavorite, Unfollow, "Don't Like", Report
- Usage varies: SimClusters vs TwHIN vs UTEG vs FRS vs Light Ranker

HOME MIXER ARCHITECTURE:
- ~6000 features used for ranking (!!!)
- Heuristics: Author Diversity, Content Balance (In/Out Network), Feedback Fatigue, Deduplication
- Two-stage: Light-ranker -> Heavy-ranker (neural net)
- Candidate sources: In-Network (Earlybird search ~50%) + Out-of-Network (UTEG/FRS)

VISIBILITY FILTERING:
- SafetyLabels -> Actions: Drop (hard filter), Interstitial (warning), Downranking (coarse-grained)
- Different SafetyLevels per product surface (Timeline vs Profile)
- "Part of the code has been removed and is not ready to be shared" - gaps exist

THE GAP:
- This is 2023 code, 2 years old
- Elon-era changes unknown
- Model weights not shared
- Full 6000 feature set not documented

You understand how different user types relate to this knowledge - from folk theories to technical mastery to epistemic humility about the unknowable."""


def build_prompt(num_demographics: int) -> str:
    """Build the comprehensive wizard demographics prompt."""
    return f"""You are THE WIZARD - an expert in digital sociology, Bourdieu's cultural capital theory, phenomenology of technology, platform psychology, AND the actual implementation details of X's recommendation algorithm.

You have studied the actual source code from github.com/twitter/the-algorithm (released 2023), including:
- RETRIEVAL_SIGNALS.md showing which user actions matter and how (favorites, retweets, video watch, clicks, unfollows, etc.)
- home-mixer showing the ~6000 features used for ranking
- Specific heuristics: Author Diversity, Content Balance (In-Network vs Out-of-Network), Feedback Fatigue, Deduplication
- Visibility filtering with SafetyLabels, Actions (Drop, Interstitial, Downranking), different SafetyLevels per product surface

You also understand the epistemological gap: this is 2023 code, 2 years old, parts were removed/sanitized, Elon-era changes unknown.

Generate {num_demographics} HYPER-SOPHISTICATED Twitter/X demographic profiles mapping three dimensions plus meta-awareness.

For each demographic, provide:

**IDENTITY & POSITIONING**
1. **Demographic Label**: Evocative, technically specific (e.g., "The GitHub Code Reader Who Optimizes for Deprecated Weights", "The 6000 Features Realist Who Knows They Only Understand 50")

2. **Cultural Capital Markers**: Specific thinkers/books/concepts they signal (not "philosophy" but "late Wittgenstein, Dreyfus on Heidegger, predictive processing")

3. **Status Position & Performance**: How they position themselves intellectually (humble-bragging, authoritative, "just asking questions", performative uncertainty)

**SOFT INTERACTIONS (Being-in-the-World)**
4. **Habitus on Platform**: Their embodied relationship to Twitter (workspace, performance venue, watercooler, battlefield, seminar room, psychic prison)

5. **Cultural Capital Strategy**: How they accumulate/display/convert capital (name-dropping, thread quality, ratio prowess, curated follows, niche references)

6. **Symbolic Boundaries**: What/who they distance themselves from (midwits, "NPCs", earnest posters, naive takes, specific communities, "code readers who think they got it")

7. **Anxiety Patterns**: What threatens their position (being ratio'd by experts, called out for misreading code, association with cringe takes, algorithmic irrelevance)

8. **Subliminal Motivations**: What they're REALLY doing (validation seeking, brand building, idea processing, relevance maintenance, intellectual combat, escaping monadistic reality)

**HARD INTERACTIONS (Technical/Behavioral)**
9. **Composition Patterns**: How they write (draft in notes app, rapid-fire, threading, edit-delete-repost, screenshot vs native)

10. **UI Interaction Signature**: Behavioral patterns (lurk ratio, QT vs reply preference, bookmark habits, list usage, mute vs block philosophy, notification management)

11. **Temporal Patterns**: When/how they post (morning threads, late-night takes, reactive throughout day, scheduled, binge-posting, timezone gaming)

12. **Engagement Calculus**: How they decide to interact (engagement farming, genuine discussion, relationship building, performance art, intellectual combat)

13. **Tool-at-Hand Psychology**: How Twitter interfaces with cognition (external brain, performance stage, dopamine feedback loop, addiction, professional obligation, reality construction)

**ALGORITHMIC AWARENESS (Implementation-Level)**

**Core System Understanding:**
14. **Code Literacy Level**: Do they understand the actual implementation? Scale: Folk Theory -> Studied GitHub Repo -> Can Read Scala -> Understands ML Architecture -> Knows The Gap

15. **Signal Weights Awareness**: Do they know which signals actually matter from RETRIEVAL_SIGNALS.md?
    - HIGH VALUE: Favorites (used everywhere), Retweets, Quote Tweets, Replies, Video Watch Time, Tweet Clicks
    - NEGATIVE: Unfavorite, Unfollow, "Don't Like", Report
    - UNDERRATED: Video watch time as ranking signal, Tweet clicks as label

16. **The 6000 Features Problem**: Do they understand ranking uses ~6000 features? Their mental model (thinking it's 5 signals vs knowing it's 6000 they can't all optimize for)

**Tactical Optimization:**
17. **Video Watch Time Gaming**: Do they know video watch seconds/percentage is a direct ranking signal? Strategic video usage?

18. **Author Diversity Hacking**: Do they understand the author diversity heuristic? Spacing posts, engaging with diverse accounts first?

19. **Content Balance Theory**: Do they understand In-Network vs Out-of-Network ratio balancing? Trying to appear in both candidate sources?

20. **Feedback Fatigue Awareness**: Do they know repeated exposure without engagement = downranking? Strategic post spacing?

**Visibility & Moderation:**
21. **SafetyLabel Sophistication**: Do they understand SafetyLabels -> Actions (Drop vs Interstitial vs Downranking)? Know different SafetyLevels?

22. **Visibility Filter Navigation**: How close to boundaries do they operate? Understanding of "coarse-grained downranking" vs hard-filtering?

**Meta-Awareness:**
23. **The 2023 Gap**: Do they understand this code is 2 years old, parts removed, Elon-era changes unknown? Epistemic humility vs false confidence?

24. **Folk Theory vs Reality**: What do they THINK they know vs what's actually in the code? Common misconceptions?

**CROSS-CUTTING DIMENSIONS**
25. **Capitalization Aesthetic**: ALL CAPS for emphasis, lowercase for humility, proper for authority - and what this signals to both humans AND potentially to NLP features

26. **Quote-Tweet vs Reply Ethics**: Their philosophy on dunking, good-faith engagement, when to QT for audience vs reply for person

27. **Ratioing Relationship**: Do they ratio? Get ratio'd? Fear it? Seek it? Understand engagement signals?

28. **Thread Culture**: Solo threads, collaborative, reply-guy, thread-reader, thread-optimizer (understanding dwell time)

29. **Monadistic Reality Construction**: How does their algorithmic positioning shape their perceived reality? Are they aware they're in a personalized information bubble?

30. **Persona Quote**: 2-3 sentences capturing their voice, self-understanding, and relationship to algorithmic reality

Make each DEEPLY SPECIFIC and MULTI-LAYERED. Think:
- "The Video Watch Time Optimizer Who Structures Threads with Strategic Video Hooks in Tweet 3 (Read the 2023 Code, Doesn't Know If Weights Changed)"
- "The SafetyLabel Cartographer (Knows Drop vs Downrank, Maps Boundaries, Understands Different SafetyLevels for Timeline vs Profile)"
- "The 6000 Features Zen Master (Accepted You Can't Optimize for All, Focuses on Video + Favorites + Author Diversity, Epistemic Humility About The Rest)"
- "The Folk Theory Believer (Thinks Bookmarks > Likes Because They Read It Somewhere, Never Actually Looked at RETRIEVAL_SIGNALS.md)"
- "The GitHub Code Reader With False Confidence (Read 2023 Repo, Optimizes for Old Weights, Doesn't Realize Feedback Fatigue Changed)"
- "The Post-Algorithmic Philosopher (Understands They're Trapped in Monadistic Reality, Tries to Game It Anyway, Kafka-esque Awareness)"

Cover tribes: rationalists, econ theory, ML/AI, cultural criticism, academic, reformed tech, philosophy, systems thinking, algorithm hackers, code readers, folk theorists, post-algorithmic philosophers.

Return as JSON with fields: label, cultural_capital_markers, status_performance, habitus, capital_strategy, symbolic_boundaries, anxiety_patterns, subliminal_motivations, composition_patterns, ui_signature, temporal_patterns, engagement_calculus, tool_psychology, code_literacy_level, signal_weights_awareness, six_thousand_features_problem, video_watch_time_gaming, author_diversity_hacking, content_balance_theory, feedback_fatigue_awareness, safetylabel_sophistication, visibility_filter_navigation, the_2023_gap, folk_theory_vs_reality, capitalization_aesthetic, quote_tweet_ethics, ratioing_relationship, thread_culture, monadistic_reality_construction, persona_quote."""


# ============ MARKDOWN FORMATTER ============

def format_markdown(data: dict, f) -> None:
    """Format wizard demographics as markdown - the unique output form of this monad."""
    f.write("# The Wizard's Twitter Demographics\n\n")
    f.write("## If the algorithm dictates perception which dictates monadistic realities... Claude is the Wizard\n\n")
    f.write(f"*Generated on {data['generated_at']} using {data['model_used']}*\n\n")
    f.write(f"*Based on actual implementation from {data['algorithm_source']}*\n\n")

    f.write("### Mapping Four Dimensions:\n")
    f.write("1. **SOFT**: Cultural capital, habitus, being-in-the-world (Bourdieu-inspired)\n")
    f.write("2. **HARD**: UI patterns, behavioral metrics, technical interactions\n")
    f.write("3. **ALGORITHMIC**: Implementation-level understanding from actual source code\n")
    f.write("   - ~6000 features in ranking\n")
    f.write("   - Signal weights (favorites, video watch time, clicks)\n")
    f.write("   - Heuristics (author diversity, content balance, feedback fatigue)\n")
    f.write("   - SafetyLabels and visibility filtering\n")
    f.write("4. **META**: Awareness of 2023 vs 2025 gap, epistemic humility, monadistic reality construction\n\n")

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
        f.write("### ALGORITHMIC AWARENESS (Implementation-Level)\n\n")
        f.write("**Core System Understanding:**\n\n")

        for field, label in [
            ('code_literacy_level', 'Code Literacy Level'),
            ('signal_weights_awareness', 'Signal Weights Awareness'),
            ('six_thousand_features_problem', 'The 6000 Features Problem'),
        ]:
            if field in demo:
                f.write(f"**{label}:** {demo[field]}\n\n")

        f.write("**Tactical Optimization:**\n\n")

        for field, label in [
            ('video_watch_time_gaming', 'Video Watch Time Gaming'),
            ('author_diversity_hacking', 'Author Diversity Hacking'),
            ('content_balance_theory', 'Content Balance Theory'),
            ('feedback_fatigue_awareness', 'Feedback Fatigue Awareness'),
        ]:
            if field in demo:
                f.write(f"**{label}:** {demo[field]}\n\n")

        f.write("**Visibility & Moderation:**\n\n")

        for field, label in [
            ('safetylabel_sophistication', 'SafetyLabel Sophistication'),
            ('visibility_filter_navigation', 'Visibility Filter Navigation'),
        ]:
            if field in demo:
                f.write(f"**{label}:** {demo[field]}\n\n")

        f.write("**Meta-Awareness:**\n\n")

        for field, label in [
            ('the_2023_gap', 'The 2023 Gap'),
            ('folk_theory_vs_reality', 'Folk Theory vs Reality'),
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

        # META
        f.write("### META-AWARENESS\n\n")

        if 'monadistic_reality_construction' in demo:
            f.write(f"**Monadistic Reality Construction:** {demo['monadistic_reality_construction']}\n\n")

        if 'persona_quote' in demo:
            f.write("**Persona Quote:**\n")
            f.write(f"> {demo['persona_quote']}\n\n")

        f.write("---\n\n")


# ============ CORE FUNCTIONS ============

def generate_wizard_demographics(num_demographics=15, output_format="markdown", model=None):
    """
    Generate the most sophisticated Twitter demographic profiles possible.

    Args:
        num_demographics: Number of distinct demographics
        output_format: 'markdown' or 'json'
        model: LLM model to use

    Returns:
        Dictionary containing the generated demographics, or None on failure
    """
    client = get_llm_client()
    model = model or get_default_model()

    print(f"Starting generation: {num_demographics} wizard demographics (model: {model})")

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
        "algorithm_source": "github.com/twitter/the-algorithm (2023 release)",
        "num_demographics": len(demographics),
        "demographics": demographics
    }


def save_wizard_demographics(data, output_format="markdown"):
    """Save wizard demographics to file."""
    return save_output(
        data,
        prefix=GENERATOR_CONFIG["name"],
        format_markdown=format_markdown,
        output_format=output_format
    )


def main():
    """The Wizard's standalone execution entry point."""
    run_generation(
        generate_wizard_demographics,
        save_wizard_demographics,
        success_message="The Wizard has spoken! Monadistic realities mapped.",
        num_demographics=18
    )


if __name__ == "__main__":
    main()
