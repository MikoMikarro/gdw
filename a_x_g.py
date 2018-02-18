import os
import string
from string import replace
from guizero import App, PushButton, Text, TextBox


def ex():
	def exit():
		ap_ax.destroy()
	def a_gen():
		file = open("genres.txt","r")
		xenres = file.readlines()
		file.close()
		xen_name = replace(input_box.get()," ","_")
		check = False
		for i in xenres[:]:
			if i[0:-1].lower() == xen_name.lower():
				err_text.clear()
				err_text.append("Xenero xa existente")
				check = True
				break
		if check == False:
			file = open("genres.txt","r")
			act_data = file.read()
			file.close()
			os.mkdir("songs/"+xen_name)
			os.mkdir("songs/"+xen_name+"/No_definido")
			os.mkdir("songs/"+xen_name+"/No_definido/No_definido")
			file = open("genres.txt","w")
			file.write(act_data+xen_name+"\n")
			file.close
			err_text.clear()
			err_text.append("Xenero correctamente anhadido")
	ap_ax = App(title="Anhadir xenero", layout = "grid")
	input_box = TextBox(ap_ax,grid = [1,0])
	n_text = Text(ap_ax,grid = [0,0], text = "Genero: ", align = "left")
	button1 = PushButton(ap_ax,text = "Anhadir", command = a_gen,grid = [0,1])
	button2 = PushButton(ap_ax,text = "Close", command = exit,grid = [1,1])
	err_text = Text(ap_ax,grid = [0,2], align = "left")
	ap_ax.display()
