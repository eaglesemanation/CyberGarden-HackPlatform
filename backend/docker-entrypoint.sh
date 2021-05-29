#!/bin/sh

set -e

. /app/.venv/bin/activate

# gunicorn reload is broken
exec python ./app.py
#exec gunicorn app:app --bind '0.0.0.0:8000' -k uvicorn.workers.UvicornWorker --reload
