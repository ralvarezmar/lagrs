FROM ubuntu:18.04
RUN apt-get update && apt-get install -y openssh-server net-tools \
libnet-ifconfig-wrapper-perl \
iputils-ping \
ssh
COPY delta_hosts /tmp/
RUN mkdir /var/run/sshd
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd
COPY entrypoint.sh /
RUN chmod +x /entrypoint.sh

EXPOSE 22
ENTRYPOINT ["/entrypoint.sh"]
