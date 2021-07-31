FROM python:3.9 as base

EXPOSE 5000

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python



WORKDIR /srv/www/
ENV PATH="/root/.poetry/bin/:/srv/www/.venv/bin:/srv/www/todo_app/:${PATH}" 

COPY ./poetry.toml .
COPY ./pyproject.toml .
COPY ./todo_app ./todo_app
RUN ~/.poetry/bin/poetry install
WORKDIR /srv/www/todo_app

from base as production
ENTRYPOINT gunicorn --bind 0.0.0.0:5000 app:app

from base as development
ENTRYPOINT poetry run flask run -h 0.0.0.0
