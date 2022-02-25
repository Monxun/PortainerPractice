#!/bin/sh

cd ..
cd services/backend

for d in */ ; do
    cd $d
    mvn -B -DskipTests clean install
    cd ..
done
cd ..
cd ..
find . -name '*.jar' -exec mv {} ./dockerfiles/backend/target \;
