#!/bin/sh

docker rm --force db-aline
docker rm --force db-adminer
docker rm --force ms-bank
docker rm --force ms-gateway
docker rm --force ms-underwriter
docker rm --force ms-user
docker rm --force ms-transaction

yes | docker image prune -a
