
server:
	python manage.py runserver

migrate:
	python manage.py makemigrations
	python manage.py migrate

user:
	python manage.py createsuperuser

shell:
	python manage.py shell

venv:
	python -m venv venv

install:
	pip install -r requirements.txt

active:
	source venv/bin/activate
