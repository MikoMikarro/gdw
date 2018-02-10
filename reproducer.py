#-*- coding : utf-8 -*-
from playsound import playsound
import time

file = open('audio_list.txt','r')
data = file.readlines()
file.close()
from string import split
t = time.clock()
while True:
	for i in data[0:-1]:
		try:

			print('Reproduciendo: "'+str(split(split(i,"/")[0],".")[0])+'" de '+str(split(i,"/")[2]))
			playsound("songs/"+str(split(i,"/")[3][0:-1])+"/"+str(split(i,"/")[2])+"/"+str(split(i,"/")[1])+"/"+str(split(i,"/")[0]))
			if time > 3600:
				print "Time since session was started: ",(time.clock()-t)/3600," h"
			elif time > 60:
				print "Time since session was started: ",(time.clock()-t)/60," min"
			else:
				print "Time since session was started: ",time.clock()-t," s"
		except UnicodeDecodeError:
			print('Error ascii no arquivo: "'+str(split(split(i,"/")[0],".")[0])+'" de '+str(split(i,"/")[2]))
		except KeyboardInterrupt:
			print("saindo...")
			quit()
