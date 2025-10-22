#!/usr/bin/env python3
"""
Generate distinct writing style descriptions for literary Substack content.
These styles will be used to guide AI assistants in article writing.
"""

import os
import json
from datetime import datetime
from openai import OpenAI

def generate_writing_styles(num_styles=10, output_format="markdown"):
    """
    Generate diverse writing style descriptions using OpenAI's API.
    
    Args:
        num_styles: Number of distinct styles to generate (default: 10)
        output_format: 'markdown' or 'json' (default: markdown)
    
    Returns:
        Dictionary containing the generated styles
    """
    
    # Initialize OpenAI client (requires OPENAI_API_KEY environment variable)
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    
    prompt = f"""You are a literary expert and writing coach with deep knowledge of various writing traditions, from classical to contemporary.

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

    print("🎨 Generating writing styles using OpenAI...")
    print(f"📝 Requesting {num_styles} distinct styles...\n")
    
    # Call OpenAI API with the latest model
    response = client.chat.completions.create(
        model="o3-2025-04-16",  # Using o3 - advanced reasoning model
        messages=[
            {"role": "system", "content": "You are an expert in literary analysis and writing styles. You provide detailed, nuanced descriptions that capture the essence of different writing approaches."},
            {"role": "user", "content": prompt}
        ],
        # Note: o3 models only support default temperature (1)
        max_completion_tokens=4000,  # o3 models use max_completion_tokens instead of max_tokens
        response_format={"type": "json_object"}  # Ensure JSON output
    )
    
    # Parse the response
    content = response.choices[0].message.content
    
    # Extract JSON from the response
    try:
        styles_data = json.loads(content)
        
        # Handle different possible JSON structures
        if isinstance(styles_data, dict):
            if "styles" in styles_data:
                styles = styles_data["styles"]
            elif "writing_styles" in styles_data:
                styles = styles_data["writing_styles"]
            else:
                # Take the first list value found
                for value in styles_data.values():
                    if isinstance(value, list):
                        styles = value
                        break
                else:
                    styles = [styles_data]
        else:
            styles = styles_data
            
    except json.JSONDecodeError as e:
        print(f"❌ Error parsing JSON: {e}")
        print(f"Raw content: {content[:500]}...")
        return None
    
    result = {
        "generated_at": datetime.now().isoformat(),
        "model_used": "o3-2025-04-16",
        "num_styles": len(styles),
        "styles": styles
    }
    
    return result


def save_styles(styles_data, output_format="markdown"):
    """Save the generated styles to a file."""
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    if output_format == "json":
        filename = f"writing_styles_{timestamp}.json"
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(styles_data, f, indent=2, ensure_ascii=False)
        print(f"✅ Saved styles to {filename}")
        
    else:  # markdown
        filename = f"writing_styles_{timestamp}.md"
        with open(filename, "w", encoding="utf-8") as f:
            f.write("# Literary Writing Styles for Substack\n\n")
            f.write(f"*Generated on {styles_data['generated_at']} using {styles_data['model_used']}*\n\n")
            f.write(f"**Total Styles:** {styles_data['num_styles']}\n\n")
            f.write("---\n\n")
            
            for i, style in enumerate(styles_data['styles'], 1):
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
        
        print(f"✅ Saved styles to {filename}")
    
    return filename


def main():
    """Main execution function."""
    
    # Check for API key
    if not os.getenv("OPENAI_API_KEY"):
        print("❌ Error: OPENAI_API_KEY environment variable not set")
        print("Please set it with: export OPENAI_API_KEY='your-api-key-here'")
        return
    
    # Generate styles
    styles_data = generate_writing_styles(num_styles=12, output_format="markdown")
    
    if styles_data:
        # Save in both formats
        print("\n📄 Saving results...\n")
        md_file = save_styles(styles_data, output_format="markdown")
        json_file = save_styles(styles_data, output_format="json")
        
        print(f"\n✨ Success! Generated {styles_data['num_styles']} writing styles")
        print(f"📖 Read the markdown file for beautiful formatting")
        print(f"🔧 Use the JSON file for programmatic access")
        print("\n💡 You can now use these styles to guide Claude in writing articles!")
    else:
        print("❌ Failed to generate styles")


if __name__ == "__main__":
    main()