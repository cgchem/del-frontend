#!/usr/bin/env bash
gunicorn main:app -b 0.0.0.0:8000 --access-logfile guni.log --reload --reload-extra-file main/static --reload-extra-file main/templates