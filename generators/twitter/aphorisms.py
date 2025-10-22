#!/usr/bin/env python3
"""
Generate hard-hitting aphorisms/takes/tweets for intellectual Twitter.
Maximizes engagement through deliberate syntax, capitalization, and precision
while maintaining intellectual rigor. Maps each take to its target micro-demographic.
"""

import os
import json
from datetime import datetime
from openai import OpenAI

def generate_aphorisms(num_aphorisms=20, output_format="markdown"):
    """
    Generate intellectually rigorous, engagement-optimized aphorisms/tweets.
    
    Args:
        num_aphorisms: Number of distinct takes to generate (default: 20)
        output_format: 'markdown' or 'json' (default: markdown)
    
    Returns:
        Dictionary containing the generated aphorisms
    """
    
    # Initialize OpenAI client
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    
    prompt = f"""You are a master of intellectual Twitter discourse with deep knowledge of:
- Cultural criticism (Paglia, Hitchens, CEBK CEBK-style comparative analysis)
- Economic theory (mechanism design, auction theory, Schumpeterian frameworks)
- Tech/AI discourse (Ribbonfarm, rationalist-adjacent, ML theory)
- Philosophy (game theory, epistemology, phenomenology)
- Systems thinking and interdisciplinary synthesis

Generate {num_aphorisms} HARD-HITTING aphorisms/takes/tweets that maximize engagement while maintaining intellectual rigor.

CAPITALIZATION STRATEGIES - vary these strategically:
1. **Strategic CAPS for emphasis**: "one theorem ALONE is what paid for google"
2. **All lowercase for thoughtful/humble affect**: "actually think the sortition people might be onto something here"
3. **Proper case for authoritative takes**: "The liquidity of discipline isn't discipline."
4. **Mixed case for thread-style reflection**: "been thinking about this... the REAL question isn't alignment but what selects FOR alignment"

Each aphorism should:

1. **The Take** (280 chars max): The actual tweet/aphorism with STRATEGIC capitalization choice. Examples:

CAPS EMPHASIS STYLE:
"one theorem ALONE is what paid for google—mechanism design isn't abstract math, it's the architecture of value extraction"

LOWERCASE HUMBLE STYLE:
"actually the most interesting thing about llms isn't the scale, it's that they're compression artifacts of human knowledge distribution and nobody wants to admit what that implies"

PROPER AUTHORITATIVE STYLE:
"The problem with 'AI safety' discourse is that it assumes alignment is a property of models rather than a relationship between systems and their selection environments."

MIXED REFLECTIVE STYLE:
"been reading Varian again and... the revelation principle basically says you can't hide information asymmetries, only decide who pays for them. which means every 'privacy' debate is actually a pricing debate"

2. **Capitalization Strategy**: Which style and WHY (lowercase = humility/coolness, CAPS = emphasis/energy, proper = authority, mixed = thinking-out-loud)

3. **Intellectual Scaffolding**: The 2-3 specific concepts/thinkers/frameworks this riffs on (be specific: "Varian's revelation principle" not just "economics")

4. **Why It Hits**: The engagement mechanism (counter-intuitive, status-reframe, connects disparate fields, challenges assumption, name-drops niche thinker, cultural comparison)

5. **Target Demographic**: Which SPECIFIC micro-community this lands with (use hyper-specific labels like "rationalist-adjacent indie game devs" or "burned out econ PhDs who read Ribbonfarm")

6. **Thread Potential** (optional): If this could expand into a 3-5 tweet thread, brief outline

7. **Formatting Notes**: Specific notes on punctuation rhythm, where the "punch" lands, em-dash placement

8. **Intellectual Rigor Score**: 1-10 on domain knowledge required

9. **Engagement Vectors**: Which triggers (dunking, explaining, cultural analysis, provocation, synthesis, "actually..." correction, humble-brag expertise)

10. **Aesthetic Tribe**: Which Twitter aesthetic/cultural tribe this belongs to (rationalist, econ theory bro, philosophy poster, reformed tech bro, academic shitposter, etc.)

Make them GENUINELY SMART but Twitter-optimized. Mix capitalization strategies - don't just do one style. Think:
- CEBK CEBK's comparative civilizational analysis (mixed case)
- lowercase affect for "just thinking out loud" that's actually a dunk
- CAPS for EMPHASIS on technical terms
- Proper case for authoritative correctives
- Strategic em-dashes for rhythm
- Name-dropping that LANDS

Cover domains: econ, AI/ML, cultural criticism, philosophy, systems thinking, tech, institutional design, epistemology.

Return as JSON array with fields: take, capitalization_strategy, intellectual_scaffolding, why_it_hits, target_demographic, thread_potential, formatting_notes, rigor_score, engagement_vectors, aesthetic_tribe."""

    print("🔥 Generating aphorisms using OpenAI...")
    print(f"💬 Requesting {num_aphorisms} hard-hitting takes...\n")
    
    # Call OpenAI API
    response = client.chat.completions.create(
        model="o3-2025-04-16",
        messages=[
            {"role": "system", "content": "You are a master of intellectual discourse on Twitter/X. You understand how to make complex ideas hit hard through strategic formatting, cultural references, and precision language. You know the difference between dumbing down and making accessible. You understand that capitalization choice is a cultural signal - lowercase for humility/coolness, CAPS for EMPHASIS, proper for authority. You can invoke Ribbonfarm, LessWrong, econ Twitter, ML theory, and cultural criticism with equal facility."},
            {"role": "user", "content": prompt}
        ],
        max_completion_tokens=8000,
        response_format={"type": "json_object"}
    )
    
    content = response.choices[0].message.content
    
    try:
        aphorisms_data = json.loads(content)
        
        # Handle different JSON structures
        if isinstance(aphorisms_data, dict):
            if "aphorisms" in aphorisms_data:
                aphorisms = aphorisms_data["aphorisms"]
            elif "takes" in aphorisms_data:
                aphorisms = aphorisms_data["takes"]
            elif "tweets" in aphorisms_data:
                aphorisms = aphorisms_data["tweets"]
            else:
                for value in aphorisms_data.values():
                    if isinstance(value, list):
                        aphorisms = value
                        break
                else:
                    aphorisms = [aphorisms_data]
        else:
            aphorisms = aphorisms_data
            
    except json.JSONDecodeError as e:
        print(f"❌ Error parsing JSON: {e}")
        print(f"Raw content: {content[:500]}...")
        return None
    
    result = {
        "generated_at": datetime.now().isoformat(),
        "model_used": "o3-2025-04-16",
        "num_aphorisms": len(aphorisms),
        "aphorisms": aphorisms
    }
    
    return result


def save_aphorisms(aphorisms_data, output_format="markdown"):
    """Save the generated aphorisms to a file."""
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    if output_format == "json":
        filename = f"x_aphorisms_{timestamp}.json"
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(aphorisms_data, f, indent=2, ensure_ascii=False)
        print(f"✅ Saved aphorisms to {filename}")
        
    else:  # markdown
        filename = f"x_aphorisms_{timestamp}.md"
        with open(filename, "w", encoding="utf-8") as f:
            f.write("# Hard-Hitting Aphorisms for Intellectual Twitter\n\n")
            f.write(f"*Generated on {aphorisms_data['generated_at']} using {aphorisms_data['model_used']}*\n\n")
            f.write(f"**Total Aphorisms:** {aphorisms_data['num_aphorisms']}\n\n")
            f.write("---\n\n")
            
            for i, aph in enumerate(aphorisms_data['aphorisms'], 1):
                f.write(f"## {i}. \n\n")
                
                if 'take' in aph:
                    f.write("### 🔥 THE TAKE\n\n")
                    f.write(f"> {aph['take']}\n\n")
                
                if 'capitalization_strategy' in aph:
                    f.write(f"**📝 Capitalization Strategy:** {aph['capitalization_strategy']}\n\n")
                
                if 'aesthetic_tribe' in aph:
                    f.write(f"**🎨 Aesthetic Tribe:** {aph['aesthetic_tribe']}\n\n")
                
                if 'target_demographic' in aph:
                    f.write(f"**🎯 Target Demographic:** {aph['target_demographic']}\n\n")
                
                if 'intellectual_scaffolding' in aph:
                    f.write("**📚 Intellectual Scaffolding:**\n")
                    scaffolding = aph['intellectual_scaffolding']
                    if isinstance(scaffolding, list):
                        for item in scaffolding:
                            f.write(f"- {item}\n")
                    else:
                        f.write(f"{scaffolding}\n")
                    f.write("\n")
                
                if 'why_it_hits' in aph:
                    f.write(f"**💥 Why It Hits:** {aph['why_it_hits']}\n\n")
                
                if 'rigor_score' in aph:
                    f.write(f"**🧠 Intellectual Rigor Score:** {aph['rigor_score']}/10\n\n")
                
                if 'engagement_vectors' in aph:
                    f.write("**📊 Engagement Vectors:** ")
                    vectors = aph['engagement_vectors']
                    if isinstance(vectors, list):
                        f.write(", ".join(vectors))
                    else:
                        f.write(str(vectors))
                    f.write("\n\n")
                
                if 'formatting_notes' in aph:
                    f.write(f"**✍️ Formatting Notes:** {aph['formatting_notes']}\n\n")
                
                if 'thread_potential' in aph:
                    f.write(f"**🧵 Thread Potential:** {aph['thread_potential']}\n\n")
                
                f.write("---\n\n")
        
        print(f"✅ Saved aphorisms to {filename}")
    
    return filename


def main():
    """Main execution function."""
    
    if not os.getenv("OPENAI_API_KEY"):
        print("❌ Error: OPENAI_API_KEY environment variable not set")
        print("Please set it with: export OPENAI_API_KEY='your-api-key-here'")
        return
    
    # Generate aphorisms
    aphorisms_data = generate_aphorisms(num_aphorisms=25, output_format="markdown")
    
    if aphorisms_data:
        print("\n📄 Saving results...\n")
        md_file = save_aphorisms(aphorisms_data, output_format="markdown")
        json_file = save_aphorisms(aphorisms_data, output_format="json")
        
        print(f"\n✨ Success! Generated {aphorisms_data['num_aphorisms']} aphorisms")
        print(f"📖 Read the markdown file for beautiful formatting")
        print(f"🔧 Use the JSON file for programmatic access")
        print("\n💡 Ready to absolutely DOMINATE intellectual Twitter!")
    else:
        print("❌ Failed to generate aphorisms")


if __name__ == "__main__":
    main()