#!/bin/sh

docker container ls --format "table {{.Ports}}\t{{.Names}}" -a | grep '\->' > /home/drew/dev/docker/ports/ports.txt
