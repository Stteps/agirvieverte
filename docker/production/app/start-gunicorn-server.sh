#!/bin/sh
gunicorn config.wsgi:application --bind 0.0.0.0:8030 --timeout 60 --access-logfile - --error-logfile -