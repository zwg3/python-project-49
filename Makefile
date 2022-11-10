install:
	poetry install
build:
	poetry build
publish:
	poetry bublish --dry-run
package-install:
	python3 -m pip install --user dist/hexlet_code-0.1.0-py3-none-any.whl
brain-games:
	poetry run brain-games
lint:
	poetry run flake8 brain_games
