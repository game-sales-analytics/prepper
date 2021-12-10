# syntax=docker/dockerfile:1

FROM docker.io/library/python:3-slim

RUN python -m pip install --upgrade pip

RUN groupadd --gid 1000 dev && useradd --create-home --uid 1000 --gid dev dev

RUN pip install pipenv

USER dev

COPY --chown=dev:dev . /home/dev/app

WORKDIR /home/dev/app

RUN pipenv install

CMD [ "pipenv", "run", "python", "job.py" ]
