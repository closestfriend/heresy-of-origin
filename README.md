# CULTURAL MONAD OPTIMIZATION SYSTEM

**CLASSIFICATION: ACCELERATIONIST CRITIQUE-THROUGH-PRACTICE**

## Overview

If the algorithm dictates perception which dictates monadistic realities...

This system provides tooling for granular optimization of cultural production at the level of individual monads. Implements Frankfurt School critique through actual working code.

## Theory → Implementation

- **Adorno's Culture Industry** → Microsegmented content generation
- **Leibnizian Monads** → Isolated demographic units with windowless realities
- **Bourdieu's Cultural Capital** → Soft interaction mapping
- **Heidegger's Tool-at-Hand** → Hard behavioral patterns
- **Algorithmic Reality** → Implementation-level understanding of X's recommendation system

## Architecture

```
automation_api_prompts/
├── app.py                      # FastAPI backend
├── static/
│   └── index.html              # Pentagon-agency aesthetic UI
├── generators/
│   ├── twitter/
│   │   ├── wizard.py           # Implementation-level (6000 features)
│   │   ├── lived_experience.py # Phenomenological
│   │   ├── soft_hard_enhanced.py # Soft+Hard+Algorithmic
│   │   └── aphorisms.py        # Engagement-optimized
│   └── substack/
│       ├── reader_demographics.py
│       └── writing_styles.py
└── outputs/                    # Generated artifacts
```

## Installation

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Set OpenAI API key (required for generation)
export OPENAI_API_KEY='your-api-key-here'
```

## Usage

**Recommended (uses startup script):**
```bash
./start.sh
```

The startup script will:
- Auto-create venv if needed
- Auto-install dependencies
- Load `.env.local` for API key
- Kill any existing process on the port
- Start the server

**Manual:**
```bash
# Activate virtual environment
source venv/bin/activate

# Start the server
./venv/bin/python app.py

# Or with custom port
PORT=3000 ./venv/bin/python app.py
```

**Access:**
Default: `http://localhost:8000`
Custom port: `http://localhost:PORT`

**Tech Stack:**
- Pure Python (no npm/node required)
- FastAPI backend
- Vanilla JS frontend
- No build step needed

## Interface

Minimal, monochrome, monospace. Pentagon-agency aesthetic for interacting with cultural manipulation apparatus.

- Select platform (Twitter/X or Substack)
- Choose generators (demographics, content)
- Set parameters (count, model, format)
- Execute
- Download outputs

## Generators

### Twitter/X

**Demographics:**
- Soft+Hard+Algorithmic: Technical mapping of cultural capital + UI patterns + algorithm awareness
- The Wizard: Implementation-level understanding (github.com/twitter/the-algorithm)
- Lived Experience: Phenomenological descriptions without academic jargon

**Content:**
- X Aphorisms: Engagement-optimized intellectual takes with strategic capitalization

### Substack/Longform

**Demographics:**
- Reader Demographics: Hyper-specific niche personas with auxiliary interest vectors

**Content:**
- Writing Styles: Literary traditions mapped to Substack voice

## API Endpoints

- `GET /` - UI
- `GET /api/generators` - List available generators
- `POST /api/generate` - Execute generation
- `GET /api/outputs` - List generated files
- `GET /api/outputs/{filename}` - Download file
- `GET /api/status` - System status

## Docker Deployment

For containerized deployment with persistent storage:

**Prerequisites:**
- Docker and Docker Compose installed
- OpenAI API key

**Setup:**
```bash
# Copy environment template
cp .env.example .env

# Edit .env and add your OpenAI API key
# OPENAI_API_KEY=your_openai_api_key_here

# Start the system
docker-compose up -d

# Check status
docker-compose logs cultural-monad-system
```

**Access:**
- Interface: http://localhost:8000
- Generated outputs persist in `./outputs/`
- System logs in `./logs/`

**Management:**
```bash
# Stop the system
docker-compose down

# Rebuild after changes
docker-compose up --build

# View logs
docker-compose logs -f
```

## Notes

This is critique-through-practice. The apparatus demonstrates its own functioning while enabling cultural production at atomic scale.

The monad is the message.
