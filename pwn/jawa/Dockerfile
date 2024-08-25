FROM ubuntu:22.04

ENV DEBIAN_FRONTEND noninteractive

# Update the package list and install dependencies
RUN apt-get update --fix-missing && apt-get -y upgrade
RUN apt-get install -y openjdk-22-jre-headless xinetd

# Create ctf-user
RUN groupadd -r ctf && useradd -r -g ctf ctf
RUN mkdir /home/ctf

# Configuration files/scripts
ADD config/ctf.xinetd /etc/xinetd.d/ctf
ADD config/run_xinetd.sh /etc/run_xinetd.sh
ADD config/run_challenge.sh /home/ctf/run_challenge.sh

# Add the Java class files and other necessary files
ADD flag.txt /home/ctf/flag.txt
ADD release/chall.class /home/ctf/chall.class

# Set appropriate permissions
RUN chown -R root:ctf /home/ctf /home/ctf/flag.txt
RUN chmod 750 /home/ctf/chall.class
RUN chmod 750 /home/ctf/run_challenge.sh
RUN chmod 440 /home/ctf/flag.txt
RUN chmod 700 /etc/run_xinetd.sh

# Restart xinetd service
RUN service xinetd restart
