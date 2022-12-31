FROM python:3.10.9-alpine3.17

WORKDIR /app 

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add --no-cache mariadb-dev
RUN python -m pip install -U pip
RUN pip install --upgrade setuptools

COPY requirements.txt /app
RUN pip install -r requirements.txt --no-cache-dir
RUN apk del build-deps

COPY . /app

EXPOSE 8000