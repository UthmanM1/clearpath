# ClearPath — Intelligent Employee Onboarding Orchestrator

An autonomous multi-agent AI system that orchestrates new hire onboarding across IT provisioning, HR documents, calendar scheduling, and communications — with a human-in-the-loop approval checkpoint.

## What it does

1. Submit a new hire's details (name, role, department, start date)
2. The **Orchestrator agent** spins up and delegates in parallel:
   - **IT Provisioner** — provisions Google Workspace, Slack, GitHub, Notion, Figma, VPN
   - **HR Docs agent** — generates a personalised welcome pack for the new hire
3. Pipeline **pauses** at the HITL checkpoint — manager approves access in the dashboard
4. On approval, in parallel:
   - **Calendar agent** — books intro calls, team standup, and buddy sessions
   - **Comms agent** — sends personalised Slack and email welcome messages
5. Dashboard shows "Day-1 ready" ✓

## Setup

### Requirements
- Python 3.9+
- Node.js (optional — see Frontend section)

### 1. Backend

```bash
cd clearpath
pip install -r requirements.txt
python -m uvicorn api.main:app --reload
# Backend runs at http://localhost:8000
```

### 2. Frontend

**Option A — Single HTML file (recommended, no install needed)**

Just open `frontend/index.html` directly in your browser. No npm required.

**Option B — React dev server**

```bash
cd frontend
npm install
npm start
# Dashboard runs at http://localhost:3000
```

### 3. Trigger the demo

With the backend running:

```bash
# Option A — use the web form in your browser
# Option B — run the trigger script
python trigger_demo.py
```

## API

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/webhook/offer-accepted` | Start onboarding |
| GET | `/onboarding/{id}/status` | Poll live state |
| POST | `/onboarding/{id}/approve` | HITL approval |
| GET | `/onboarding` | List all onboardings |
| GET | `/docs` | Interactive API docs |

## Architecture

```
Trigger
  └── Orchestrator Agent
        ├── IT Provisioner Agent      (parallel)
        ├── HR Documents Agent        (parallel)
        ├── [HITL Approval Checkpoint]
        ├── Calendar Agent            (parallel)
        └── Comms Agent               (parallel)
```

## Tech stack

- **Backend** — Python, FastAPI, asyncio
- **Frontend** — React (or single HTML file)
- **Agent framework** — Airia
- **Architecture** — Multi-agent, human-in-the-loop, parallel execution
