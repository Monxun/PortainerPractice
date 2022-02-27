#!/bin/bash

cd apps

docker-compose -f docker-compose.db.yml up -d

sleep 1m

docker-compose -f docker-compose.ms.yml up -d