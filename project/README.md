# RUN APP

RUN USING GITBASH OR LINUX TERMINAL (or WSL2)

Step 1:
   `cd project`

Step 2:
- BUILD ALL JARS:
   `bash build.sh`
  
- DEPLOY DB + MICROSERVICES:
   `bash deploy.sh`
   
- DEPLOY CICD/PRODUCERS 
   (run after verifying all services have started their tomcat servers first):
   `bash cicd.sh`
   
Step 3:
- Check database using adminer 
- Check docker desktop > apps > container_name > logs & inspect 

Step 4:
- DESTROY DB + MICROSERVICES + IMAGES:
   `bash destroy.sh`


# RUN CICD
