#!/bin/bash

cd ..
cd kubernetes

# BUILD DB IMAGES
cd K8-db
docker-compose -f docker-compose.db.yml build
cd ..

# BUILD MS IMAGES
cd K8-ms
docker-compose -f docker-compose.ms.yml build
cd ..

# # BUILD FE IMAGES
cd K8-fe
# docker-compose -f docker-compose.fe.yml build
cd ..

# BUILD CI IMAGES
cd K8-ci
docker-compose -f docker-compose.ci.yml build
cd ..

# # BUILD CD IMAGES
cd K8-cd
# docker-compose -f docker-compose.cd.yml build
cd ..

cd ..
cd scripts
