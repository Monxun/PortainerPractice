# syntax=docker/dockerfile:1
FROM openjdk:latest

ENV APP_PORT=8080 \
    APP_SERVICE_HOST=0.0.0.0 \
    PORTAL_LANDING=0.0.0.0:4200 \
    PORTAL_DASHBOARD=0.0.0.0:3007 \
    PORTAL_ADMIN=0.0.0.0:3000

COPY . /app-gateway
WORKDIR /app-gateway

CMD ["java", "-jar", "aline-gateway-0.0.1-SNAPSHOT.jar"]