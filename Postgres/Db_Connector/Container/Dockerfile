FROM python:3.10-alpine3.18

RUN apk add --no-cache \
    build-base \
    postgresql-client \
    postgresql-dev
COPY requirements.txt /requirements.txt
RUN python3 -m pip install -r /requirements.txt
RUN mkdir /api
#COPY *.py /db_connector/
WORKDIR /db_connector
ENTRYPOINT ["python3", "main.py"]