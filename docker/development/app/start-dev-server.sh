#!/bin/sh
echo "Running migrations.."
python manage.py migrate
echo "Compiling i18n files.."
python manage.py compilemessages
echo "Starting server.."
python manage.py runserver 0.0.0.0:8000