#!/usr/bin/python -tt
# -*- codigo: utf-8 -*-

#Ruben Alvarez Martin
#rmartin
import os
import subprocess
import sys
def get_files():
    comando = "ls -l"
    cmd_token = comando.split()
    return subprocess.check_output(cmd_token)

def printlist(raw):
    files = raw.split("\n")
    files.pop()
    for file in files:
        if file[0]=='-':
            data = file.split()
            print data[4] + " " + data[8]

if __name__ == "__main__":
    raw_files = get_files()
    printlist(raw_files)
