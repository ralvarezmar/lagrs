#!/bin/bash
cat /tmp/delta_hosts >> /etc/hosts
chown juan:juan /home/juan -R
chmod 700 /home/juan/.ssh
chmod 600 /home/juan/.ssh/*
su - juan
/bin/bash
