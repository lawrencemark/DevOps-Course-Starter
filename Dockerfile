FROM python:3.9 as base

EXPOSE 5000

from base as production

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python

WORKDIR /srv/www/
ENV PATH="/root/.poetry/bin/:/srv/www/.venv/bin:/srv/www/todo_app/:${PATH}" 

COPY ./poetry.toml .
COPY ./pyproject.toml .
RUN ~/.poetry/bin/poetry install
COPY ./todo_app ./todo_app
WORKDIR /srv/www/todo_app
ENTRYPOINT gunicorn --bind 0.0.0.0:5000 app:app

from base as development
# Poetry has been substituted in the development release - giving me a 
# giving me a headache due to my development setup (not Dockers fault)
WORKDIR /srv/www
COPY ./requirements.txt .
RUN  pip3 install -r requirements.txt
ENTRYPOINT flask run -h 0.0.0.0
