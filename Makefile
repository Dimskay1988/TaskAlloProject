run:
	python manage.py runserver

migrate:
	python manage.py makemigrations
	python manage.py migrate

dependencies:
	pip install -r requirements.txt

add test bd:
	python manage.py loaddata test_fixtures.json
