# syntax=docker/dockerfile:1

FROM docker.io/library/python:3

RUN python -m pip install --upgrade pip

RUN groupadd --gid 1000 devs && useradd --create-home --uid 1000 --gid 1000 dev

USER dev

RUN pip install pipenv

COPY . /home/dev/app

WORKDIR /home/dev/app

RUN pipenv install

CMD [ "pipenv", "run", "python", "job.py" ]
