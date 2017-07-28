FROM armhf/debian:jessie
MAINTAINER David Delgado <lokiteitor513@gmail.com>

ENV HOME="/config"
ENV MINETEST_SUBGAME_PATH="/config/.minetest/games"

RUN apt-get -y update && apt-get -y install build-essential libirrlicht-dev cmake \
    libbz2-dev libpng-dev libjpeg-dev libxxf86vm-dev libgl1-mesa-dev \
    libsqlite3-dev libogg-dev libvorbis-dev libopenal-dev libcurl4-gnutls-dev \
    libfreetype6-dev zlib1g-dev libgmp-dev libjsoncpp-dev git  libluajit-5.1-dev \
    gettext luajit libhiredis-dev libspatialindex-dev doxygen libncurses5-dev libleveldb-dev

RUN apt-get -y autoremove && apt-get clean && rm -rf /var/lib/apt/lists/*

RUN git clone --depth 1 https://github.com/minetest/minetest.git 

RUN    cd minetest && cmake .  \
    -DBUILD_CLIENT=0 \
    -DBUILD_SERVER=1 \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DCUSTOM_BINDIR=/usr/bin \
    -DCUSTOM_DOCDIR="/usr/share/doc/minetest" \
    -DCUSTOM_SHAREDIR="/usr/share/minetest" \
    -DRUN_IN_PLACE=0 \
    -DENABLE_CURL=1 \
    -DENABLE_LEVELDB=1\
    -DENABLE_GETTEXT=1 \
    -DENABLE_LUAJIT=1 \
    -DENABLE_REDIS=1 \
    -DENABLE_SOUND=0 \
    -DENABLE_SYSTEM_GMP=1 \
    -DCMAKE_BUILD_TYPE="Release" \
    -DENABLE_CURSES=1 && \
    make -j 4 && \
    make install


VOLUME /config
VOLUME /usr/share/minetest/games

#ENTRYPOINT ["/bin/bash"]

EXPOSE 30000/udp

#CMD ["minetestserver"]

