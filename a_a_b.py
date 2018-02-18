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
			txt += str(num) + " :" +split(l,"/")[0]+"\n"
			num +=1
		return txt
	file_name = "authors.txt"
	def go_next():
		val.value = val.value + 1
		text.clear()
		text.append(ret_txt())
		prev.enable()
		if val.value*size+size > lenght:
			next_b.disable()
	def go_prev():
		val.value = val.value - 1
		text.clear()
		text.append(ret_txt())
		if val.value == 0:
			prev.disable()
		next_b.enable()
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
		ap_ab.destroy()
	def a_auth():
		file = open("albumes.txt","r")
		authors = file.readlines()
		file.close()
		alb_name = replace(input_box.get()," ","_")
		check = False
		for i in authors[:]:
			if i[0:-1].lower() == alb_name.lower():
				err_text.clear()
				err_text.append("Album xa engadido")
				check = True
				break
		if 	(slid.value+val.value*size)-1 < lenght:
			auth_name = split(data[(slid.value+val.value*size)-1],"/")[0]
			xen_name = split(data[(slid.value+val.value*size)-1],"/")[1][:-1]
		else:
			check = True
		if check == False:
			file = open("albumes.txt","r")
			act_data = file.read()
			file.close()
			os.mkdir("songs/"+xen_name+"/"+auth_name+"/"+alb_name)
			file = open("albumes.txt","w")
			file.write(act_data+alb_name+"/"+auth_name+"/"+xen_name+"\n")
			file.close
			err_text.clear()
			err_text.append("Album correctamente anhadido")

	ap_ab = App(title="Anhadir album", layout = "grid", height = 400, width = 350)
	input_box = TextBox(ap_ab,grid = [1,0], width = 30)
	n_text = Text(ap_ab,grid = [0,0], text = "Album: ", align = "left")
	button1 = PushButton(ap_ab,text = "Anhadir", command = a_auth,grid = [0,1])
	button2 = PushButton(ap_ab,text = "Close", command = exit,grid = [1,1])
	slid= Slider(ap_ab, start = 1, end = 10,grid = [0,2], horizontal = False, command = refresh_butt)
	prev = PushButton(ap_ab, command = go_prev, text = "Prev",grid = [0,3])
	next_b = PushButton(ap_ab, command = go_next, text = "Next", grid = [1,3])
	text = Text(ap_ab, grid = [1,2])
	val = Text(ap_ab,grid = [10,10])
	val.hide()
	val.value = 0
	text.append(ret_txt())
	err_text = Text(ap_ab,grid = [3,0], align = "left")
	ap_ab.display()
