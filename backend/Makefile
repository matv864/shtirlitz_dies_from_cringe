deps:
	pip install black
	python -m pip install poetry
	poetry install

update-poetry:
	poetry install

run:
	poetry run uvicorn src.app:app --reload --host 0.0.0.0

test:
	pytest tests