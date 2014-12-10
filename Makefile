
install:
	pip install -r requirements.txt

build:
	python manage.py migrate
	python manage.py createsuperuser
	python manage.py loaddata planets.json
	python manage.py loaddata people.json
	python manage.py loaddata species.json
	python manage.py loaddata starships.json
	python manage.py loaddata vehicles.json
	python manage.py loaddata transport.json
	python manage.py loaddata films.json


serve:
	python manage.py runserver


drop_db:
	python manage.py flush
