[![Build Status](https://travis-ci.org/chrisgilmerproj/parker.svg?branch=master)](https://travis-ci.org/chrisgilmerproj/parker)

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

# Credit

This began as a reconstruction of work from another library so I could get a
handle on music theory in python. Credit is due to the original author `bspaans`:

https://github.com/bspaans/python-mingus/tree/mingus-oo/mingus
