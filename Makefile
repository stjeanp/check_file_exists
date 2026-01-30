.DEFAULT_GOAL := test

test_clean:
	coverage erase
	touch check_file_exists.py

mypy:
	mypy

pylint:
	pylint check_file_exists.py

pytest:
	coverage erase
	pytest
	coverage report -m --fail-under=100

black:
	black check_file_exists.py tests

pip-audit:
	pip-audit --desc on

test: mypy pylint pytest black pip-audit
