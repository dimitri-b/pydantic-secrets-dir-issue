# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /

RUN mkdir "/project"
COPY . "/project"
RUN pip3 install -r /project/requirements.txt

RUN mkdir "/secrets-at-root"
RUN echo "contents-of-secret-AT-ROOT" > "secrets-at-root/SECRET_VAR"
RUN echo "NORMAL_VAR=bar" > "/.env"

