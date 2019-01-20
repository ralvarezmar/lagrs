FROM ubuntu:18.04
RUN apt-get update && apt-get upgrade -y && \
  apt-get install -y  openssh-server net-tools \
  libnet-ifconfig-wrapper-perl \
  iputils-ping \
  ssh \
  nano \
  locales  && \
  localedef -i es_ES -c -f UTF-8  \
  -A /usr/share/locale/locale.alias es_ES.UTF-8
ENV LANG es_ES.UTF-8

RUN useradd -d /home/juan -s /bin/bash juan
RUN mkdir /home/juan
RUN mkdir /home/juan/.ssh

RUN mkdir /var/run/sshd

RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

COPY delta_hosts /tmp/
COPY id_ed25519.pub /home/juan/.ssh/authorized_keys
COPY entrypoint.sh /

EXPOSE 22
ENTRYPOINT ["/entrypoint.sh"]
