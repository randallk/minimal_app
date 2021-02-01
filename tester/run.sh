#!/bin/sh
IP=`ip route get 1 | cut -d' '  -f7`
docker run --rm --add-host webserver:${IP} tester
