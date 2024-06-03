#!/usr/bin/env sh
set -e

if test -f "../.venv/bin/python"; then
    ../.venv/bin/python -m pytest tests
fi

if test -f "../.venv//python"; then
    ../.venv/Scripts/python -m pytest tests
fi
