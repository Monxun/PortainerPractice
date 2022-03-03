step 1: 
    docker-compose -f docker-compose.db.yml up -d

step 2: 
    docker-compose -f docker-compose.ms.yml up -d

step 3: 
    docker-compose -f docker-compose.fe.yml up -d