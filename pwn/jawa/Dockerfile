FROM ubuntu:22.04

ENV DEBIAN_FRONTEND noninteractive

# Update the package list and install dependencies
RUN apt-get update --fix-missing && apt-get -y upgrade
RUN apt-get install -y wget tar xinetd


# Unduh dan instal JDK 22
RUN wget https://download.oracle.com/java/22/latest/jdk-22_linux-x64_bin.deb -P /tmp \
    && apt-get update \
    && apt-get install -y /tmp/jdk-22_linux-x64_bin.deb \
    && rm /tmp/jdk-22_linux-x64_bin.deb

# Atur JAVA_HOME dan PATH
ENV JAVA_HOME=/usr/lib/jvm/jdk-22
ENV PATH="${JAVA_HOME}/bin:${PATH}"

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
