### Get started:
1. Build stack in root of cicd dir:

    docker-compose up

2. Then configure Jenkins + Sonarqube:
VIDEO:
https://www.youtube.com/watch?v=KsTMy0920go&list=PLvBBnHmZuNQJeznYL2F-MpZYBUeLIXYEe&index=60
ARTICLE:
https://funnelgarden.com/sonarqube-jenkins-docker/
https://dzone.com/articles/jenkins-pipeline-with-sonarqube-and-gitlab

A. Setup in Jenkins:
    cd /var/jenkins_home
    mkdir sonar-scanner
    cd sonar-scanner
    wget https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-3.3.0.1492-linux.zip
    unzip sonar-scanner-cli-3.3.0.1492-linux.zip


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

1. Setup Kind Cluster as Jenkins Node:
    curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.11.1/kind-darwin-amd64
    chmod +x ./kind
    mv ./kind /root
    nano jenkins-k8-config.yaml

Add to file: 

kind: Cluster
apiVersion: kind.x-k8s.io/v1alpha4
networking:
  apiServerAddress: "137.184.81.181"
  apiServerPort: 58444

    ctrl+x
    y
    enter

MAKE CLUSTER:

    kind create cluster --config jenkins-k8-config.yaml