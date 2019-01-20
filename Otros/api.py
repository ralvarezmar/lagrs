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
import requests
from apixu.client import ApixuClient, ApixuException



API_KEY = '16053badc204426a9b2113255192001'
DIRECTORIOS=  ["~/lagrs/practica01", "~/lagrs/practica02","~/lagrs/practica03"]
MAX_TAMANIO= 5
MAX_FICHEROS= 20
ID_USUARIO=727281131
TOKEN_NAME= "./token.txt"

usage = "%prog [-f --force-telegram]"
parser = OptionParser(usage)
parser.add_option("-f","--force-telegram",
action="store_true",dest="force",
help="Forzar mensaje")
options,args = parser.parse_args()

def getCurrentWeather():
    client = ApixuClient(API_KEY)
    current = client.getCurrentWeather(q='Madrid')
    return current

def getNextDays():
    client = ApixuClient(API_KEY)
    next = client.getForecastWeather(q='Madrid',days='1')
    return next

def getInfo():
    response = requests.get("http://api.open-notify.org/iss-pass")

    return response

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
    info = getCurrentWeather()
    print info
    info = getNextDays()
    print "Next days: " , info
    # bot.sendMessage(ID_USUARIO,"Envia maquina " + machine + ": " + check)

if __name__ == "__main__":
    main()
