# step 1:
    bash run.sh

Deploys the db and backend microservices

# step 2:
    bash cicd.sh

Deploys the producers as a container app to test endpoints

# step 3:
    sh destroy.sh

Destroys the db, backend microservices, and cicd containers + images