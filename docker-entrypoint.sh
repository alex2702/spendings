#!/bin/bash

python manage.py migrate --no-input
python -m gunicorn spendings.wsgi --bind 0.0.0.0:8000
