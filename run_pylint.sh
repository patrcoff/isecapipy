#!/usr/bin/env sh

if test -f "../.venv/bin/python"; then
    ../.venv/bin/python -m pylint isecapipy
fi

if test -f "../.venv//python"; then
    ../.venv/Scripts/python -m pylint isecapipy
fi
