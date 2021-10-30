# syntax=docker/dockerfile:1
FROM python:3.9

ENV PYTHONUNBUFFERED=1

RUN mkdir /pages_content

WORKDIR /pages_content

COPY requirements.txt /pages_content/

RUN pip install -r requirements.txt

COPY . /pages_content/

