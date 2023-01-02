FROM python:3.10.9-alpine3.17

WORKDIR /app 

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update \
    && apk add --no-cache --update gcc bash \
    python3-dev mariadb-dev gfortran musl-dev \
    g++ libffi-dev openssl-dev libxml2 libxml2-dev  \
    libxslt libxslt-dev libjpeg-turbo-dev zlib-dev \
    jpeg-dev libjpeg tesseract-ocr py3-numpy make

RUN python3 -m ensurepip
RUN pip3 install --no-cache --upgrade pip setuptools wheel

COPY requirements.txt /app
RUN pip3 install -r requirements.txt --no-cache-dir

COPY . /app

EXPOSE 8000