FROM python:3.11.6-slim as builder

RUN apt-get update

RUN pip install pip

WORKDIR /app

COPY . /app

FROM python:3.11.6-slim

RUN apt-get update

WORKDIR /app

