#!/usr/bin/env python3
"""
Run this script to fire a demo onboarding event.
Make sure the backend is running first: uvicorn api.main:app --reload
"""
import httpx
import webbrowser
import time

HIRE = {
    "name": "Sarah Reynolds",
    "role": "Senior Product Designer",
    "department": "Product",
    "start_date": "2026-04-07",
    "manager_name": "James Okafor",
    "personal_email": "sarah.reynolds@gmail.com",
}

BASE = "http://localhost:8000"

print("Firing onboarding trigger...")
r = httpx.post(f"{BASE}/webhook/offer-accepted", json=HIRE)
r.raise_for_status()

data = r.json()
oid = data["onboarding_id"]
print(f"Onboarding started: {oid}")

time.sleep(1)
webbrowser.open(f"http://localhost:3000/onboarding/{oid}")
print(f"Dashboard opened at http://localhost:3000/onboarding/{oid}")
