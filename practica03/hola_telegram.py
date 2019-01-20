#!/usr/bin/env python
# -*- coding: utf-8 -*-
import telepot
import telepot.namedtuple
import time
from telepot.loop import MessageLoop as ml

file = open("token.txt","r")
TOKEN=file.read(45)
bot = telepot.Bot(TOKEN)

def handler(msg):
    chat_id = msg["chat"]["id"]
    texto = msg["text"]

    print "Recibiendo mensaje: "
    print msg

    respuesta = "Recibido: " + texto
    bot.sendMessage(chat_id,respuesta)
    return

def main():
    ml(bot,handler).run_as_thread()
    id_usuario= "727281131"
    bot.sendMessage(id_usuario, "Hola")
    print ".....Esperando mensajes...."
    while True:
        time.sleep(5)
    return

if __name__ == "__main__":
    main()
