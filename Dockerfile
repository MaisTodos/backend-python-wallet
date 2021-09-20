# pull the official base image
FROM python:3.8.3-alpine

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install some packages
RUN apk add --no-cache bash mariadb-dev mariadb-client python3-dev build-base

# set work directory
WORKDIR /code

# install dependencies
RUN pip install --upgrade pip 
COPY ./requirements.txt /code/
RUN pip install -r requirements.txt

# copy project
COPY . /code/

# RUN adduser -D samplemed
# USER samplemed