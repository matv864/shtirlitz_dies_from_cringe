deps:
	pip install black
	python -m pip install poetry
	poetry install

migrate:
	poetry run python -m src.utils.migrate

update-poetry:
	poetry install

run:
	poetry run uvicorn src.app:app --reload --host 0.0.0.0