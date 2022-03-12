#!/bin/bash

cd ..
cd ..
cd apps
docker-compose -f docker-compose.db.yml build
docker-compose -f docker-compose.ms.yml build
# docker-compose -f docker-compose.fe.yml build
docker-compose -f docker-compose.ci.yml build
# docker-compose -f docker-compose.cd.yml build

docker tag ms-bank:0.1 localhost:5001/ms-bank:01
docker push localhost:5001/ms-bank:01

docker tag ms-transaction:0.1 localhost:5001/ms-transaction:0.1
docker push localhost:5001/ms-transaction:0.1


docker tag ms-underwriter:0.1 localhost:5001/ms-underwriter:0.1
docker push localhost:5001/ms-underwriter:0.1


docker tag ms-user:0.1 localhost:5001/ms-user:0.1
docker push localhost:5001/ms-user:0.1


docker tag ms-gateway:0.1 localhost:5001/ms-gateway:0.1
docker push localhost:5001/ms-gateway:0.1
