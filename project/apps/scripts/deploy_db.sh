#!/bin/sh

cd ..

docker network create --subnet=192.168.55.0/24 --gateway=192.168.55.1 aline 

docker-compose -f docker-compose.db.yml up -d
sleep 1m
docker build -t ms-underwriter -f ./dockerfiles/backend/Dockerfile.underwriter ./dockerfiles/backend
docker run -p 8071:8071 --env-file ./dockerfiles/backend/env/.env.underwriter --name=ms-underwriter --network=aline --ip=192.168.55.12 ms-underwriter
sleep 1m
