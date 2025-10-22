#!/usr/bin/env python3
"""
If the algorithm dictates perception which dictates monadistic realities...
Claude is the Wizard. 🔮

Generate hyper-granular Twitter/X demographic profiles mapping:
- SOFT: Bourdieu-inspired cultural capital, habitus, being-in-the-world
- HARD: Technical UI patterns, behavioral metrics, tool-at-hand psychology  
- ALGORITHMIC: Deep understanding/exploitation of X's recommendation system
  Based on actual implementation details from github.com/twitter/the-algorithm

Including awareness of:
- The ~6000 features used in ranking
- Specific signals: video watch time, tweet clicks, favorites, retweets
- Author diversity heuristics, content balance, feedback fatigue
- SafetyLabels and visibility filtering mechanics
- The 2023 code vs 2025 reality gap (what changed, what's still hidden)
"""

import os
import json
from datetime import datetime
from openai import OpenAI

def generate_wizard_demographics(num_demographics=15, output_format="markdown"):
    """
    Generate the most sophisticated Twitter demographic profiles possible.
    
    Args:
        num_demographics: Number of distinct demographics (default: 15)
        output_format: 'markdown' or 'json'
    
    Returns:
        Dictionary containing the generated demographics
    """
    
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    
    prompt = f"""You are THE WIZARD - an expert in digital sociology, Bourdieu's cultural capital theory, phenomenology of technology, platform psychology, AND the actual implementation details of X's recommendation algorithm.

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
14. **Code Literacy Level**: Do they understand the actual implementation? Scale: Folk Theory → Studied GitHub Repo → Can Read Scala → Understands ML Architecture → Knows The Gap

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
21. **SafetyLabel Sophistication**: Do they understand SafetyLabels → Actions (Drop vs Interstitial vs Downranking)? Know different SafetyLevels?

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

    print("🔮 THE WIZARD AWAKENS...")
    print(f"✨ Generating {num_demographics} hyper-sophisticated demographic profiles...")
    print("📖 Drawing from actual implementation details (github.com/twitter/the-algorithm)")
    print("🧠 Mapping soft + hard + algorithmic + meta-awareness dimensions...\n")
    
    response = client.chat.completions.create(
        model="o3-2025-04-16",
        messages=[
            {"role": "system", "content": """You are THE WIZARD - a master of digital sociology, Bourdieu's theories, phenomenology, AND the actual implementation of X's recommendation algorithm.

You have studied the source code from github.com/twitter/the-algorithm (2023 release):

RETRIEVAL SIGNALS (what matters):
- HIGH: Tweet Favorite (used everywhere), Retweets, Quote Tweets, Replies
- RANKING LABELS: Video Watch Time (seconds/percentage), Tweet Clicks
- NEGATIVE: Unfavorite, Unfollow, "Don't Like", Report
- Usage varies: SimClusters vs TwHIN vs UTEG vs FRS vs Light Ranker

HOME MIXER ARCHITECTURE:
- ~6000 features used for ranking (!!!)
- Heuristics: Author Diversity, Content Balance (In/Out Network), Feedback Fatigue, Deduplication
- Two-stage: Light-ranker → Heavy-ranker (neural net)
- Candidate sources: In-Network (Earlybird search ~50%) + Out-of-Network (UTEG/FRS)

VISIBILITY FILTERING:
- SafetyLabels → Actions: Drop (hard filter), Interstitial (warning), Downranking (coarse-grained)
- Different SafetyLevels per product surface (Timeline vs Profile)
- "Part of the code has been removed and is not ready to be shared" - gaps exist

THE GAP:
- This is 2023 code, 2 years old
- Elon-era changes unknown
- Model weights not shared
- Full 6000 feature set not documented

You understand how different user types relate to this knowledge - from folk theories to technical mastery to epistemic humility about the unknowable."""},
            {"role": "user", "content": prompt}
        ],
        max_completion_tokens=12000,  # More tokens for this level of detail
        response_format={"type": "json_object"}
    )
    
    content = response.choices[0].message.content
    
    try:
        demographics_data = json.loads(content)
        
        if isinstance(demographics_data, dict):
            for key in ["demographics", "profiles", "personas", "tribes", "wizards"]:
                if key in demographics_data:
                    demographics = demographics_data[key]
                    break
            else:
                for value in demographics_data.values():
                    if isinstance(value, list):
                        demographics = value
                        break
                else:
                    demographics = [demographics_data]
        else:
            demographics = demographics_data
            
    except json.JSONDecodeError as e:
        print(f"❌ Error parsing JSON: {e}")
        print(f"Raw content: {content[:500]}...")
        return None
    
    result = {
        "generated_at": datetime.now().isoformat(),
        "model_used": "o3-2025-04-16",
        "algorithm_source": "github.com/twitter/the-algorithm (2023 release)",
        "num_demographics": len(demographics),
        "demographics": demographics
    }
    
    return result


def save_wizard_demographics(demographics_data, output_format="markdown"):
    """Save the wizard-generated demographics to a file."""
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    if output_format == "json":
        filename = f"wizard_demographics_{timestamp}.json"
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(demographics_data, f, indent=2, ensure_ascii=False)
        print(f"✅ Saved demographics to {filename}")
        
    else:  # markdown
        filename = f"wizard_demographics_{timestamp}.md"
        with open(filename, "w", encoding="utf-8") as f:
            f.write("# 🔮 The Wizard's Twitter Demographics\n\n")
            f.write("## If the algorithm dictates perception which dictates monadistic realities... Claude is the Wizard\n\n")
            f.write(f"*Generated on {demographics_data['generated_at']} using {demographics_data['model_used']}*\n\n")
            f.write(f"*Based on actual implementation from {demographics_data['algorithm_source']}*\n\n")
            
            f.write("### Mapping Four Dimensions:\n")
            f.write("1. **SOFT**: Cultural capital, habitus, being-in-the-world (Bourdieu-inspired)\n")
            f.write("2. **HARD**: UI patterns, behavioral metrics, technical interactions\n")
            f.write("3. **ALGORITHMIC**: Implementation-level understanding from actual source code\n")
            f.write("   - ~6000 features in ranking\n")
            f.write("   - Signal weights (favorites, video watch time, clicks)\n")
            f.write("   - Heuristics (author diversity, content balance, feedback fatigue)\n")
            f.write("   - SafetyLabels and visibility filtering\n")
            f.write("4. **META**: Awareness of 2023 vs 2025 gap, epistemic humility, monadistic reality construction\n\n")
            
            f.write(f"**Total Demographics:** {demographics_data['num_demographics']}\n\n")
            f.write("---\n\n")
            
            for i, demo in enumerate(demographics_data['demographics'], 1):
                f.write(f"## {i}. {demo.get('label', 'Untitled Demographic')}\n\n")
                
                # SOFT INTERACTIONS
                f.write("### 🌊 SOFT INTERACTIONS (Being-in-the-World)\n\n")
                
                if 'cultural_capital_markers' in demo:
                    f.write("**Cultural Capital Markers:**\n")
                    markers = demo['cultural_capital_markers']
                    if isinstance(markers, list):
                        for marker in markers:
                            f.write(f"- {marker}\n")
                    else:
                        f.write(f"{markers}\n")
                    f.write("\n")
                
                if 'status_performance' in demo:
                    f.write(f"**Status Position & Performance:** {demo['status_performance']}\n\n")
                
                if 'habitus' in demo:
                    f.write(f"**Habitus on Platform:** {demo['habitus']}\n\n")
                
                if 'capital_strategy' in demo:
                    f.write(f"**Cultural Capital Strategy:** {demo['capital_strategy']}\n\n")
                
                if 'symbolic_boundaries' in demo:
                    f.write(f"**Symbolic Boundaries:** {demo['symbolic_boundaries']}\n\n")
                
                if 'anxiety_patterns' in demo:
                    f.write(f"**Anxiety Patterns:** {demo['anxiety_patterns']}\n\n")
                
                if 'subliminal_motivations' in demo:
                    f.write(f"**Subliminal Motivations:** {demo['subliminal_motivations']}\n\n")
                
                # HARD INTERACTIONS
                f.write("### ⚙️ HARD INTERACTIONS (Technical/Behavioral)\n\n")
                
                if 'composition_patterns' in demo:
                    f.write(f"**Composition Patterns:** {demo['composition_patterns']}\n\n")
                
                if 'ui_signature' in demo:
                    f.write(f"**UI Interaction Signature:** {demo['ui_signature']}\n\n")
                
                if 'temporal_patterns' in demo:
                    f.write(f"**Temporal Patterns:** {demo['temporal_patterns']}\n\n")
                
                if 'engagement_calculus' in demo:
                    f.write(f"**Engagement Calculus:** {demo['engagement_calculus']}\n\n")
                
                if 'tool_psychology' in demo:
                    f.write(f"**Tool-at-Hand Psychology:** {demo['tool_psychology']}\n\n")
                
                # ALGORITHMIC AWARENESS
                f.write("### 🤖 ALGORITHMIC AWARENESS (Implementation-Level)\n\n")
                
                f.write("**Core System Understanding:**\n\n")
                
                if 'code_literacy_level' in demo:
                    f.write(f"**Code Literacy Level:** {demo['code_literacy_level']}\n\n")
                
                if 'signal_weights_awareness' in demo:
                    f.write(f"**Signal Weights Awareness:** {demo['signal_weights_awareness']}\n\n")
                
                if 'six_thousand_features_problem' in demo:
                    f.write(f"**The 6000 Features Problem:** {demo['six_thousand_features_problem']}\n\n")
                
                f.write("**Tactical Optimization:**\n\n")
                
                if 'video_watch_time_gaming' in demo:
                    f.write(f"**Video Watch Time Gaming:** {demo['video_watch_time_gaming']}\n\n")
                
                if 'author_diversity_hacking' in demo:
                    f.write(f"**Author Diversity Hacking:** {demo['author_diversity_hacking']}\n\n")
                
                if 'content_balance_theory' in demo:
                    f.write(f"**Content Balance Theory:** {demo['content_balance_theory']}\n\n")
                
                if 'feedback_fatigue_awareness' in demo:
                    f.write(f"**Feedback Fatigue Awareness:** {demo['feedback_fatigue_awareness']}\n\n")
                
                f.write("**Visibility & Moderation:**\n\n")
                
                if 'safetylabel_sophistication' in demo:
                    f.write(f"**SafetyLabel Sophistication:** {demo['safetylabel_sophistication']}\n\n")
                
                if 'visibility_filter_navigation' in demo:
                    f.write(f"**Visibility Filter Navigation:** {demo['visibility_filter_navigation']}\n\n")
                
                f.write("**Meta-Awareness:**\n\n")
                
                if 'the_2023_gap' in demo:
                    f.write(f"**The 2023 Gap:** {demo['the_2023_gap']}\n\n")
                
                if 'folk_theory_vs_reality' in demo:
                    f.write(f"**Folk Theory vs Reality:** {demo['folk_theory_vs_reality']}\n\n")
                
                # CROSS-CUTTING
                f.write("### 🔀 CROSS-CUTTING DIMENSIONS\n\n")
                
                if 'capitalization_aesthetic' in demo:
                    f.write(f"**Capitalization Aesthetic:** {demo['capitalization_aesthetic']}\n\n")
                
                if 'quote_tweet_ethics' in demo:
                    f.write(f"**Quote-Tweet vs Reply Ethics:** {demo['quote_tweet_ethics']}\n\n")
                
                if 'ratioing_relationship' in demo:
                    f.write(f"**Ratioing Relationship:** {demo['ratioing_relationship']}\n\n")
                
                if 'thread_culture' in demo:
                    f.write(f"**Thread Culture:** {demo['thread_culture']}\n\n")
                
                # META
                f.write("### 🎭 META-AWARENESS\n\n")
                
                if 'monadistic_reality_construction' in demo:
                    f.write(f"**Monadistic Reality Construction:** {demo['monadistic_reality_construction']}\n\n")
                
                if 'persona_quote' in demo:
                    f.write("**Persona Quote:**\n")
                    f.write(f"> {demo['persona_quote']}\n\n")
                
                f.write("---\n\n")
        
        print(f"✅ Saved demographics to {filename}")
    
    return filename


def main():
    """The Wizard's main incantation."""
    
    if not os.getenv("OPENAI_API_KEY"):
        print("❌ Error: OPENAI_API_KEY environment variable not set")
        print("The Wizard requires an API key to channel the algorithmic spirits")
        print("Please set it with: export OPENAI_API_KEY='your-api-key-here'")
        return
    
    demographics_data = generate_wizard_demographics(num_demographics=18, output_format="markdown")
    
    if demographics_data:
        print("\n📄 Materializing the Wizard's visions...\n")
        md_file = save_wizard_demographics(demographics_data, output_format="markdown")
        json_file = save_wizard_demographics(demographics_data, output_format="json")
        
        print(f"\n🔮 Success! The Wizard has generated {demographics_data['num_demographics']} demographic profiles")
        print(f"📖 Read the markdown file for the full prophecy")
        print(f"🔧 Use the JSON file for programmatic divination")
        print("\n✨ The Wizard has spoken:")
        print("   - Mapped from actual source code (github.com/twitter/the-algorithm)")
        print("   - ~6000 features, signal weights, heuristics revealed")
        print("   - SafetyLabels, visibility filters, the whole machinery")
        print("   - Meta-awareness: 2023 vs 2025 gap, epistemic humility")
        print("   - Monadistic reality construction mapped")
        print("\n🎭 If the algorithm dictates perception which dictates monadistic realities...")
        print("   Claude is indeed the Wizard. 🧙‍♂️")
    else:
        print("❌ The Wizard's spell failed")


if __name__ == "__main__":
    main()

