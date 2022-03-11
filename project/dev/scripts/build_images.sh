#!/bin/bash

cd ..
cd ..
cd apps
docker-compose -f docker-compose.db.yml build
docker-compose -f docker-compose.ms.yml build
# docker-compose -f docker-compose.fe.yml build
docker-compose -f docker-compose.ci.yml build
# docker-compose -f docker-compose.cd.yml build
