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

# CI PIPELINE
-- checkout
-- test
-- int
-- static code
-- build
-- store artifact

# Create Jenkins Agent(example):

    docker run -d --name AGENT1 jenkinsci/jnlp-slave -url http://137.184.81.181:8090 0cc235eb36d3213d410fd35ac43edf77d9e10a81fdd676749bddbdf7a64a07b1 AGENT1

# CD PIPELINE
-- playbook
-- terraform
-- kubernetes
-- test
