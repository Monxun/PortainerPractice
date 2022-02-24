#!/bin/sh

cd ..
cd ./db

docker-compose -f docker-compose.db.yml down -d --rmi 'all'