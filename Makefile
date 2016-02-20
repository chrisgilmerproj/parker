#! /usr/bin/make 

PACKAGE_NAME=parker

VENV_DIR?=.venv
VENV_ACTIVATE=$(VENV_DIR)/bin/activate
WITH_VENV=. $(VENV_ACTIVATE);

TEST_OUTPUT?=nosetests.xml
COVERAGE_OUTPUT?=coverage.xml
COVERAGE_HTML_DIR?=cover

default:
	python setup.py check build

.PHONY: venv setup clean teardown lint test package

$(VENV_ACTIVATE): requirements.txt requirements-dev.txt
	test -f $@ || virtualenv --python=python2.7 $(VENV_DIR)
	$(WITH_VENV) pip install --no-deps -r requirements.txt
	$(WITH_VENV) pip install --no-deps -r requirements-dev.txt
	touch $@

venv: $(VENV_ACTIVATE)

setup: venv

clean:
	python setup.py clean
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg*/
	rm -rf __pycache__/
	rm -f MANIFEST
	rm -f $(TEST_OUTPUT)
	rm -f .coverage
	rm -f $(COVERAGE_OUTPUT)
	rm -rf $(COVERAGE_HTML_DIR)
	find ./ -type f -name '*.pyc' -delete

teardown:
	rm -rf $(VENV_DIR)/

lint: venv
	$(WITH_VENV) flake8 $(PACKAGE_NAME)/

test: venv
	$(WITH_VENV) nosetests -c tests/nose.cfg \
		--with-doctest \
		--with-xunit --xunit-file=$(TEST_OUTPUT) \
		--logging-filter=-factory

.PHONY: coverage
coverage: venv
	${WITH_VENV} nosetests -c tests/nose.cfg \
		--with-doctest \
		--with-coverage \
		--cover-html \
		--cover-html-dir=${COVERAGE_HTML_DIR} \
		--cover-xml \
		--cover-xml-file=${COVERAGE_OUTPUT} \
		--cover-package=${PACKAGE_NAME}

package:
	python setup.py sdist

install:
	$(WITH_VENV) python setup.py install
