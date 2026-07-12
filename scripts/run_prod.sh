#!/bin/bash
# Run the application in production mode using Gunicorn with Uvicorn workers
./venv/bin/gunicorn app.main:app -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000