## Choose from https://hub.docker.com/_/python/tags?page=1&name=3.9.14
FROM python:3.9.14-alpine

COPY requirements.txt /
RUN pip3 install -r requirements.txt

COPY . /app
WORKDIR /app

ENTRYPOINT [ "./gunicorn.sh" ]