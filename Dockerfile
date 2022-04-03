# syntax=docker/dockerfile:1
FROM python:3.8

WORKDIR /weatherserv

RUN pip install pipenv
COPY  Pipfile Pipfile.lock /weatherserv/
RUN pipenv install --system

COPY . /weatherserv/
EXPOSE 8080
ENTRYPOINT [ "python3.8", "pyserv2.py"]