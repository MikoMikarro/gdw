# -*- coding: utf-8 -*-

from string import split
import os
from sys import executable
from subprocess import Popen, CREATE_NEW_CONSOLE

import a_x
import a_a
import a_b
import a_c
import r_t
import r_a
import r_b
import r_x
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
	print ("h - Lista de reproducion por artista")
	print ("i - Lista de reproducion por xenero")
	print ("j - Todo")
	print ("k - Abrir AtubeCatcher")
	print ("v - Para el volumen")
	print ("s - Sair")
	ans = raw_input().lower()
	if ans == "a":
		last_act = a_a.ex()
	elif ans == "c":
		last_act = a_x.ex()
	elif ans == "b":
	    last_act = a_c.ex()
	elif ans == "d":
		last_act = a_b.ex()
	elif ans == "e":
		last_act = r_b.ex()
	elif ans == "h":
		last_act = r_a.ex()
	elif ans == "i":
		last_act = r_x.ex()
	elif ans == "s":
		break
	elif ans == "ra":
		pass
	elif ans == "j":
		last_act = r_t.ex()
	elif ans == "k":
		last_act = o_at.ex()
	elif ans == "v":
		while True:
			try:
				print("Volumen?: 0.0 - 100.0")
				ans = input()
				if ans <=100 and ans >=0:
					last_act = v_c.ex(ans)
					break
				else:
					print("Un numero dentro dos parametros")
			except:
				print("Numeros")

	else:
		print ( " Non tenho programada esa opcion " )
