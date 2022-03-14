#!/bin/sh

cd ..

for d in */ ; do
    cd $d
    mvn -B -DskipTests clean install
    cd ..
done

cd scripts