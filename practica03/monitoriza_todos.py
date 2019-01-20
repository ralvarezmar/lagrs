
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import subprocess
import os
import sys

MAQUINAS = ["alpha", "beta","gamma"]
COMANDOS = ["touch /tmp/log_monitoriza_rmartin.txt" , "~/lagrs/practica03/monitor.py --force-telegram"]

def doPing(host):
    defaultPing = "ping -c 1 -W 1 "
    ping = defaultPing+host
    return os.system(ping+"> /dev/null")

def doComands(maquina):
    for cmd in COMANDOS:
        cmd = cmd.replace("~",os.path.expanduser("~"))
        cmd = "ssh "+maquina + " " + cmd
        reply=subprocess.check_output(cmd.split())

def main():
    for pc in MAQUINAS:
        if not doPing(pc):
            doComands(pc)

if __name__ == "__main__":
    main()
