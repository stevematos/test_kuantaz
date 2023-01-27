# syntax=docker/dockerfile:1
FROM python:3.9-slim-buster

WORKDIR /home/app

ENV VAR1=10

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1


RUN apt-get update \
    && apt-get -y install libpq-dev gcc

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements-docker.txt /home/app/requirements.txt
RUN pip install -r requirements.txt

COPY . /home/app/

# run entrypoint.sh
ENTRYPOINT ["chmod", "+x", "/home/app/entrypoint.sh"]

ENTRYPOINT [ "python" ]
CMD [ "main.py" ]
