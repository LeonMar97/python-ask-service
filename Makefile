install:poetry.lock pyproject.toml
	poetry install
run: 
	poetry run flask -A python_ask_service.backend.app run
format:
	poetry run ruff format python_ask_service
lint:
	poetry run ruff check python_ask_service
lint-fix:
	poetry run ruff check --fix password_manager_gui
lint-unsafe:
	poetry run check --fix --unsafe-fixes password_manager_gui
format-tests:
	poetry run ruff format tests/
lint-tests:
	poetry run ruff check tests/
lint-tests-fix:
	poetry run ruff check --fix tests/
lint-tests-unsafe:
	poetry run check --fix --unsafe-fixes tests/
test:
	poetry run pytest

