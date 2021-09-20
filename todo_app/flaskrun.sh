#!/bin/bash
source /srv/www/.venv/bin/activate
poetry run flask run -h 0.0.0.0
