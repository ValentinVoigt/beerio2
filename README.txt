O2 Getränkeverkauf
==================

Technologies
------------

Backend:
- WTForms + WTForms-Alchemy
- factory_boy + Faker

Frontend:
- Bootstrap
- Angular / React?
- npm with nodeenv
  -> pip install nodeenv
  -> nodeenv -p
- Webpack
- Font Awesome

Getting Started
---------------

- Change directory into your newly created project.

    cd beerio2

- Create a Python virtual environment.

    python3 -m venv env

- Enter der virtual environment

    source en/bin/activate

- Upgrade packaging tools.

    pip install --upgrade pip setuptools

- Install the project in editable mode with its testing requirements.

    pip install -e ".[testing]"

- Install NodeJS environment inside your virtualenv

    nodeenv -p

- Configure the database.

    initialize_beerio2_db development.ini

- Run your project's tests.

    pytest

- Run your project.

    pserve development.ini
