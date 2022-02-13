# PortainerPractice
Portainer practice repo

SETUP: 

* MAKE SURE MAVEN AND JAVA ARE INSTALLED LOCALLY

1. Replace 'your-microservice-repo' dir with your microservice repo

2. Copy the Docker and docker-compose.yaml files into the root of your microservices dir

3. Create an 'init' dir in the same root dir

4. Run 'mvn clean install' in root dir

5. Replace .jar file in Dockerfile lines 2 and 3

_______________________________________________________________________________

1. https://docs.fuga.cloud/how-to-install-portainer-docker-ui-manager-on-ubuntu-20.04-18.04-16.04

2. https://docs.portainer.io/v/ce-2.11/start/upgrade/docker
* UPDATE ENV NAME AND IP PER IMAGE 1

3. Make new dirs / create docker-compose files for app and db
https://nginxproxymanager.com/setup/#running-the-app

4. Update app template lists

App Template:
https://www.youtube.com/watch?v=B2SJGyJCK7I

Self Hosted:
https://raw.githubusercontent.com/SelfhostedPro/selfhosted_templates/master/Template/portainer-v2.json

DEFAULT:
https://raw.githubusercontent.com/portainer/templates/master/templates-2.0.json

5. Setup Custom DNS / SSL To Apps On Portainer
https://www.reddit.com/r/selfhosted/comments/icwvox/super_simple_cloudflare_and_nginx_proxy_manager/

6. Review "Stacks" page form image 2

7. Deploy Jenkins + Sonarqube + Terraform 
https://funnelgarden.com/sonarqube-jenkins-docker/

8. Setup Terraform Pipeline 
 https://youtu.be/qFjGqPw1NUY


gitkey:
****************************

S3 bucket:
jenkins-terraform-cicd

9. Deploy Springboot Mocroservice using Terraform

https://youtu.be/J2YhWG994Iw

https://youtu.be/jHjN5pzIMC4

______________________________

https://techdozo.dev/restful-microservices-with-spring-boot-and-kubernetes/

https://techdozo.dev/deploying-a-restful-spring-boot-microservice-on-kubernetes/

10. Populate Dummy Data 

https://onexlab-io.medium.com/docker-compose-mysql-entry-point-fa6335346791