# Flask-Appbuilder demo

Simple demo using Flask-AppBuilder python framework

## Using venv

```bash

# Creating venv
> python -m venv venv

# Activating venv
> source venv/bin/activate

# Installing deps from requeriments.txt
> python -m pip install -r requeriments.txt

# Leave venv
> deactivate

```

### [More about Python venvs here](https://realpython.com/python-virtual-environments-a-primer/)

## Starting with Flask-AppBuilder (F.A.B)

```bash

# Creating the app
> flask fab create-app

# Creating admin module
> cd <new-app-name>
> export FLASK_APP=app
> flask fab create-admin



```