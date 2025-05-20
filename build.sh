#!/bin/bash
set -e

# Clean old builds
rm -rf mods image

# Compile the module
javac -d mods/com.example.hello \
      src/com.example.hello/module-info.java \
      src/com.example.hello/Hello.java

# Create custom runtime using jlink
jlink --module-path $JAVA_HOME/jmods:mods \
      --add-modules com.example.hello \
      --output image \
      --launcher hello=com.example.hello/com.example.hello.Hello \
      --strip-debug --no-header-files --no-man-pages --compress=2


src/com.example.hello
Hello.java
package com.example.hello;

public class Hello {
    public static void main(String[] args) {
        System.out.println("Hello from jlink!");
    }
}

module-info.java 
module com.example.hello {
    requires java.base;
}
