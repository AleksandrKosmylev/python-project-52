install:
	poetry install

lint:
	poetry run flake8 task_manager

test:
	poetry run python manage.py test

run:
	python manage.py runserver

test_coverage:
	poetry run coverage run manage.py test
	poetry run coverage report -m --include=task_manager/* --omit=task_manager/settings.py
	poetry run coverage xml --include=task_manager/* --omit=task_manager/settings.py

