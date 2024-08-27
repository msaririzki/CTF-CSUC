FROM ubuntu:jammy

EXPOSE 6666

RUN apt update
RUN apt-get install -y socat

RUN mkdir /home/pwn
COPY flag.txt /home/pwn/flag.txt
COPY chall /home/pwn/chall
WORKDIR /home/pwn

RUN chmod -R 755 /home/pwn
RUN chmod 700 /usr/bin/* /bin/* /tmp /dev/shm
RUN chmod 755 /usr/bin/env /bin/dash /bin/bash /bin/sh /bin/cat /usr/bin/id /bin/ls

CMD socat TCP-LISTEN:6666,reuseaddr,fork EXEC:/home/pwn/chall,pty,echo=0,raw,iexten=0,su=nobody