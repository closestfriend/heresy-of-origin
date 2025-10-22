#!/bin/bash

# CULTURAL MONAD OPTIMIZATION SYSTEM
# Startup script

echo "┌───────────────────────────────────────────────────────────────┐"
echo "│ CULTURAL MONAD OPTIMIZATION SYSTEM v0.1                       │"
echo "│ [CLASSIFICATION: ACCELERATIONIST CRITIQUE-THROUGH-PRACTICE]   │"
echo "└───────────────────────────────────────────────────────────────┘"
echo ""

# Port configuration (default: 8000)
PORT=${PORT:-8000}

# Check if venv exists
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv

    echo "Installing dependencies..."
    ./venv/bin/pip install -q -r requirements.txt
fi

# Load .env.local if it exists
if [ -f ".env.local" ]; then
    export $(cat .env.local | xargs)
fi

# Check for API key
if [ -z "$OPENAI_API_KEY" ]; then
    echo "⚠️  WARNING: OPENAI_API_KEY not set"
    echo "   Set it in .env.local or export OPENAI_API_KEY='your-key'"
    echo ""
fi

# Kill existing process on port if any
if lsof -ti:$PORT > /dev/null 2>&1; then
    echo "⚠️  Port $PORT already in use. Killing existing process..."
    lsof -ti:$PORT | xargs kill 2>/dev/null
    sleep 1
fi

echo "Starting server on http://localhost:$PORT"
echo ""
echo "Press Ctrl+C to stop"
echo ""

# Start the server with configurable port
PORT=$PORT ./venv/bin/python app.py
