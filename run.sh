#!/bin/sh
sleep 5
# python manage.py createsuperuser
# python manage.py createsuperuser --noinput --username root --email info@swapi.dev

python manage.py migrate
make load_data
python manage.py runserver 0.0.0.0:8000
