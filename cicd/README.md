

## How to deploy the stack:

The stack is tested on Docker 2.10 and Docker-compose 1.26, should works on earlier versions.

### Get started:
1. Build stack in root of cicd dir:

    docker-compose up

2. Then configure Jenkins + Sonarqube:
https://funnelgarden.com/sonarqube-jenkins-docker/

3. Setup Github / Terraform:
https://youtu.be/qFjGqPw1NUY

4. Create item to checkout git repo and build jarfile:
https://learn.smoothstack.com/component/splms/lesson/?id=585

pipeline visual @ 27:52

# PIPELINE
-- checkout
-- test
-- int
-- static code
-- build
-- store artifact

# Create Jenkins Agent:

    chmod +x agent.sh

    # agent.sh PLUS NAME FOLLOWED BY AGENT EXTERNAL PORT NUMBER
    ./agent.sh JA1 33 
