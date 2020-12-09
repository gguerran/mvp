#!/bin/sh

source venv/bin/activate

python manage.py migrate

python manage.py collectstatic --noinput

uwsgi --socket :8001 --master --enable-threads --module mvp.wsgi
