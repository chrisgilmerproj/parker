[![Build Status](https://travis-ci.org/chrisgilmerproj/parker.svg?branch=master)](https://travis-ci.org/chrisgilmerproj/parker) 
[![Coverage Status](https://coveralls.io/repos/github/chrisgilmerproj/parker/badge.svg?branch=master)](https://coveralls.io/github/chrisgilmerproj/parker?branch=master)
[![Documentation Status](https://readthedocs.org/projects/parker/badge/?version=latest)](http://parker.readthedocs.org/en/latest/?badge=latest)
[![LGPL License](https://img.shields.io/badge/license-LGPL-blue.svg)](https://github.com/chrisgilmerproj/parker/blob/master/LICENSE)

# Parker

This is a library to help me understand music theory and build useful studying
tools for my music courses.  I am aiming at two things:

- Ease of use in constructing tools
- Completion of music theory

# Make Commands

There are several commands in the makefile for convenience.  You can list them
by typing `make` or `make help`.

## Testing Locally

Easy to test.  Simply run `make test`.

This project uses Tox to test.  You will need to have python 2.7 and python 3.5
available to run the tests.

## Packaging

Packaging is done with `make package`.

## Linting

Style is important.  Check with `make lint`.

# Documentation

Change to the `docs` directory.  Then do the following:

```sh
$ cd docs/
$ virtualenv .venv
$ source .venv/bin/activate
(.venv) $ pip install -r requirements.txt
(.venv) $ pip install -r requirements-local.txt --upgrade
(.venv) $ make html
(.venv) $ open build/index.html
```

It's important that the current version of the library be installed in order
to generate the API docs.  To insure this insure to install from
`requirements-local.txt` with the `--upgrade` flag every time.  Example:

```sh
$ source .venv/bin/activate
(.venv) $ pip install -r requirements-local.txt --upgrade
(.venv) $ make html
```

# Credit

This began as a reconstruction of work from another library so I could get a
handle on music theory in python. Credit is due to the original author `bspaans`:

https://github.com/bspaans/python-mingus/tree/mingus-oo/mingus
