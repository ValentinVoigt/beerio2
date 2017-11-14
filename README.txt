O2 Getränkeverkauf
==================

Technologies
------------

- WTForms + WTForms-Alchemy
- factory_boy + Faker
- npm
- Bootstrap
- Angular / React?

Getting Started
---------------

- Change directory into your newly created project.

    cd beverages

- Create a Python virtual environment.

    python3 -m venv env

- Upgrade packaging tools.

    env/bin/pip install --upgrade pip setuptools

- Install the project in editable mode with its testing requirements.

    env/bin/pip install -e ".[testing]"

- Configure the database.

    env/bin/initialize_beverages_db development.ini

- Run your project's tests.

    env/bin/pytest

- Run your project.

    env/bin/pserve development.ini
