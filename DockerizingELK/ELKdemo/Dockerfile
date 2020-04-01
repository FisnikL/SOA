FROM openjdk:8-jdk-alpine

COPY ./demo-0.0.1-SNAPSHOT.jar /usr/src/demo/

WORKDIR /usr/src

EXPOSE 8080

CMD ["java", "-jar", "demo/demo-0.0.1-SNAPSHOT.jar"]