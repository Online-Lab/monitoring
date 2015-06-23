#!/bin/sh

sleep 10
cd src
# migrate db, so we have the latest db schema
python manage.py migrate
python manage.py collectstatic --noinput
# start development server on public ip interface, on port 8000
gunicorn main.wsgi:application -c gunicorn.conf.py
