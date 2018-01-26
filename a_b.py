import string
from string import split
from string import replace
import os
def ex():
	while True:
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
	# file = open("authors.txt","r")
	# authors = []
	# xenres = []
	# data = file.readlines()
	# file.close()
	# num = 0
	# nums = []
	# for i in data:
	# 	nums.append(num)
	# 	num+= 1
	# 	authors.append(split(i,"/")[0])
	# 	xenres.append(split(i,"/")[1])
	# while True:
	# 	num = 0
	# 	list_ans = []
	# 	print ("Autores disponhibels:")
	# 	for i in authors:
	# 		print num,i
	# 		list_ans.append(num)
	# 		num +=1
	# 	ans = input()
	# 	if int(ans) in list_ans:
	# 		auth_name = authors[int(ans)]
	# 		xen_name = xenres[int(ans)]
	# 		file = open("albumes.txt","r")
	# 		act_data = file.read()
	# 		file.close()
	# 		file = open("albumes.txt","w")
	# 		file.write(act_data +alb_name+"/"+auth_name+'/'+xen_name+"\n")
	# 		file.close()
	# 		last_act = "anhadir "+alb_name + " ("+auth_name+")"
	# 		return last_act
	# 		break
	# 	else:
	# 		print("Non tenho rexistrado ese autor")
