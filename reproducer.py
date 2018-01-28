#-*- coding : utf-8 -*-
from playsound import playsound


file = open('audio_list.txt','r')
data = file.readlines()
file.close()
paste = "C:/Users/lopez/OneDrive/Escritorio/Codigos/Gestordewebs/"
from string import split
while True:
	for i in data[0:-1]:
		# try:
		print('Reproduciendo: "'+str(split(split(i,"/")[0],".")[0])+'" de '+str(split(i,"/")[2]))
		playsound("songs/"+str(split(i,"/")[3][0:-1])+"/"+str(split(i,"/")[2])+"/"+str(split(i,"/")[1])+"/"+str(split(i,"/")[0]))
		# except:
		print('Error no arquivo: "'+str(split(split(i,"/")[0],".")[0])+'" de '+str(split(i,"/")[2]))
