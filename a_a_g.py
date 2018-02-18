import os
import string
from string import replace,split
from guizero import App, PushButton, Text, TextBox, Slider


def ex():
	size = 10
	def ret_txt():
		txt = ""
		num = 1
		for l in data[val.value*size:size+val.value*size]:
			txt += str(num) + " :" +l
			num +=1
		return txt
	file_name = "genres.txt"
	def go_next():
		val.value = val.value + 1
		text.clear()
		text.append(ret_txt())
		prev.enable()
		if val.value*size+size > lenght:
			next_b.disable()
		refresh_butt()
	def go_prev():
		val.value = val.value - 1
		text.clear()
		text.append(ret_txt())
		if val.value == 0:
			prev.disable()
		next_b.enable()
		refresh_butt()
	file = open(file_name,"r")
	data = file.readlines()
	file.close()
	lenght = len(data)
	def refresh_butt(a):
		if 	(slid.value+val.value*size)-1 < lenght:
			button1.enable()
		else:
			button1.disable()
	def exit():
		ap_ax.destroy()
	def a_auth():
		file = open("authors.txt","r")
		authors = file.readlines()
		file.close()
		auth_name = replace(input_box.get()," ","_")
		check = False
		for i in authors[:]:
			if i[0:-1].lower() == auth_name.lower():
				err_text.clear()
				err_text.append("Autor xa engadido")
				check = True
				break
		if 	(slid.value+val.value*size)-1 < lenght:
			xen_name = data[(slid.value+val.value*size)-1][0:-1]
		else:
			check = True
		if check == False:
			file = open("authors.txt","r")
			act_data = file.read()
			file.close()
			os.mkdir("songs/"+xen_name+"/"+auth_name)
			os.mkdir("songs/"+xen_name+"/"+auth_name+"/No_definido")
			file = open("authors.txt","w")
			file.write(act_data+auth_name+"/"+xen_name+"\n")
			file.close
			err_text.clear()
			err_text.append("Autor correctamente anhadido")

	ap_ax = App(title="Anhadir autor", layout = "grid", height = 350,width = 300)
	input_box = TextBox(ap_ax,grid = [1,0], width = 30)
	n_text = Text(ap_ax,grid = [0,0], text = "Autor: ", align = "left")
	button1 = PushButton(ap_ax,text = "Anhadir", command = a_auth,grid = [0,1])
	button2 = PushButton(ap_ax,text = "Close", command = exit,grid = [1,1])
	slid= Slider(ap_ax, start = 1, end = 10,grid = [0,2], horizontal = False, command = refresh_butt)
	prev = PushButton(ap_ax, command = go_prev, text = "Prev",grid = [0,3])
	next_b = PushButton(ap_ax, command = go_next, text = "Next", grid = [1,3])
	text = Text(ap_ax, grid = [1,2])
	val = Text(ap_ax,grid = [10,10])
	val.hide()
	val.value = 0
	text.append(ret_txt())
	err_text = Text(ap_ax,grid = [3,0], align = "left")
	ap_ax.display()
