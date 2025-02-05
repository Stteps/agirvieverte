#!/bin/sh
python manage.py collectstatic --noinput
python setup.py build_ext --inplace && rm -rf build/
python manage.py migrate --noinput
python manage.py compilemessages
