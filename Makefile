setup1: install build publish package-install

setup2: install build publish package-reinstall

setup3: build package-reinstall

install:
	poetry install

brain-games:
	poetry run brain-games

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

package-reinstall:
	python3 -m pip install --force-reinstall --user dist/*.whl


.PHONY: install