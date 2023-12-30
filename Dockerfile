FROM python:3.11.6-slim as builder

RUN apt update && apt install gcc -y

WORKDIR /app
COPY . /app
RUN pip3 install --no-cache-dir pipenv==2023.11.15

RUN python3 -m venv /app/.venv
RUN PIPENV_VERBOSITY=-1 pipenv install --deploy $(test "$PIP_ENV" = "production" || echo "--dev")

FROM python:3.11.6-slim

RUN apt update && apt install gcc -y

WORKDIR /app

WORKDIR /app
COPY . /app
RUN pip3 install --no-cache-dir pipenv==2023.11.15

RUN python3 -m venv /app/.venv
RUN PIPENV_VERBOSITY=-1 pipenv install --deploy $(test "$PIP_ENV" = "production" || echo "--dev")

