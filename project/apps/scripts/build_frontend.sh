#!/bin/sh

cd ..

cd ./frontend

for d in */ ; do
    cd $d
    mvn -B -DskipTests clean install
    cd ..
done