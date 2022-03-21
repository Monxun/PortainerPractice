#!/bin/sh

kubectl run -it --rm --image=mysql:latest --restart=Never mysql-client -- mysql -h mysql-db -proot
create database alinedb;
create user 'alinedb' identified by 'alinedb';
grant all privileges on alinedb . * to 'alinedb';
flush privileges;