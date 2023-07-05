FROM python:3.11-slim-buster

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

ENTRYPOINT [ "./docker-entrypoint.sh" ]