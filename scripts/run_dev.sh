#!/bin/bash
# Run the application in development model with auto-reload
./venv/bin/uvicorn app.main:app --reload --host 0.0.0.0 --port 8000