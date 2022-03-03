#!/bin/sh

cd ..
cd services/backend

for d in */ ; do
    cd $d
    mvn -B -DskipTests clean install
    cd ..
done

