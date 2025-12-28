# HERESY OF ORIGIN

**Cultural Monad Optimization System**

Accelerationist critique-through-practice via granular optimization of cultural monads.

---

## Theory

If the algorithm dictates perception which dictates monadistic realities...

- **Frankfurt School** (Adorno's Culture Industry) — Microsegmented content generation
- **Leibnizian Monads** — Isolated demographic reality tunnels
- **Bourdieu's Cultural Capital** — Soft interaction mapping
- **Heidegger's Tool-at-Hand** — Hard behavioral patterns
- **Implementation-level X algorithm** — Based on 2023 source release (~6000 features)

---

## Architecture

```
generators/
├── utils.py                  # Shared protocol (parse, save, run)
├── __init__.py               # Package exports
├── twitter/
│   ├── wizard.py             # Implementation-level demographics
│   ├── lived_experience.py   # Phenomenological profiles
│   ├── soft_hard_enhanced.py # Three-dimensional mapping
│   └── aphorisms.py          # Engagement-optimized takes
└── substack/
    ├── reader_demographics.py
    ├── writing_styles.py
    ├── about_page.py
    └── article_writer.py
```

Each generator is a **monad** — an isolated unit that:
- Contains its own prompt logic (the unique "soul")
- Defines its own output structure (the unique "form")
- Interfaces with the world through `utils.py` (the shared protocol)

No inheritance hierarchies. No framework lock-in. No magic.
Generators can still run standalone (`python wizard.py`).

---

## Quick Start

```bash
# Clone
git clone https://github.com/closestfriend/heresy-of-origin.git
cd heresy-of-origin

# Run (auto-creates venv, installs deps, loads .env.local)
./monad.sh
```

Create `.env.local` with your API key:
```bash
OPENAI_API_KEY=your-key-here

# Or for OpenRouter:
LLM_PROVIDER=openrouter
OPENROUTER_API_KEY=your-key-here
```

Then open `http://localhost:8000`

---

## Generators

### Twitter/X

| Generator | Description |
|-----------|-------------|
| **The Wizard** | Implementation-level demographics: SOFT (Bourdieu), HARD (behavioral), ALGORITHMIC (6000 features, SafetyLabels), META (2023 gap awareness) |
| **Lived Experience** | Phenomenological profiles — what it *feels like* to exist in algorithmic reality |
| **Soft+Hard+Algorithmic** | Three-dimensional platform interaction mapping |
| **Aphorisms** | Hard-hitting takes for intellectual Twitter with strategic capitalization |

### Substack

| Generator | Description |
|-----------|-------------|
| **Reader Demographics** | Hyper-specific micro-demographics with auxiliary interest vectors |
| **Writing Styles** | Literary archetypes for content voice matching |
| **About Page** | Conversion-optimized with authenticity validation |
| **Article Writer** | Long-form with Human Authenticity Validation Module (anti-AI-tell) |

---

## Adding New Generators

Define three things:

```python
# 1. Configuration
GENERATOR_CONFIG = {
    "name": "my_generator",
    "item_keys": ["items", "results"],
    "max_tokens": 6000,
    "temperature": 0.7,
}

# 2. Prompts
SYSTEM_PROMPT = "You are..."
def build_prompt(num_items): return f"Generate {num_items}..."

# 3. Markdown formatter (generator-specific output form)
def format_markdown(data, f):
    f.write("# Output\n\n")
    for item in data["items"]:
        f.write(f"## {item['name']}\n\n")
```

Everything else inherits from `utils.py`.

---

## The 2023 Gap

Based on `github.com/twitter/the-algorithm`:

- **~6000 features** in ranking (not the 5 signals folk theory suggests)
- **Signal weights**: Favorites, Video Watch Time, Tweet Clicks, Retweets
- **Heuristics**: Author Diversity, Content Balance, Feedback Fatigue
- **SafetyLabels**: Drop vs Interstitial vs Downranking
- **Candidate sources**: In-Network (~50%) vs Out-of-Network (UTEG/FRS)

Epistemic humility: 2023 code, 2 years old, parts removed, Elon-era changes unknown.

---

## API

- `GET /` — UI
- `GET /api/generators` — List generators
- `POST /api/generate` — Execute generation
- `GET /api/outputs` — List files
- `GET /api/outputs/{filename}` — Download
- `POST /api/article/generate` — Article pipeline

---

## Docker

```bash
cp .env.example .env
# Add OPENAI_API_KEY to .env
docker-compose up -d
```

Outputs persist in `./outputs/`

---

## Philosophy

The monad is the message.

Each generator exists as a windowless unit with its own internal logic, but all speak the same language to the outside world. They can be composed, chained, and evolved independently.

This is critique-through-practice: using the machinery of algorithmic culture production to expose its own operations.

---

*"I feel like I'm screaming into the void, but every now and then, someone hears me and it's like, 'oh, I'm not crazy!' But then it goes back to silence."*
