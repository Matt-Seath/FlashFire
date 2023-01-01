FROM python:3.7-alpine3.17

WORKDIR /app 

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update \
    && apk add --no-cache --update gcc python3 \
    python3-dev mariadb-dev gfortran musl-dev  \
    g++ libffi-dev openssl-dev libxml2 libxml2-dev  \
    libxslt libxslt-dev libjpeg-turbo-dev zlib-dev

RUN pip install pip==22.3.1 wheel==0.38.4

COPY requirements.txt /app
RUN pip install -r requirements.txt --no-cache-dir

RUN apk del gcc fortran musl-dev  \
    g++ libffi-dev openssl-dev libxml2 libxml2-dev  \
    libxslt libxslt-dev libjpeg-turbo-dev zlib-dev

COPY . /app

EXPOSE 8000