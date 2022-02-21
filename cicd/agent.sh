#!/bin/sh

ssh-keygen -N "" -f ~/.ssh/jenkins_agent_key

docker run -d --rm --name=agent1 -p $1:$1 \
-e "JENKINS_AGENT_SSH_PUBKEY=cat ~/.ssh/jenkins_agent_key" \
jenkins/ssh-agent:alpine

VARS1="HOME=|USER=|MAIL=|LC_ALL=|LS_COLORS=|LANG="
VARS2="HOSTNAME=|PWD=|TERM=|SHLVL=|LANGUAGE=|_="
VARS="${VARS1}|${VARS2}"
docker exec agent1 sh -c "env | egrep -v '^(${VARS})' >> /etc/environment"