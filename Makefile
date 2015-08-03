.PHONY: test

help:
	@echo "  env         create a development environment using virtualenv"
	@echo "  deps        install dependencies"
	@echo "  clean       remove unwanted stuff"
	@echo "  test        run all your tests using nose"

env:
	pip install virtualenv && \
    virtualenv --always-copy .env && \
	. .env/bin/activate && \
	make deps

deps:
	pip install -r eggs.txt

clean:
	find . -name '*.pyc' -exec rm -f {} \; && \
    rm -rf temp && \
    rm -rf dist

test:
	make clean && \
	make env && \
	. .env/bin/activate && \
	nosetests -s --with-xunit --rednose --force-color
