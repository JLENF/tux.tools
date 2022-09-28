#!/bin/sh
gunicorn --chdir app wsgi:app -w 4 --threads 4 -b 0.0.0.0:8000