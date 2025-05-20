FROM docker.io/openjdk:latest as build
COPY src /app/src/
COPY build.sh /app

WORKDIR /app

RUN bash ./build.sh

FROM docker.io/redhat/ubi9-micro:latest

ENV JAVA_HOME=/opt/jdk/jdk21
ENV PATH=$JAVA_HOME/bin:$PATH

# Copy the custom runtime image
COPY --from=build /app/image $JAVA_HOME
COPY --from=build /usr/lib64/libz.so.1.2.11 /usr/lib64/libz.so.1.2.11
RUN ln -s /usr/lib64/libz.so.1.2.11 /usr/lib64/libz.so.1

# Set entrypoint
ENTRYPOINT ["/opt/jdk/jdk21/bin/hello"]
