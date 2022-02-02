FROM python:3.9.9-slim

RUN pip install -U pip \
    pip install django==3.* celery[redis] psycopg2-binary

WORKDIR /app

ENTRYPOINT ["bash"]
