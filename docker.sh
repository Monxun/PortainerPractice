#!/bin/sh

# DOCKER
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

# DOCKER-COMPOSE
sudo curl -L https://github.com/docker/compose/releases/download/1.21.2/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
sudo docker volume create portainer_data

# PORTAINER
sudo docker run -d -p 9000:9000 -p 8000:8000 --name PORTAINER --restart always -v /var/run/docker.sock:/var/run/docker.sock -v /srv/portainer:/data portainer/portainer

