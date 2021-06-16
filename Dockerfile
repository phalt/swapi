# syntax=docker/dockerfile:1
FROM python:2
ENV PYTHONUNBUFFERED=1
RUN apt-get update && apt-get install -y libmemcached-dev
WORKDIR /code
COPY . /code/
RUN pip install -r requirements.txt
CMD ["sh", "-c", "./run.sh"]
