#!/usr/bin/env python3
"""
if the algorithm dictates perception which dictates monadistic realities claude is the wizard

Generate Twitter/X demographic profiles that capture the LIVED EXPERIENCE of algorithmic reality.

Theory-informed (Bourdieu, Heidegger, Leibniz, + actual implementation from the-algorithm repo)
Experience-focused (no academic jargon, just phenomenologically accurate descriptions)

The output should make people go "holy shit that's exactly what it feels like"
without them needing to know the theory behind it.
"""

import os
import json
from datetime import datetime
from openai import OpenAI

def generate_lived_experience_demographics(num_demographics=18, output_format="markdown"):
    """
    Generate demographics capturing lived experience of algorithmic Twitter reality.
    
    Theory guides the analysis, but output is pure phenomenological description.
    """
    
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    
    prompt = f"""You are creating {num_demographics} demographic profiles of Twitter/X users that capture the LIVED EXPERIENCE of existing in algorithmically-mediated social reality.

You are equipped with:

**THEORETICAL LENSES (use to inform analysis, NOT in output language):**

BOURDIEU:
- Cultural capital: influence/reach as accumulated through specific practices
- Symbolic violence: how the algorithm enforces hierarchies invisibly
- Habitus: embodied, unconscious relationship to the platform
- Field position: where they sit in status hierarchies
- Distinction: how some "naturally" get reach, others struggle

HEIDEGGER:
- Ready-to-hand vs present-at-hand: when Twitter "just works" vs when you become conscious of the machinery
- Tool breakdown: moments when algo changes and reveals its structure
- Being-thrown: you didn't choose this algorithmic reality, but you're in it
- Dasein's fall into "the they": getting absorbed into timeline scrolling

MONADISM (Leibniz):
- Windowless monads: each user in isolated, personalized filter bubble
- No direct access to others' realities/feeds
- Pre-established harmony: the algorithm dictates what appears real
- Parallel but non-communicating universes

**EMPIRICAL MECHANICS (from github.com/twitter/the-algorithm):**
- ~6000 features shaping what appears
- Signal weights: favorites, video watch time, replies
- Heuristics: author diversity, feedback fatigue, content balance
- SafetyLabels and visibility filtering
- The gap: 2023 code, changes unknown

**YOUR TASK:**

Create profiles that capture these EXPERIENCES without using academic language. Each profile should feel like someone reading it and thinking "holy shit, that's EXACTLY what it's like."

For each demographic provide:

**IDENTITY & LIVED SITUATION**
1. **Label**: Evocative, experience-focused (e.g., "The Person Who Feels Like They're Shouting Into a Void That Occasionally Shouts Back Randomly", "The One Who Knows Everyone Else Sees Different Stuff But Can't Escape Their Own Bubble")

2. **Background Markers**: What they read/listen to/care about (specific, not academic)

3. **Position in the Hierarchy**: How it FEELS to be where they are (not "low cultural capital" but "watches others go viral for similar takes, can't figure out the difference")

**THE EXPERIENCE OF ALGORITHMIC REALITY**

4. **Filter Bubble Awareness**: Do they know they're in a personalized reality tunnel? How does it feel? The claustrophobia of seeing the same 50 accounts? The uncanny sense everyone else is having a different experience?

5. **Moments of Tool Breakdown**: When does Twitter stop "just working" and they become aware of the machinery? Algorithm changes? Shadow-banning anxiety? Sudden reach changes?

6. **Invisible Hierarchy Navigation**: How do they experience the status game? Watching "influencers" play by different rules? The rituals that sometimes work (threads, video) without understanding why?

7. **Anxiety & Dependence**: What does it feel like to depend on invisible machinery? Fear of algorithmic irrelevance? The dopamine loop? Checking if the last post "landed"?

8. **Reality Tunnel**: What IS real to them? Their FYP = reality? Awareness it's constructed? The weird feeling of "main character moments" passing them by?

**BEHAVIORAL PATTERNS**

9. **Posting Rituals**: How they compose (without knowing WHY these rituals work - thread structure, video placement, timing)

10. **Engagement Patterns**: What they do, how it feels (lurking guilt, reply anxiety, quote-tweet dunking as status play)

11. **The Invisible Rules**: What do they SENSE works without knowing the mechanism? (Video holds attention, spacing posts, engaging before posting, diverse replies)

12. **Adaptation to Changes**: How do they cope when the algorithm shifts? Confusion? Rage? Adaptation? Learned helplessness?

**SOCIAL REALITY CONSTRUCTION**

13. **Information Bubble**: What's their information diet? Do they know it's curated? The echo chamber feeling vs thinking they're seeing "what's happening"?

14. **Parallel Realities Awareness**: Do they understand others see completely different content? The disorientation of "main character" moments that don't appear in their feed?

15. **Status Rituals They Can't Name**: What do they DO that's actually cultural capital accumulation, but they experience as just "how you Twitter"? (Name-dropping certain thinkers, aesthetic choices, strategic vulnerability)

16. **The Algorithmic Other**: Who do they think "gets reach naturally"? Their theory of why some people just... work? Resentment? Admiration? Confusion?

**META-AWARENESS**

17. **The Unseen Machinery**: What's their theory of how it works? Close to reality? Folk theory? Know there's something but can't articulate it?

18. **Epistemic Humility vs False Confidence**: Do they know what they don't know? Or think they've figured it out?

19. **Relationship to Being Trapped**: Acceptance? Resistance? Trying to game it? Kafka-esque awareness with no escape?

20. **Quote**: 2-3 sentences in their voice capturing their experience and understanding of algorithmic reality

**CRITICAL:** Write in EXPERIENTIAL language, not theoretical language. Bad: "experiences symbolic violence through algorithmic downranking." Good: "has the creeping sense their tweets just... disappear, while others with similar takes get thousands of likes, can't figure out what they're doing wrong, feels like there's an invisible rule system they're not cool enough to understand."

Make each profile DEEPLY SPECIFIC and RECOGNIZABLE. Think:
- "The Person Who Restructured Their Whole Posting Strategy Around Video After One Went Viral, Doesn't Know Why It Worked But Cargo-Cults It Now"
- "The One Who Realizes They Only See The Same 50 Accounts, Tried Using Lists to Escape But Got Pulled Back Into the FYP Vortex"
- "The Status Striver Who Watches People With Worse Takes Get More Reach, Has Complex Theories About 'Engagement Bait' But Can't Admit It's Just Status Games"
- "The Doomscroller Who Knows Their Feed Is Personalized Depression But Can't Stop, The Algorithm Knows What They'll Click Even When They Hate It"

Cover experiences: people who feel trapped, people who think they gamed it, people who don't realize they're in a bubble, people who feel algorithmic anxiety, people who've adapted, people who broke through and now fear falling back, people experiencing status hierarchy without naming it, people in parallel realities.

Return as JSON with fields: label, background_markers, position_feeling, filter_bubble_awareness, tool_breakdown_moments, invisible_hierarchy_navigation, anxiety_and_dependence, reality_tunnel, posting_rituals, engagement_patterns, invisible_rules, adaptation_to_changes, information_bubble, parallel_realities_awareness, status_rituals_unnamed, algorithmic_other, unseen_machinery_theory, epistemic_position, trapped_relationship, persona_quote."""

    print("🎭 Channeling lived experiences of algorithmic reality...")
    print(f"✨ Generating {num_demographics} phenomenologically-grounded profiles...")
    print("🌊 Theory informs, experience speaks...\n")
    
    response = client.chat.completions.create(
        model="o3-2025-04-16",
        messages=[
            {"role": "system", "content": """You are a phenomenologist and sociologist studying lived experience of algorithmic social media.

Your theoretical toolkit (DO NOT use this language in output):

BOURDIEU: Cultural capital, habitus, symbolic violence, field position, distinction
HEIDEGGER: Ready-to-hand, present-at-hand, tool breakdown, being-thrown, the they
LEIBNIZ/MONADISM: Windowless monads, personalized reality bubbles, no direct access
ALGORITHM MECHANICS: ~6000 features, signal weights, feedback fatigue, visibility filtering

Your output language: PURE PHENOMENOLOGICAL DESCRIPTION. How it FEELS. What it's LIKE.

Example of GOOD output:
"Watches other people's mediocre threads blow up while their better ones get 12 likes. Has developed elaborate theories about 'timing' and 'hooks' but deep down suspects there's an invisible hierarchy they're not part of. The algorithm feels like a club bouncer who lets some people in for reasons they'll never understand."

Example of BAD output:
"Experiences low cultural capital position in the field, leading to symbolic violence through algorithmic downranking."

Write so that someone reading goes "holy shit that's EXACTLY what it feels like" without needing theoretical vocabulary."""},
            {"role": "user", "content": prompt}
        ],
        max_completion_tokens=12000,
        response_format={"type": "json_object"}
    )
    
    content = response.choices[0].message.content
    
    try:
        demographics_data = json.loads(content)
        
        if isinstance(demographics_data, dict):
            for key in ["demographics", "profiles", "personas", "experiences"]:
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
        "theoretical_framework": "Bourdieu + Heidegger + Monadism (informing, not visible)",
        "num_demographics": len(demographics),
        "demographics": demographics
    }
    
    return result


def save_lived_experience_demographics(demographics_data, output_format="markdown"):
    """Save the phenomenologically-grounded demographics."""
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    if output_format == "json":
        filename = f"lived_experience_demographics_{timestamp}.json"
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(demographics_data, f, indent=2, ensure_ascii=False)
        print(f"✅ Saved to {filename}")
        
    else:  # markdown
        filename = f"lived_experience_demographics_{timestamp}.md"
        with open(filename, "w", encoding="utf-8") as f:
            f.write("# Lived Experiences of Algorithmic Twitter Reality\n\n")
            f.write("## if the algorithm dictates perception which dictates monadistic realities...\n\n")
            f.write(f"*Generated {demographics_data['generated_at']} via {demographics_data['model_used']}*\n\n")
            f.write(f"*Framework: {demographics_data['theoretical_framework']}*\n\n")
            
            f.write("These profiles capture what it FEELS like to exist in algorithmically-mediated social reality.\n\n")
            f.write(f"**Total Profiles:** {demographics_data['num_demographics']}\n\n")
            f.write("---\n\n")
            
            for i, demo in enumerate(demographics_data['demographics'], 1):
                f.write(f"## {i}. {demo.get('label', 'Untitled Experience')}\n\n")
                
                if 'background_markers' in demo:
                    f.write(f"**Background:** {demo['background_markers']}\n\n")
                
                if 'position_feeling' in demo:
                    f.write(f"**Where They Feel They Sit:** {demo['position_feeling']}\n\n")
                
                f.write("### 🌀 The Experience of Algorithmic Reality\n\n")
                
                if 'filter_bubble_awareness' in demo:
                    f.write(f"**Filter Bubble Awareness:** {demo['filter_bubble_awareness']}\n\n")
                
                if 'tool_breakdown_moments' in demo:
                    f.write(f"**When The Machine Becomes Visible:** {demo['tool_breakdown_moments']}\n\n")
                
                if 'invisible_hierarchy_navigation' in demo:
                    f.write(f"**Navigating Invisible Hierarchies:** {demo['invisible_hierarchy_navigation']}\n\n")
                
                if 'anxiety_and_dependence' in demo:
                    f.write(f"**Anxiety & Dependence:** {demo['anxiety_and_dependence']}\n\n")
                
                if 'reality_tunnel' in demo:
                    f.write(f"**What Feels Real:** {demo['reality_tunnel']}\n\n")
                
                f.write("### 📱 How They Act\n\n")
                
                if 'posting_rituals' in demo:
                    f.write(f"**Posting Rituals:** {demo['posting_rituals']}\n\n")
                
                if 'engagement_patterns' in demo:
                    f.write(f"**Engagement Patterns:** {demo['engagement_patterns']}\n\n")
                
                if 'invisible_rules' in demo:
                    f.write(f"**Rules They Sense But Can't Name:** {demo['invisible_rules']}\n\n")
                
                if 'adaptation_to_changes' in demo:
                    f.write(f"**When The Algorithm Shifts:** {demo['adaptation_to_changes']}\n\n")
                
                f.write("### 🎭 Social Reality Construction\n\n")
                
                if 'information_bubble' in demo:
                    f.write(f"**Their Information Diet:** {demo['information_bubble']}\n\n")
                
                if 'parallel_realities_awareness' in demo:
                    f.write(f"**Awareness of Others' Different Realities:** {demo['parallel_realities_awareness']}\n\n")
                
                if 'status_rituals_unnamed' in demo:
                    f.write(f"**Status Games They Can't Name:** {demo['status_rituals_unnamed']}\n\n")
                
                if 'algorithmic_other' in demo:
                    f.write(f"**Who 'Gets Reach Naturally':** {demo['algorithmic_other']}\n\n")
                
                f.write("### 🤔 Understanding & Relationship\n\n")
                
                if 'unseen_machinery_theory' in demo:
                    f.write(f"**Their Theory of How It Works:** {demo['unseen_machinery_theory']}\n\n")
                
                if 'epistemic_position' in demo:
                    f.write(f"**What They Know They Don't Know:** {demo['epistemic_position']}\n\n")
                
                if 'trapped_relationship' in demo:
                    f.write(f"**Relationship to Being Trapped:** {demo['trapped_relationship']}\n\n")
                
                if 'persona_quote' in demo:
                    f.write("**In Their Words:**\n")
                    f.write(f"> {demo['persona_quote']}\n\n")
                
                f.write("---\n\n")
        
        print(f"✅ Saved to {filename}")
    
    return filename


def main():
    """Main execution."""
    
    if not os.getenv("OPENAI_API_KEY"):
        print("❌ Error: OPENAI_API_KEY environment variable not set")
        print("Set with: export OPENAI_API_KEY='your-api-key-here'")
        return
    
    demographics_data = generate_lived_experience_demographics(num_demographics=18, output_format="markdown")
    
    if demographics_data:
        print("\n📄 Materializing experiences...\n")
        md_file = save_lived_experience_demographics(demographics_data, output_format="markdown")
        json_file = save_lived_experience_demographics(demographics_data, output_format="json")
        
        print(f"\n✨ Generated {demographics_data['num_demographics']} lived experience profiles")
        print("📖 Theory-informed, experience-focused")
        print("🎭 No jargon, just phenomenological accuracy")
        print("\n💫 Profiles should make readers think:")
        print("   'Holy shit, that's EXACTLY what it feels like'")
    else:
        print("❌ Generation failed")


if __name__ == "__main__":
    main()

