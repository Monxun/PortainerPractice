#!/bin/sh

cd ..

docker-compose -f docker-compose.ms.yml down --rmi 'all'