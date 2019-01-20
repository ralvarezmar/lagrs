#!/usr/bin/env python
# -*- coding: utf-8 -*-
import telepot
import telepot.namedtuple
import time
import subprocess
import os
import sys
from optparse import OptionParser
from datetime import datetime
from telepot.loop import MessageLoop as ml

DIRECTORIOS=  ["~/lagrs/practica01", "~/lagrs/practica02","~/lagrs/practica03"]
MAX_TAMANIO= 5
MAX_FICHEROS= 20
ID_USUARIO=727281131
TOKEN_NAME= "/home/alumnos/rmartin/lagrs/practica03/token.txt"

usage = "%prog [-f --force-telegram]"
parser = OptionParser(usage)
parser.add_option("-f","--force-telegram",
action="store_true",dest="force",
help="Forzar mensaje")
options,args = parser.parse_args()

def watchPath():
    error=""
    for file in DIRECTORIOS:
        path = file.replace("~",os.path.expanduser("~"))
        statinfo = os.stat(path)
        numFiles= len([name for name in os.listdir(path) if os.path.isfile(os.path.join(path, name))])
        if statinfo.st_size>MAX_TAMANIO*1024:
            error+="Problema en path " + path + " con el tamaño\n\n"
        if numFiles>MAX_FICHEROS:
            error+="Problema en path: " + path + " con el numero de ficheros\n\n"
    return error

def getToken():
    if not os.path.isfile(TOKEN_NAME):
        sys.stderr.write("Fichero de token no existente\n")
        sys.exit(1)
    file = open(TOKEN_NAME,"r")
    statinfo=os.stat(TOKEN_NAME)
    token=file.read(statinfo.st_size)#Lectura de token
    file.close()
    return token

def main():
    token = getToken()
    bot = telepot.Bot(token)
    check = watchPath()
    machine = os.uname()[1]
    if check:
        bot.sendMessage(ID_USUARIO,"Envia maquina " + machine + ": " + check)
    elif options.force:
        bot.sendMessage(ID_USUARIO,"Envia maquina " + machine + ": archivos OK")
if __name__ == "__main__":
    main()
