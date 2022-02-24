#!/bin/sh

cd ..
cd ./frontend

docker-compose -f docker-compose.fe.yml down -d --rmi 'all'