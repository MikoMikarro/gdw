# -*- coding: utf-8 -*-

from string import split
import os
from sys import executable
from subprocess import Popen, CREATE_NEW_CONSOLE,call

import a_x
import a_a
import a_b
import a_c
import rep_joined
import v_c
import o_at
import random

from random import shuffle
print ("Bienvenido al reproductor de musica de Miko")
last_act = "Iniciar o programa"
while True:
	print ("Last act: "+ last_act)
	print ("Que quieres hacer?")
	print ("a - Novo autor")
	print ("b - Nova cancion")
	print ("c - Novo xenero")
	print ("d - Novo album")
	print ("e - Lista de reproducion por album")
	print ("f - Lista de reproducion por artista")
	print ("g - Lista de reproducion por xenero")
	print ("h - Todo")
	print ("i - Abrir AtubeCatcher")
	print ("j - Para el volumen")
	print ("k - Parar o reproductor")
	print ("l - Reinicar o reproductor")
	print ("s - Sair")
	ans = raw_input().lower()
	if ans == "a":
		last_act = a_a.ex()
	elif ans == "b":
		last_act = a_c.ex()
	elif ans == "c":
		last_act = a_x.ex()
	elif ans == "d":
		last_act = a_b.ex()
	elif ans == "e":
		last_act = rep_joined.ex("album")
	elif ans == "f":
		last_act = rep_joined.ex("author")
	elif ans == "g":
		last_act = rep_joined.ex("genre")

	elif ans == "h":
		last_act = rep_joined.ex("all")
		pass
	elif ans == "i":
		call("nircmd.exe exec show C:/Program Files (x86)/DsNET Corp/aTube Catcher 2.0/yct.exe")
	    last_act = "Abrir AtubeCatcher"

	elif ans == "j":
		while True:
			try:
				print("Volumen?: 0.0 - 100.0")
				ans = float(input())
				if ans <=100 and ans >=0:
					call("nircmd.exe setappvolume python.exe " + str(ans/100) )
				    return "Cambiar volume a "+str(ans)+"%"
					break
				else:
					print("Un numero dentro dos parametros")
			except:
				print("Numeros")
	elif ans == "k":
		call("nircmd.exe suspendprocess python.exe " + str(ans/100) )
		return "Parar o reproductor"
	elif ans == "l":
		call("nircmd.exe resumeprocess python.exe " + str(ans/100) )
		return "Re activar o reproductor"
	elif ans == "s":
		break
	else:
		print ( " Non tenho programada esa opcion " )
