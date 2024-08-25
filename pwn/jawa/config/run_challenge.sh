#! /bin/bash
#!/bin/bash

# Set JAVA_HOME and PATH in the script
export JAVA_HOME=/opt/jdk-22
export PATH=${JAVA_HOME}/bin:$PATH

# Change directory and run the Java application
cd /home/ctf && java chall

