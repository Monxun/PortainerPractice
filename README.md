# RUN APP

* RUN USING GITBASH OR LINUX TERMINAL (or WSL2)

Step 1:
   `cd project`

Step 2:
- BUILD ALL JARS:
   `bash build.sh`
  
- DEPLOY DB + MICROSERVICES:
   `bash deploy.sh`
   
- DEPLOY CICD/PRODUCERS 
   (run after verifying all services have started their tomcat servers first using docker desktop > logs):
   `bash cicd.sh`




# RUN CICD
