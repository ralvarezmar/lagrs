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
    print msg


    #bot.sendMessage(chat_id,"Mensaje recibido:  " + reply)
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
