FROM python:3.10

WORKDIR /usr/src/app

COPY ./requirements.txt /requirements.txt

RUN apt-get update \
    && apt-get install gcc -y \
    && apt-get clean

RUN pip install --no-cache-dir --upgrade -r /requirements.txt