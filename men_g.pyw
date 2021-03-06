from guizero import App, PushButton, Text, MenuBar, Picture
import time
from sys import executable
from subprocess import Popen, CREATE_NEW_CONSOLE
import rep_joined
def most_aut():
    txt = 'from mostr import *; ex()'
    file = open("filt.txt","w")
    file.write("aut")
    file.close()
    Popen('python -c '+'"'+txt+'"', CREATE_NEW_CONSOLE)
def most_xen():
    txt = 'from mostr import *; ex()'
    file = open("filt.txt","w")
    file.write("xen")
    file.close()
    Popen('python -c '+'"'+txt+'"', CREATE_NEW_CONSOLE)
def most_alb():
    txt = 'from mostr import *; ex()'
    file = open("filt.txt","w")
    file.write("alb")
    file.close()
    Popen('python -c '+'"'+txt+'"', CREATE_NEW_CONSOLE)
def most_can():
    txt = 'from mostr import *; ex()'
    file = open("filt.txt","w")
    file.write("can")
    file.close()
    Popen('python -c '+'"'+txt+'"', CREATE_NEW_CONSOLE)
def anh_xen():
    txt = 'from a_x_g import *; ex()'
    Popen('python -c '+'"'+txt+'"', CREATE_NEW_CONSOLE)
def anh_aut():
    txt = 'from a_a_g import *; ex()'
    Popen('python -c '+'"'+txt+'"', CREATE_NEW_CONSOLE)
def anh_alb():
    txt = 'from a_a_b import *; ex()'
    Popen('python -c '+'"'+txt+'"', CREATE_NEW_CONSOLE)
def r_t_g():
    rep_joined.ex("all")

app = App(title="Menu",height = 868,width = 476, layout="auto")
menubar = MenuBar(app,
                  toplevel=["Mostrar","Anhadir","Reproducir"],
                  options=[
                      [ ["Mostrar autores", most_aut], ["Mostrar xeneros", most_xen], ["Mostrar albumes", most_alb], ["Mostrar cancions", most_can] ],
                      [ ["Anhadir xenero", anh_xen], ["Anhadir autor", anh_aut], ["Anhadir album", anh_alb]],
                      [ ["Reproducir todo", r_t_g] ]
                  ])
picture = Picture(app, image="gramola.gif")
app.display()
