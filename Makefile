.DEFAULT_GOAL := test

test_clean:
	poetry run coverage erase
	touch check_file_exists.py

mypy:
	poetry run mypy

pylint:
	poetry run pylint check_file_exists.py

pytest:
	poetry run coverage erase
	poetry run pytest
	poetry run coverage report -m --fail-under=100

black:
	poetry run black check_file_exists.py tests

pip-audit:
	poetry run pip-audit --desc on

test: mypy pylint pytest black pip-audit
