#!/usr/bin/env bash
# ClearPath startup script
# Run from the clearpath/ directory

echo ""
echo "  ClearPath — Intelligent Onboarding Orchestrator"
echo ""

echo "  Starting backend..."
python -m uvicorn api.main:app --reload --port 8000 &
BACKEND_PID=$!

echo "  Backend running at http://localhost:8000"
echo "  API docs:  http://localhost:8000/docs"
echo ""
echo "  Open frontend/index.html in your browser to use the dashboard."
echo "  Or run: cd frontend && npm install && npm start"
echo ""
echo "  Press Ctrl+C to stop."
echo ""

trap "kill $BACKEND_PID 2>/dev/null; exit" INT TERM
wait
