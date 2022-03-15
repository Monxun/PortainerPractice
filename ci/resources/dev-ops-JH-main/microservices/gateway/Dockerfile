# syntax=docker/dockerfile:1
FROM alpine

RUN apk update && \
    apk add openjdk17-jre
    
EXPOSE 8080

ENV APP_PORT=8080 \
    PORTAL_LANDING=0.0.0.0:4200 \
    PORTAL_DASHBOARD=0.0.0.0:3007 \
    PORTAL_ADMIN=0.0.0.0:3000 \
    DB_USERNAME=alinedb \
    DB_PASSWORD=alinedb \
    DB_HOST=mysql-db \
    DB_PORT=3306 \
    DB_NAME=alinedb \
    ENCRYPT_SECRET_KEY=cQfThWmZq4t7w!z%C*F-JaNdRgUkXn2r \
    JWT_SECRET_KEY=e6c51627-4938-4148-a962-aa27834db06d \
    APP_USER_ACCESS_KEY=something \
    APP_USER_SECRET_KEY=something

COPY . /app
WORKDIR /app

ENTRYPOINT ["java", "-jar", "aline-gateway-0.0.1-SNAPSHOT.jar"]
