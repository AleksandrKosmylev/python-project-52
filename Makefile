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
	poetry run coverage report
	poetry run coverage xml

