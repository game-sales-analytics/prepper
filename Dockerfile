# syntax=docker/dockerfile:1

FROM docker.io/library/python:3-slim

RUN python -m pip install --upgrade pip

RUN addgroup -g 1000 devs && adduser -h /home/dev -u 1000 -D -G devs dev

RUN pip install pipenv

USER dev

COPY . /home/dev/app

WORKDIR /home/dev/app

RUN pipenv install

CMD [ "pipenv", "run", "python", "job.py" ]
