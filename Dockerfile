## Choose from https://hub.docker.com/_/python/tags?page=1&name=3.9.14
FROM python:3.9.14-alpine

COPY requirements.txt /
RUN  /usr/local/bin/python -m pip install --upgrade pip > /dev/null 2>&1 && pip install --root-user-action=ignore -r requirements.txt

COPY . /app
WORKDIR /app

ENTRYPOINT [ "./gunicorn.sh" ]