FROM python:3.7

ENV HELLO=1

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

COPY main.py /app

