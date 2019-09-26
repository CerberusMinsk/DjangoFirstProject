FROM python:3
MAINTAINER cerberus.minsk

ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
COPY ./code /code