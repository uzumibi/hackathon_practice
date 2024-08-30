fmt:
	poetry run black .
	poetry run isort .
lint:
	poetry run flake8 .
	poetry run mypy .