#!/bin/sh

cd ..
cd ./backend

docker-compose -f docker-compose.ms.yml down -d --rmi 'all'