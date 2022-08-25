#! /var/www/python/tux.tools/tux.tools/venv/bin/python3
import bjoern
from main import app

if __name__ == "__main__":
    bjoern.run(app, '0.0.0.0', 5050)

