import os

def ex():
	file = open("genres.txt","r")
	act_data = file.read()
	file.close()
	file = open("genres.txt","r")
	xenres = file.readlines()
	file.close()
	check = True
	while True:
		xen_name = replace(raw_input("Indica o nome do xenero que queres agregar: ")," ","_")
		for i in xenres[:]:
			if i[0:-1].lower() == xen_name.lower():
				print("Xenero xa anhadido")
				check = True
				break
			else:
				check = False
				pass
		if check == False:
			break
	os.mkdir("songs/"+xen_name)
	os.mkdir("songs/"+xen_name+"/No_definido")
	os.mkdir("songs/"+xen_name+"/No_definido/No_definido")
	file = open("genres.txt","w")
	file.write(act_data+xen_name+"\n")
	file.close
	last_act = "Anhadir xenero: " + xen_name
	return last_act
