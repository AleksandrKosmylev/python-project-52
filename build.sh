#!/usr/bin/env bash
# exit on error
set -o errexit

poetry install  --no-root

python manage.py migrate
poetry run ./manage.py collectstatic