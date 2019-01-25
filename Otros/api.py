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
import json
from apixu.client import ApixuClient, ApixuException


API_KEY = '16053badc204426a9b2113255192001'
DIRECTORIOS=  ["~/lagrs/practica01", "~/lagrs/practica02","~/lagrs/practica03"]
MAX_TAMANIO= 5
MAX_FICHEROS= 20
ID_USUARIO=727281131
TOKEN_NAME= "/home/alumnos/rmartin/lagrs/Otros/token.txt"

usage = "%prog [-f --force-telegram]"
parser = OptionParser(usage)
parser.add_option("-f","--force-telegram",
action="store_true",dest="force",
help="Forzar mensaje")
options,args = parser.parse_args()

def getCurrentWeather(city):
    client = ApixuClient(API_KEY)
    current = client.current(q=city)
    return current

def getNextDays(city,days):
    client = ApixuClient(API_KEY)
    next = client.forecast(q=city,days=days)
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

def formatData(info):
    message = []
    message.append("temperatura: " + str(info['current']['temp_c']) + " ºC")
    message.append("humedad: " + str(info['current']['humidity']))
    message.append("nubes: " + str(info['current']['cloud']))
    message.append("viento: " + str(info['current']['wind_kph']) + " km/h")
    message.append("posibilidad de lluvia: " + str(info['current']['precip_in']) + " %")
    message.append("dirección de viento: " + str(info['current']['wind_dir']))
    message.append("Info adicional: " + info['current']['condition']['text'])
    print message
    return message

def handler(msg):
    token = getToken()
    bot = telepot.Bot(token)
    chat_id = msg["chat"]["id"]
    texto = msg["text"]
    print "texto", texto
    comandos = texto.split()
    if(len(comandos)==1):
        info= getCurrentWeather(comandos[0])
        message = formatData(info)
        bot.sendMessage(ID_USUARIO,"Tiempo ahora mismo en " + info['location']['name'])
        for data in message:
            bot.sendMessage(ID_USUARIO,data)
    else:
        info = getNextDays(comandos[0],comandos[1])
        message = formatData(info)
        bot.sendMessage(ID_USUARIO,"Tiempo los proximos " + comandos[1] + " dias en " + info['location']['name'])
        for data in message:
            bot.sendMessage(ID_USUARIO,data)


def main():
    token = getToken()
    bot = telepot.Bot(token)
    if(len(sys.argv)>1):
        city = sys.argv[1]
        info = getCurrentWeather(city)
        message = formatData(info)
        bot.sendMessage(ID_USUARIO,"Tiempo ahora mismo en " + info['location']['name'])
        for data in message:
            bot.sendMessage(ID_USUARIO,data)
    else:
        ml(bot,handler).run_as_thread()
        while True:
            time.sleep(2)

if __name__ == "__main__":
    main()
