lint:
	poetry run flake8 task_manager

test:
	python manage.py test

run:
	python manage.py runserver

