from string import split
import os
from os import listdir
from os.path import isfile, join
import shutil
def ex():
	paste = "to_import/"
	albumes = []
	authors = []
	xeneros = []
	file = open("albumes.txt","r")
	for i in file.readlines():
		albumes.append(split(i,"/")[0])
		authors.append(split(i,"/")[1])
		xeneros.append(split(i,"/")[2][0:-1])
	file.close()
	while True:
		num = 0
		print ("Albumes disponhibels:")
		for i in albumes:
			print num,i," - (",authors[num],')'
			num +=1
		ans = input()
		try:
			if ans == 0:
				authors = []
				xeneros = []
				file = open("authors.txt","r")
				for i in file.readlines():
					authors.append(split(i,"/")[0])
					xeneros.append(split(i,"/")[1][0:-1])
				file.close()
				while True:
					num = 0
					print ("Autores disponhibels:")
					for i in authors:
						print num,i
						num +=1
					ans = input()
					if int(ans) <= num:
						alb_name = "No_definido"
						auth_name = authors[int(ans)]
						xen_name = xeneros[int(ans)]
						break
					else:
						print("Non tenho rexistrado ese autor")
				break
			elif int(ans) <= num:
				alb_name = albumes[int(ans)]
				auth_name = authors[int(ans)]
				xen_name = xeneros[int(ans)]
				break
			else:
				print("Non tenho rexistrado ese album")
		except:
			pass
	onlyfiles = [f for f in listdir(str(paste)) if isfile(join(str(paste), f))]
	print (onlyfiles)
	while True:
		print ("Arquivos disponhibels:")
		for i in onlyfiles:
			print i
		num +=1
		print "Mover y n"
		ans = raw_input()
		while True:
			if ans.lower() == "y":
				print ("Movendo")
				break
			elif ans.lower() == "n":
				quit()
			else:
				print ("Non tenho rexistrada esta  orde")
				break
		for i in onlyfiles:
			try:
				shutil.move(paste+"/"+ i,"songs/"+xen_name+"/"+auth_name+"/"+alb_name+"/"+i)
			except:
				print("Error")
				while True:
					print("Eliminar o arquivo?y/n")
					yn = raw_input().lower()
					if yn == "y":
						os.remove(paste+ "/" + i)
					elif yn == "n":
						onlyfiles.pop(i)
					else:
						print("Non tenho orde posibel")
		break
	text = ""
	for i in onlyfiles:
		text = text+ i+"/"+alb_name+"/"+auth_name+"/"+xen_name+"\n"
	file = open("audio_data.txt","r")
	act_data = file.read()
	file.close()
	file = open("audio_data.txt","w")
	file.write(act_data +text)
	file.close()
	last_act = "anhadir cancions do album "+"("+alb_name+")  -- "+auth_name
	return last_act
