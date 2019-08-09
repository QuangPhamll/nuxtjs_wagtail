#!/bin/sh

python manage.py migrate --noinput
python manage.py create_admin_user
exec gunicorn backend.wsgi:application --bind 0.0.0.0:7999 --workers 3
