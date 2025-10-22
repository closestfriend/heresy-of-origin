#!/usr/bin/env python3
"""
Generate detailed, niche demographic profiles of Substack and Medium readers.
These profiles include granular interests, behaviors, and semantic understanding vectors.
"""

import os
import json
from datetime import datetime
from openai import OpenAI

def generate_reader_demographics(num_demographics=10, output_format="markdown"):
    """
    Generate diverse reader demographic profiles using OpenAI's API.
    
    Args:
        num_demographics: Number of distinct demographics to generate (default: 10)
        output_format: 'markdown' or 'json' (default: markdown)
    
    Returns:
        Dictionary containing the generated demographics
    """
    
    # Initialize OpenAI client (requires OPENAI_API_KEY environment variable)
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    
    prompt = f"""You are an expert in digital media demographics, sociology, and cultural analysis with deep knowledge of online reading communities.

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

    print("👥 Generating reader demographics using OpenAI...")
    print(f"📊 Requesting {num_demographics} distinct demographic profiles...\n")
    
    # Call OpenAI API with the latest model
    response = client.chat.completions.create(
        model="gpt-4o",  # Using GPT-4o - fast and capable
        messages=[
            {"role": "system", "content": "You are an expert in demographic analysis, cultural anthropology, and digital media consumption patterns. You create detailed, nuanced reader personas that capture authentic behavioral patterns and interest networks."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.8,  # Higher temperature for creative variety
        max_tokens=6000,  # Plenty for detailed profiles
        response_format={"type": "json_object"}  # Ensure JSON output
    )
    
    # Parse the response
    content = response.choices[0].message.content
    
    # Check if content is empty
    if not content:
        print("❌ Error: API returned empty content")
        print(f"Response object: {response}")
        return None
    
    # Extract JSON from the response
    try:
        demographics_data = json.loads(content)
        
        # Handle different possible JSON structures
        if isinstance(demographics_data, dict):
            if "demographics" in demographics_data:
                demographics = demographics_data["demographics"]
            elif "reader_demographics" in demographics_data:
                demographics = demographics_data["reader_demographics"]
            elif "profiles" in demographics_data:
                demographics = demographics_data["profiles"]
            else:
                # Take the first list value found
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
        if content:
            print(f"Raw content: {content[:500]}...")
        else:
            print("Raw content is None or empty")
        return None
    
    result = {
        "generated_at": datetime.now().isoformat(),
        "model_used": "gpt-4o",
        "num_demographics": len(demographics),
        "demographics": demographics
    }
    
    return result


def save_demographics(demographics_data, output_format="markdown"):
    """Save the generated demographics to a file."""
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    if output_format == "json":
        filename = f"reader_demographics_{timestamp}.json"
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(demographics_data, f, indent=2, ensure_ascii=False)
        print(f"✅ Saved demographics to {filename}")
        
    else:  # markdown
        filename = f"reader_demographics_{timestamp}.md"
        with open(filename, "w", encoding="utf-8") as f:
            f.write("# Substack & Medium Reader Demographics\n\n")
            f.write(f"*Generated on {demographics_data['generated_at']} using {demographics_data['model_used']}*\n\n")
            f.write(f"**Total Demographics:** {demographics_data['num_demographics']}\n\n")
            f.write("---\n\n")
            
            for i, demo in enumerate(demographics_data['demographics'], 1):
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
        
        print(f"✅ Saved demographics to {filename}")
    
    return filename


def main():
    """Main execution function."""
    
    # Check for API key
    if not os.getenv("OPENAI_API_KEY"):
        print("❌ Error: OPENAI_API_KEY environment variable not set")
        print("Please set it with: export OPENAI_API_KEY='your-api-key-here'")
        return
    
    # Generate demographics
    demographics_data = generate_reader_demographics(num_demographics=15, output_format="markdown")
    
    if demographics_data:
        # Save in both formats
        print("\n📄 Saving results...\n")
        md_file = save_demographics(demographics_data, output_format="markdown")
        json_file = save_demographics(demographics_data, output_format="json")
        
        print(f"\n✨ Success! Generated {demographics_data['num_demographics']} reader demographics")
        print(f"📖 Read the markdown file for beautiful formatting")
        print(f"🔧 Use the JSON file for programmatic access")
        print("\n💡 You can now use these demographics to target specific reader personas!")
    else:
        print("❌ Failed to generate demographics")


if __name__ == "__main__":
    main()