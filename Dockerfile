
FROM python:3.9 as base

EXPOSE 5000

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
RUN mkdir /srv/www
WORKDIR /srv/www/
ENV PATH="/root/.poetry/bin/:/srv/www/.venv/bin:/srv/www/todo_app:${PATH}" 

COPY ./poetry.toml .
COPY ./pyproject.toml .
RUN ~/.poetry/bin/poetry install

from base as production 

COPY ./todo_app ./todo_app
WORKDIR /srv/www/todo_app

ENTRYPOINT gunicorn --bind 0.0.0.0:5000 app:app

from base as development
COPY ./requirements.txt /srv/www
WORKDIR /srv/www
RUN pip install -r requirements.txt
ENTRYPOINT ["/srv/www/todo_app/flaskwatch.sh"]


from base as test
#RUN apt-get update && apt-get install git && apt-get install nano
#WORKDIR /tmp
#RUN git clone --branch module7 https://github.com/lawrencemark/DevOps-Course-Starter
#RUN cp -R /tmp/DevOps-Course-Starter/* /srv/www
COPY ./requirements.txt .
RUN pip install -r requirements.txt
WORKDIR /srv/www/todo_app
ENTRYPOINT ["./flaskrun.sh"]

