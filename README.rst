Requirements
============

This is a template for quick setting up of new development projects. Change
description and project name accordignly
Template
=======================================


Preparing for Development
-------------------------

1. Ensure ``pip`` and ``pipenv`` are installed
2. Clone repository: ``git clone git@github.com:example/pgbackup``
3. ``cd`` into repository
4. Fetch development dependencies ``make install``
5. Activate virtualenv: ``pipenv shell``

Usage
-----


still to be defined.

::


::


Running Tests
-------------

Run tests locally using ``make`` if virtualenv is active:

::

    $ make

If virtualenv isn’t active then use:

::

    $ python run_tests.py $test_document.py test

