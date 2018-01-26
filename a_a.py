import os
import string
from string import split
from string import replace
def ex():
	while True:
		file = open("authors.txt","r")
		act_data = file.read()
		file.close()
		file = open("authors.txt","r")
		authors = file.readlines()
		file.close()
		check = True
		while True:
			aut_name = replace(raw_input("Indica o nome do author: ")," ","_")
			for i in authors:
		 		if split(i,"/")[0].lower() == aut_name.lower():
					print ("Autor xa anhadido")
					check = True
					break
				else:
					check = False
					pass
			if check == False:
				break
		xenres = []
		file = open("genres.txt","r")
		for i in file.readlines():
			xenres.append(i[0:-1])
		file.close()
		while True:
			num = 0
	  		print ("Xeneros disponhibels:")
			for i in xenres:
				print num,i
				num +=1
			ans = input()
			if int(ans) <= num:
				xen_name = xenres[int(ans)]
				break
			else:
				print("Non tenho rexistrado ese xenero")
		os.mkdir("songs/"+xen_name+"/"+aut_name)
		os.mkdir("songs/"+xen_name+"/"+aut_name+"/No_definido")
		file = open("authors.txt","w")
		file.write(act_data +aut_name+"/"+xen_name+"\n")
		file.close()
		last_act = "anhadir "+aut_name + " ("+xen_name+")"
		return last_act
