#!/bin/sh

# RUN FROM CONTAINER HOST SERVER (Where portainer is)

docker run -d --name AGENT1 jenkinsci/jnlp-slave -url http://137.184.81.181:8090 0cc235eb36d3213d410fd35ac43edf77d9e10a81fdd676749bddbdf7a64a07b1 AGENT1

# ADD CONTAINER TO cicd-cicd NETWORK IN PORTAINER
