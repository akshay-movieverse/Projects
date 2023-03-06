FROM python:3

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

WORKDIR /app

ADD . /app

RUN pip install --upgrade pip
COPY ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY . /app