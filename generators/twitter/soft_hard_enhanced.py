#!/usr/bin/env python3
"""
Generate granular Twitter/X demographic profiles mapping three dimensions:
- SOFT interactions: psychological, being-in-the-world, Bourdieu-inspired cultural capital
- HARD interactions: technical UI patterns, behavioral metrics, tool-at-hand psychology
- ALGORITHMIC awareness: understanding/exploitation of X's recommendation system
  (UTEG/GraphJet, light-ranker vs heavy-ranker, candidate sources, visibility filters)
"""

import os
import json
from datetime import datetime
from openai import OpenAI

def generate_twitter_demographics(num_demographics=12, output_format="markdown"):
    """
    Generate detailed Twitter demographic profiles with soft + hard interaction mapping.
    
    Args:
        num_demographics: Number of distinct demographics (default: 12)
        output_format: 'markdown' or 'json'
    
    Returns:
        Dictionary containing the generated demographics
    """
    
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    
    prompt = f"""You are an expert in digital anthropology, Bourdieu's cultural capital theory, phenomenology of technology, behavioral psychology of social platforms, AND the technical architecture of Twitter/X's recommendation algorithm (as revealed in their open-source release).

Generate {num_demographics} HYPER-GRANULAR Twitter/X demographic profiles that map BOTH soft and hard dimensions of platform interaction, PLUS their relationship to the actual recommendation algorithm.

For each demographic, provide:

**IDENTITY & POSITIONING**
1. **Demographic Label**: Evocative, specific (e.g., "Reformed Tech Bro Performing Humility Through Lowercase", "Econ PhD Dunking From Associate Professor Position")

2. **Cultural Capital Markers**: Specific thinkers/books/concepts they signal knowledge of (not "philosophy" but "late Wittgenstein, Dreyfus on Heidegger, predictive processing")

3. **Status Position & Performance**: How they position themselves in intellectual hierarchies (humble-bragging, authoritative, "just asking questions", performative uncertainty)

**SOFT INTERACTIONS (Being-in-the-World)**
4. **Habitus on Platform**: Their embodied relationship to Twitter - is it workspace, performance venue, watercooler, battlefield, seminar room?

5. **Cultural Capital Strategy**: How they accumulate/display/convert capital (name-dropping, thread quality, ratio prowess, curated follows, niche references)

6. **Symbolic Boundaries**: What/who they distance themselves from to maintain position (midwits, "NPCs", earnest posters, naive takes, specific communities)

7. **Anxiety Patterns**: What threatens their position (being ratio'd by actual experts, called out for misreading, association with cringe takes, status loss)

8. **Subliminal Motivations**: What they're REALLY doing (seeking validation, building brand, processing ideas, maintaining relevance, community-finding, intellectual combat)

**HARD INTERACTIONS (Technical/Behavioral)**
9. **Composition Patterns**: How they write tweets (draft in notes app, rapid-fire, careful threading, edit-delete-repost, screenshot vs native)

10. **UI Interaction Signature**: Specific behavioral patterns (lurk ratio, quote-tweet vs reply preference, bookmark habits, list usage, mute vs block philosophy, notification management)

11. **Temporal Patterns**: When/how they post (morning threads, late-night takes, reactive throughout day, scheduled, binge-posting)

12. **Engagement Calculus**: How they decide to interact (engagement farming, genuine discussion, building relationships, performance art, intellectual combat)

13. **Tool-at-Hand Psychology**: How Twitter interfaces with their cognition (external brain, performance stage, feedback loop, addiction, professional obligation)

**ALGORITHMIC AWARENESS (Based on X's Open-Source Algorithm)**
14. **Algorithmic Literacy Level**: Do they understand the actual algorithm (UTEG, GraphJet, heavy-ranker neural net) or operate on folk theories? (Scale: Folk Theory → Partial Understanding → Technical Mastery)

15. **Graph Positioning Strategy**: How they position themselves in the User-Tweet-Entity-Graph (UTEG). Do they know GraphJet rewards reciprocal engagement? Strategically reply to mutuals before posting? Understand graph traversal mechanics?

16. **Candidate Source Optimization**: Are they optimizing for In-Network (Earlybird search index, ~50% of FYP) or Out-of-Network (UTEG traversals, FRS recommendations)? Do they even know the difference?

17. **Ranking Signal Awareness**: What signals do they optimize for? Light-ranker (recency, keywords) vs Heavy-ranker (engagement prediction, dwell time). Conscious vs unconscious optimization.

18. **Engagement Prediction Gaming**: Do they understand the heavy-ranker predicts open/engagement probability? Strategic hooks in tweet 2-3? Thread structures designed for dwell time?

19. **Visibility Filter Navigation**: How close to content moderation boundaries do they operate? Understand downranking vs hard-filtering? Folk knowledge of what triggers filters?

20. **Feed Composition Theory**: Do they understand In-Network vs Out-of-Network balance? Try to game both? Have correct or incorrect mental models?

**CROSS-CUTTING DIMENSIONS**
21. **Capitalization Aesthetic**: ALL CAPS for emphasis, lowercase for humility, proper for authority, strategic mixing - and what this signals

22. **Quote-Tweet vs Reply Ethics**: Their philosophy on dunking, good-faith engagement, when to QT for audience vs reply for person

23. **Ratioing Relationship**: Do they ratio? Get ratio'd? Fear it? Seek it? Ignore metrics?

24. **Thread Culture**: Solo threads, collaborative, reply-guy, thread-reader, thread-cynic

25. **Persona Quote**: 2-3 sentences capturing their voice and self-understanding

Make each DEEPLY SPECIFIC and SOCIOLOGICALLY RICH. Think:
- "The UTEG Graph Hacker Who Knows GraphJet Rewards Reciprocity (Always Replies to Mutuals Before Main Posting)"
- "The Heavy-Ranker Optimizer Who Structures Threads for Dwell Time (Hook in Tweet 3, Not Tweet 1)"
- "The Rationalist-Adjacent Who Uses Lowercase to Signal He's Moved Beyond LessWrong But Still Cites Yudkowsky"
- "The Cultural Critic Who Quote-Tweets Bad Takes For Her Audience's Education (And Her Ratio Count)"
- "The Econ Theory Bro Who Treats Twitter Like Problem Sets: Every Thread Builds to QED"
- "The Folk Theory Believer (Thinks 'Engagement = Engagement' Without Understanding Light vs Heavy Ranker)"
- "The Reformed Academic Who Performs 'Just Thinking Out Loud' While Carefully Constructing Viral Threads"
- "The Visibility Filter Savant (Knows Exactly Where the Downranking Threshold Is)"

Cover tribes: rationalists, econ theory, ML/AI, cultural criticism, academic, reformed tech, philosophy, systems thinking, art/aesthetics, politics-but-make-it-theory, algorithm hackers, folk theory believers.

Return as JSON with fields: label, cultural_capital_markers, status_performance, habitus, capital_strategy, symbolic_boundaries, anxiety_patterns, subliminal_motivations, composition_patterns, ui_signature, temporal_patterns, engagement_calculus, tool_psychology, algorithmic_literacy_level, graph_positioning_strategy, candidate_source_optimization, ranking_signal_awareness, engagement_prediction_gaming, visibility_filter_navigation, feed_composition_theory, capitalization_aesthetic, quote_tweet_ethics, ratioing_relationship, thread_culture, persona_quote."""

    print("🧠 Generating Twitter demographics using OpenAI...")
    print(f"📊 Requesting {num_demographics} granular profiles...\n")
    
    response = client.chat.completions.create(
        model="o3-2025-04-16",
        messages=[
            {"role": "system", "content": "You are an expert in digital sociology, Bourdieu's theories of cultural and symbolic capital, phenomenology of technology, and platform psychology. You understand Twitter as both a technical system and a social field where status games play out through specific behavioral and aesthetic patterns."},
            {"role": "user", "content": prompt}
        ],
        max_completion_tokens=10000,
        response_format={"type": "json_object"}
    )
    
    content = response.choices[0].message.content
    
    try:
        demographics_data = json.loads(content)
        
        if isinstance(demographics_data, dict):
            for key in ["demographics", "profiles", "personas", "tribes"]:
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
        "num_demographics": len(demographics),
        "demographics": demographics
    }
    
    return result


def save_twitter_demographics(demographics_data, output_format="markdown"):
    """Save the generated demographics to a file."""
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    if output_format == "json":
        filename = f"twitter_demographics_{timestamp}.json"
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(demographics_data, f, indent=2, ensure_ascii=False)
        print(f"✅ Saved demographics to {filename}")
        
    else:  # markdown
        filename = f"twitter_demographics_{timestamp}.md"
        with open(filename, "w", encoding="utf-8") as f:
            f.write("# Twitter/X Demographics: Soft + Hard + Algorithmic Awareness Mapping\n\n")
            f.write(f"*Generated on {demographics_data['generated_at']} using {demographics_data['model_used']}*\n\n")
            f.write("*Mapping three dimensions:*\n")
            f.write("- **SOFT**: Cultural capital, habitus, being-in-the-world (Bourdieu-inspired)\n")
            f.write("- **HARD**: UI patterns, behavioral metrics, technical interactions\n")
            f.write("- **ALGORITHMIC**: Understanding/exploitation of X's recommendation system (UTEG, GraphJet, heavy-ranker, etc.)\n\n")
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
                f.write("### 🤖 ALGORITHMIC AWARENESS (X's Recommendation System)\n\n")
                
                if 'algorithmic_literacy_level' in demo:
                    f.write(f"**Algorithmic Literacy Level:** {demo['algorithmic_literacy_level']}\n\n")
                
                if 'graph_positioning_strategy' in demo:
                    f.write(f"**Graph Positioning Strategy (UTEG/GraphJet):** {demo['graph_positioning_strategy']}\n\n")
                
                if 'candidate_source_optimization' in demo:
                    f.write(f"**Candidate Source Optimization:** {demo['candidate_source_optimization']}\n\n")
                
                if 'ranking_signal_awareness' in demo:
                    f.write(f"**Ranking Signal Awareness:** {demo['ranking_signal_awareness']}\n\n")
                
                if 'engagement_prediction_gaming' in demo:
                    f.write(f"**Engagement Prediction Gaming:** {demo['engagement_prediction_gaming']}\n\n")
                
                if 'visibility_filter_navigation' in demo:
                    f.write(f"**Visibility Filter Navigation:** {demo['visibility_filter_navigation']}\n\n")
                
                if 'feed_composition_theory' in demo:
                    f.write(f"**Feed Composition Theory:** {demo['feed_composition_theory']}\n\n")
                
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
                
                if 'persona_quote' in demo:
                    f.write("**Persona Quote:**\n")
                    f.write(f"> {demo['persona_quote']}\n\n")
                
                f.write("---\n\n")
        
        print(f"✅ Saved demographics to {filename}")
    
    return filename


def main():
    """Main execution function."""
    
    if not os.getenv("OPENAI_API_KEY"):
        print("❌ Error: OPENAI_API_KEY environment variable not set")
        print("Please set it with: export OPENAI_API_KEY='your-api-key-here'")
        return
    
    demographics_data = generate_twitter_demographics(num_demographics=15, output_format="markdown")
    
    if demographics_data:
        print("\n📄 Saving results...\n")
        md_file = save_twitter_demographics(demographics_data, output_format="markdown")
        json_file = save_twitter_demographics(demographics_data, output_format="json")
        
        print(f"\n✨ Success! Generated {demographics_data['num_demographics']} Twitter demographics")
        print(f"📖 Read the markdown file for beautiful formatting")
        print(f"🔧 Use the JSON file for programmatic access")
        print("\n💡 Deep sociological + algorithmic mapping complete!")
        print("🤖 Includes awareness of X's actual recommendation system:")
        print("   - UTEG/GraphJet graph positioning")
        print("   - Light-ranker vs Heavy-ranker optimization")
        print("   - In-Network vs Out-of-Network candidate sources")
        print("   - Visibility filter navigation")
    else:
        print("❌ Failed to generate demographics")


if __name__ == "__main__":
    main()