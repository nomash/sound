#!/bin/bash
shopt -s nocasematch

RUN_COMMAND="uvicorn"
RUN_ARGS="api.main:app --host 0.0.0.0 --port 8000"

DJANGO_SETTINGS_MODULE="nomash.development"

export DJANGO_SETTINGS_MODULE

echo Starting ucpython using $RUN_COMMAND $RUN_ARGS
$RUN_COMMAND $RUN_ARGS
