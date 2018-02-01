import os
import string
from string import split
from string import replace
def ex():
	file = open("albumes.txt","r")
	act_data = file.read()
	file.close()
	file = open("albumes.txt","r")
	albumes = file.readlines()
	file.close()
	check = True
	while True:
		alb_name = replace(raw_input("Indica o nome do Album: ")," ","_")
		for i in albumes:
	 		if split(i,"/")[0].lower() == alb_name.lower():
				print ("Album xa anhadido")
				check = True
				break
			else:
				check = False
				pass
		if check == False:
			break
	authors = []
	xenres = []
	file = open("authors.txt","r")
	for i in file.readlines():
		authors.append(split(i,"/")[0])
		xenres.append(split(i,"/")[1][0:-1])
	file.close()
	while True:
		num = 0
		print ("Autores disponhibels:")
		for i in authors:
			print num,i
			num +=1
		ans = input()
		if ans <= num:
			aut_name = authors[ans]
			xen_name = xenres[ans]
			break
		else:
			print("Non tenho rexistrado ese autor")
	os.mkdir("songs/"+xen_name+"/"+aut_name+"/"+alb_name)
	file = open("albumes.txt","w")
	file.write(act_data +alb_name+"/"+aut_name+"/"+xen_name+"\n")
	file.close()
	last_act = "anhadir "+alb_name + " ("+aut_name+")"
	return last_act
