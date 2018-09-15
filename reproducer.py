#-*- coding : utf-8 -*-
from playsound import playsound
import time
import mutagen
file = open('audio_list.txt','r')
data = file.readlines()
file.close()
import split
t = time.perf_counter()
while True:
	for i in data[0:-1]:
		try:
			a = mutagen.File("songs/"+str(i.split("/")[3][0:-1])+"/"+str(i.split("/")[2])+"/"+str(i.split("/")[1])+"/"+str(i.split("/")[0]))
			print('Reproduciendo: "'+str(i.split("/")[0].split(".")[0])+'" de '+str(i.split("/")[2]))
			playsound(u"songs/"+str(i.split("/")[3][0:-1])+"/"+str(i.split("/")[2])+"/"+str(i.split("/")[1])+"/"+str(i.split("/")[0]))
			new_t = time.perf_counter()-t
			h = new_t//3600
			m = (new_t-h*3600)//60
			s = round(new_t-h*3600-m*60)
			print ("Time transcurred: "+str(h)+" h "+str(m)+" m "+str(s)+" s")
		except UnicodeDecodeError:
			print('Error ascii no arquivo: "'+str(i.split("/")[0].split(".")[0])+'" de '+str(i.split("/")[2]))
		except KeyboardInterrupt:
			print("saindo...")
			quit()
