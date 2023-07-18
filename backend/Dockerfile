FROM python:3.10.4-slim

# 1. Disable python process buffering
ENV PYTHONUNBUFFERD 1

# 2. Change working directory to /app/server
WORKDIR /app/server
ADD . /app/server

ARG DEV=false

# 3. Install MySQL and PostgreSQL dev tools
# RUN apt-get update && apt-get install gcc default-libmysqlclient-dev libpq-dev -y

RUN pip install --upgrade pip && pip install -r requirements.txt

CMD python manage.py runserver 0.0.0.0:8000
