#!/bin/bash

set GOMAXPROCS=4

mtredisalize                               \
  -host=172.16.1.60                          \
  -interleaved=true                        \
  -change-url=http://localhost:8808/update \
  -change-duration=10s                     \
  /config/.minetest/worlds/world/map.db &
#mtseeder              \
#  -colors=/config/.minetest/colors.txt \
#  -output-dir=/config/.minetest/worlds/world/map.db    \
#  -workers=3 && \
mtwebmapper           \
  -colors=/config/.minetest/colors.txt \
  -web-host=""                     \
  -map=/config/.minetest/worlds/world/map.db           \
  -web=/config/web    \
  -redis-host=172.16.1.60            \
  -workers=2                       \
  -websockets=true \
  -players=/tmp/mt_players_fifo


