import random
from random import shuffle
import string
from string import split
from sys import executable
from subprocess import Popen, CREATE_NEW_CONSOLE

def ex():
    file = open("albumes.txt","r")
    data = file.readlines()
    file.close()
    while True:
        num = 0
        print("Albumes disponhibles")
        for i in data[1:]:
            print num," ",i
            num+=1
        ans = input()
        if ans <= num:
            alb_name == data[ans]
            break
        else:
            print "Album non anhadido"
    file = open("audio_data.txt","r")
    data = file.readlines()
    file.close()
    sng_list = []
    for i in data[:-1]:
        if split(i,"/")[1] == alb_name:
            sng_list.append(i)
    shuffle(sng_list)
    text = ""
    for i in sng_list:
        text  = (text+split(i,"/")[0]+"/"+split(i,"/")[1]+"/"+split(i,"/")[2]+"/"+split(i,"/")[3])
    file = open("audio_list.txt","w")
    file.write(text)
    file.close()
    Popen('python reproducer.py', creationflags=CREATE_NEW_CONSOLE)
    return ("Reproducir album - "+alb_name)
