FROM ubuntu:18.04
RUN apt-get update && apt-get upgrade -y && apt-get install -y libnet-ifconfig-wrapper-perl iputils-ping ssh
COPY ./delta_hosts /tmp/
COPY entrypoint.sh /
EXPOSE 22
ENTRYPOINT ["/entrypoint.sh"]
