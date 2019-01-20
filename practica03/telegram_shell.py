#!/usr/bin/env python
# -*- coding: utf-8 -*-
import telepot
import telepot.namedtuple
import time
import subprocess
import os
import sys
from datetime import datetime
from telepot.loop import MessageLoop as ml

TOKEN_NAME= "./shelltoken"
def getToken():
    if not os.path.isfile(TOKEN_NAME):
        sys.stderr.write("Fichero de token no existente\n")
        sys.exit(1)

    file = open(TOKEN_NAME,"r")
    statinfo=os.stat(TOKEN_NAME)
    token=file.read(statinfo.st_size - 1)
    file.close()
    return token

def handler(msg):
    token = getToken()
    bot = telepot.Bot(token)
    chat_id = msg["chat"]["id"]
    texto = msg["text"]
    print "---------------MENSAJE RECIBIDO---------------"
    for key in msg:
        if(key=="date"):
            print key + ":",
            print(datetime.utcfromtimestamp(float(msg[key])).strftime('%Y-%m-%d %H:%M:%S'))
        elif(key=="from" or key=="chat"):
            for value in msg[key]:
                print value + ":",
                print msg[key][value],
        else:
            print key + ":",
            print msg[key]
    minuscula=texto.lower()
    comando=minuscula[0]+texto[1:]
    cmd_token = comando.split()
    reply = subprocess.check_output(cmd_token)
    bot.sendMessage(chat_id,reply)
    print "\n-------------------------------------------------"
    return

def main():
    token = getToken()
    bot = telepot.Bot(token)
    ml(bot,handler).run_as_thread()
    id_usuario= "727281131"
    print ".....Conectado....."
    while True:
        time.sleep(5)
    return

if __name__ == "__main__":
    main()
