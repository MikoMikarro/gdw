import random
from random import shuffle
import string
from string import split
from sys import executable
from subprocess import Popen, CREATE_NEW_CONSOLE

def ex(filter):
    if filter == "author":
        file_name = "authors.txt"
        txt_intro = "Autores"
        id = 2
    if filter == "genre":
        file_name = "genres.txt"
        txt_intro = "Xeneros"
        id = 3
    if filter == "album":
        file_name = "albumes.txt"
        txt_intro = "Albumes"
        id = 1
    if filter == "all":
        file_name = "audio_data.txt"
    file = open(file_name,"r")
    data = file.readlines()
    file.close()
    if filter != "all":
        while True:
            num = 0
            print(txt_intro+" disponhibles")
            for i in data[1:]:
                if filter != "genre":
                    print num," ",split(i,"/")[0]
                else:
                    print num," ",i[:-1]
                num+=1
            ans = input()
            if ans <= num:
                if filter != "genre":
                    filt_name = split(data[1:][ans],"/")[0]
                else:
                    filt_name = data[1:][ans]
                break
            else:
                print txt_intro," non anhadido"
    file = open("audio_data.txt","r")
    data = file.readlines()
    file.close()
    sng_list = []
    if filter != "all":
        for i in data[:-1]:
            if split(i,"/")[id] == filt_name:
                sng_list.append(i)
    else:
        for i in data[:-1]:
            sng_list.append(i)
    shuffle(sng_list)
    text = ""
    for i in sng_list:
        text  = (text+split(i,"/")[0]+"/"+split(i,"/")[1]+"/"+split(i,"/")[2]+"/"+split(i,"/")[3])
    file = open("audio_list.txt","w")
    file.write(text)
    file.close()
    Popen('python reproducer.py', creationflags=CREATE_NEW_CONSOLE)
    if filter != "all":
        return ("Reproducir por "+txt_intro+" "+filt_name)
    else:
        return ("Reproducir todo")
