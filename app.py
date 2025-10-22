#!/usr/bin/env python3
"""
CULTURAL MONAD OPTIMIZATION SYSTEM
FastAPI backend for accelerationist critique-through-practice
"""

import os
import sys
import json
from datetime import datetime
from pathlib import Path
from typing import Optional
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse
from pydantic import BaseModel
import importlib.util
from dotenv import load_dotenv

# Load environment variables from .env.local
load_dotenv('.env.local')

app = FastAPI(title="Cultural Monad Optimization System")

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

class GenerationRequest(BaseModel):
    generator_type: str  # "twitter_wizard", "twitter_lived", etc.
    num_items: int = 15
    output_format: str = "markdown"
    model: str = "o3-2025-04-16"

class GenerationResponse(BaseModel):
    status: str
    message: str
    output_files: list[str] = []
    timestamp: str
    tokens_used: Optional[int] = None
    cost: Optional[float] = None

# Generator mapping
GENERATORS = {
    "twitter_wizard": {
        "path": "generators/twitter/wizard.py",
        "function": "generate_wizard_demographics",
        "save_function": "save_wizard_demographics",
        "name": "The Wizard (Implementation-Level)"
    },
    "twitter_lived": {
        "path": "generators/twitter/lived_experience.py",
        "function": "generate_lived_experience_demographics",
        "save_function": "save_lived_experience_demographics",
        "name": "Lived Experience (Phenomenological)"
    },
    "twitter_soft_hard": {
        "path": "generators/twitter/soft_hard_enhanced.py",
        "function": "generate_twitter_demographics",
        "save_function": "save_twitter_demographics",
        "name": "Soft+Hard+Algorithmic"
    },
    "twitter_aphorisms": {
        "path": "generators/twitter/aphorisms.py",
        "function": "generate_aphorisms",
        "save_function": "save_aphorisms",
        "name": "X Aphorisms (Engagement-Optimized)"
    },
    "substack_readers": {
        "path": "generators/substack/reader_demographics.py",
        "function": "generate_reader_demographics",
        "save_function": "save_demographics",
        "name": "Reader Demographics"
    },
    "substack_styles": {
        "path": "generators/substack/writing_styles.py",
        "function": "generate_writing_styles",
        "save_function": "save_styles",
        "name": "Writing Styles"
    }
}

def load_generator_module(generator_path: str):
    """Dynamically load a generator module."""
    spec = importlib.util.spec_from_file_location("generator", generator_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

@app.get("/")
async def root():
    """Serve the main interface."""
    return FileResponse("static/index.html")

@app.get("/api/generators")
async def list_generators():
    """List all available generators."""
    return {
        "twitter": {
            "demographics": [
                {"id": "twitter_wizard", "name": GENERATORS["twitter_wizard"]["name"]},
                {"id": "twitter_lived", "name": GENERATORS["twitter_lived"]["name"]},
                {"id": "twitter_soft_hard", "name": GENERATORS["twitter_soft_hard"]["name"]}
            ],
            "content": [
                {"id": "twitter_aphorisms", "name": GENERATORS["twitter_aphorisms"]["name"]}
            ]
        },
        "substack": {
            "demographics": [
                {"id": "substack_readers", "name": GENERATORS["substack_readers"]["name"]}
            ],
            "content": [
                {"id": "substack_styles", "name": GENERATORS["substack_styles"]["name"]}
            ]
        }
    }

@app.post("/api/generate")
async def generate(request: GenerationRequest):
    """Execute a generator and return results."""

    if request.generator_type not in GENERATORS:
        raise HTTPException(status_code=400, detail=f"Unknown generator: {request.generator_type}")

    generator_info = GENERATORS[request.generator_type]

    try:
        # Load the generator module
        module = load_generator_module(generator_info["path"])

        # Get the generation function
        generate_func = getattr(module, generator_info["function"])
        save_func = getattr(module, generator_info["save_function"])

        # Execute generation
        if "aphorisms" in request.generator_type or "styles" in request.generator_type:
            # These use num_aphorisms or num_styles
            if "aphorisms" in request.generator_type:
                data = generate_func(num_aphorisms=request.num_items, output_format=request.output_format)
            else:
                data = generate_func(num_styles=request.num_items, output_format=request.output_format)
        else:
            # Demographics generators
            data = generate_func(num_demographics=request.num_items, output_format=request.output_format)

        if not data:
            raise HTTPException(status_code=500, detail="Generation failed")

        # Save outputs
        md_file = save_func(data, output_format="markdown")
        json_file = save_func(data, output_format="json")

        # Move files to outputs directory
        import shutil
        os.makedirs("outputs", exist_ok=True)

        md_dest = f"outputs/{Path(md_file).name}"
        json_dest = f"outputs/{Path(json_file).name}"

        shutil.move(md_file, md_dest)
        shutil.move(json_file, json_dest)

        return GenerationResponse(
            status="success",
            message=f"Generated {data.get('num_demographics') or data.get('num_aphorisms') or data.get('num_styles')} items",
            output_files=[md_dest, json_dest],
            timestamp=datetime.now().isoformat(),
            tokens_used=None,  # TODO: extract from API response
            cost=None  # TODO: calculate from tokens
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Generation error: {str(e)}")

@app.get("/api/outputs")
async def list_outputs():
    """List all generated output files."""
    outputs_dir = Path("outputs")
    if not outputs_dir.exists():
        return {"files": []}

    files = []
    for file in sorted(outputs_dir.glob("*"), key=lambda x: x.stat().st_mtime, reverse=True):
        files.append({
            "name": file.name,
            "size": file.stat().st_size,
            "modified": datetime.fromtimestamp(file.stat().st_mtime).isoformat(),
            "type": file.suffix
        })

    return {"files": files}

@app.get("/api/outputs/{filename}")
async def download_output(filename: str):
    """Download a specific output file."""
    file_path = Path("outputs") / filename

    if not file_path.exists():
        raise HTTPException(status_code=404, detail="File not found")

    return FileResponse(file_path, filename=filename)

@app.get("/api/article/inputs")
async def get_article_inputs():
    """List available demographics and styles for article generation."""
    outputs_dir = Path("outputs")

    demographics = []
    styles = []

    if outputs_dir.exists():
        # Find reader demographics JSON files
        for file in outputs_dir.glob("reader_demographics_*.json"):
            try:
                with open(file, 'r') as f:
                    data = json.load(f)
                    if 'demographics' in data:
                        for demo in data['demographics']:
                            demographics.append({
                                "label": demo.get('label', 'Unknown'),
                                "source_file": file.name,
                                "data": demo
                            })
            except Exception as e:
                print(f"Error reading {file}: {e}")

        # Find writing styles JSON files
        for file in outputs_dir.glob("writing_styles_*.json"):
            try:
                with open(file, 'r') as f:
                    data = json.load(f)
                    if 'styles' in data:
                        for style in data['styles']:
                            styles.append({
                                "name": style.get('name', 'Unknown'),
                                "source_file": file.name,
                                "data": style
                            })
            except Exception as e:
                print(f"Error reading {file}: {e}")

    return {
        "demographics": demographics,
        "styles": styles,
        "can_generate": len(demographics) > 0 and len(styles) > 0
    }

@app.post("/api/article/generate")
async def generate_article_endpoint(request: dict):
    """Generate a long-form article using demographic and style targeting."""

    demographic_label = request.get("demographic_label")
    style_name = request.get("style_name")
    topic = request.get("topic")
    word_count = request.get("word_count", "medium")
    model = request.get("model", "gpt-4o")

    if not all([demographic_label, style_name, topic]):
        raise HTTPException(status_code=400, detail="Missing required fields: demographic_label, style_name, topic")

    # Get the full demographic and style data
    inputs = await get_article_inputs()

    demographic_data = None
    style_data = None

    for demo in inputs["demographics"]:
        if demo["label"] == demographic_label:
            demographic_data = demo["data"]
            break

    for style in inputs["styles"]:
        if style["name"] == style_name:
            style_data = style["data"]
            break

    if not demographic_data:
        raise HTTPException(status_code=404, detail=f"Demographic not found: {demographic_label}")
    if not style_data:
        raise HTTPException(status_code=404, detail=f"Style not found: {style_name}")

    try:
        # Load the article generator module
        from generators.substack.article_writer import generate_article, save_article

        # Generate article
        article_data = generate_article(
            demographic_json=demographic_data,
            style_json=style_data,
            topic=topic,
            word_count=word_count,
            model=model
        )

        if not article_data:
            raise HTTPException(status_code=500, detail="Article generation failed")

        # Save outputs
        md_file = save_article(article_data, output_format="markdown")
        json_file = save_article(article_data, output_format="json")

        # Move files to outputs directory
        import shutil
        os.makedirs("outputs", exist_ok=True)

        md_dest = f"outputs/{Path(md_file).name}"
        json_dest = f"outputs/{Path(json_file).name}"

        shutil.move(md_file, md_dest)
        shutil.move(json_file, json_dest)

        return {
            "status": "success",
            "message": f"Generated {article_data['actual_word_count']} word article",
            "output_files": [md_dest, json_dest],
            "timestamp": datetime.now().isoformat(),
            "word_count": article_data['actual_word_count'],
            "target_demographic": demographic_label,
            "writing_style": style_name
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Article generation error: {str(e)}")

@app.get("/api/status")
async def status():
    """System status check."""
    return {
        "status": "operational",
        "timestamp": datetime.now().isoformat(),
        "generators_available": len(GENERATORS),
        "openai_key_set": bool(os.getenv("OPENAI_API_KEY"))
    }

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
