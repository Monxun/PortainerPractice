FROM openjdk:latest
ADD ./user-microservice/target/user-microservice-0.1.0.jar user-microservice-0.1.0.jar
EXPOSE 8080
ENTRYPOINT ["java", "-jar", "user-microservice-0.1.0.jar"]