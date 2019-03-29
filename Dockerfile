FROM python:2.7 
RUN apt-get update \
  && apt-get install -y postgresql postgresql-contrib build-essential libmemcached-dev zlib1g-dev \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN mkdir /swapi
WORKDIR /swapi
COPY . /swapi

#RUN apk add --update alpine-sdk
#RUN apk add --no-cache postgresql-libs postgresql-dev

RUN make install \
  && make build \
  && make load_data

CMD [ "make", "serve"]