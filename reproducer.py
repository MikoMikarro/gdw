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
			new_t = time.clock()-t
			h = new_t//3600
			m = (new_t-h*3600)//60
			s = round(new_t-h*3600-m*60)
			print "Time transcurred: ",h," h ",m," m ",s," s"
		except UnicodeDecodeError:
			print('Error ascii no arquivo: "'+str(split(split(i,"/")[0],".")[0])+'" de '+str(split(i,"/")[2]))
		except KeyboardInterrupt:
			print("saindo...")
			quit()
