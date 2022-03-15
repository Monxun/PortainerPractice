#!/bin/sh

kubectl run -it --rm --image=mysql:latest --restart=Never mysql-client -- mysql -h db-aline -proot --namespace=dev
create database alinedb;
create user 'alinedb' identified by 'alinedb';
grant all privileges on alinedb . * to 'alinedb';
flush privileges;