#!/bin/sh

cd ..
cd ./backend

docker-compose -f docker-compose.ms.yml down --rmi 'all'