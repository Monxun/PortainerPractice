#!/bin/sh

cd ..

docker network create aline

docker-compose -f docker-compose.db.yml up -d