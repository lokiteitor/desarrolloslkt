FROM golang:alpine

MAINTAINER lokiteitor <lokiteitor513@gmail.com>

RUN apk update && apk add --no-cache --virtual=build-dependencies \
    --repository http://nl.alpinelinux.org/alpine/edge/testing \
    leveldb-dev \
    mercurial \
    git \
    cmake \
    g++ \
    gcc \
    make \
    sqlite-dev \
    leveldb \
    bash
    

RUN go get -u bitbucket.org/s_l_teichmann/mtsatellite/cmd/mtdbconverter

RUN go get -u bitbucket.org/s_l_teichmann/mtsatellite/cmd/mtredisalize

RUN go get -u bitbucket.org/s_l_teichmann/mtsatellite/cmd/mtseeder

RUN go get -u bitbucket.org/s_l_teichmann/mtsatellite/cmd/mtwebmapper

RUN mkdir /config

RUN mkfifo /tmp/mt_players_fifo

VOLUME /config

EXPOSE 6379
EXPOSE 8808

COPY mtsatellite.sh /usr/local/bin

ENV GOMAXPROCS=4

CMD ["mtsatellite.sh"] 


