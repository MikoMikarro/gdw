from guizero import App, PushButton, Text
from playsound import playsound
import time
from string import split
t = time.clock()
i = 0
app = App(title="Player",width = 500, height = 40, layout="grid")
file = open('audio_list.txt','r')
data = file.readlines()
file.close()


def do_nothing():
    print("Nothing happened")
def sair():
    app.destroy()
def update_txt(stri):
    text.clear()
    text.append('Reproduciendo: "'+str(split(split(data[i],"/")[0],".")[0])+'" de '+str(split(data[i],"/")[2]))
def next_c():
    i +=1
    try:
		text_1 = Text(app,text ='Reproduciendo: "'+str(split(split(data[i],"/")[0],".")[0])+'" de '+str(split(data[i],"/")[2]))
		play_s()
		new_t = time.clock()-t
		h = new_t//3600
		m = (new_t-h*3600)//60
		s = round(new_t-h*3600-m*60)
		update_txt("Time transcurred: "+str(h)+" h "+str(m)+" m "+str(s)+" s")
    except UnicodeDecodeError:
		print('Error ascii no arquivo: "'+str(split(split(data[i],"/")[0],".")[0])+'" de '+str(split(data[i],"/")[2]))
    except KeyboardInterrupt:
		print("saindo...")
		quit()
    except IndexError:
        i = 0
def play_s():
    playsound("songs/"+str(split(data[i],"/")[3][0:-1])+"/"+str(split(data[i],"/")[2])+"/"+str(split(data[i],"/")[1])+"/"+str(split(data[i],"/")[0]), False)
text = Text(app, text="Timte transcurred: 0h 0m 0s",grid =[1,0])
# button1 = PushButton(app, command=do_nothing, text="play", grid=[0,0])
# button2 = PushButton(app, command=do_nothing, text="pause", grid=[1,0])
# button3 = PushButton(app, command=sair, text="close", grid=[2,0])
button4 = PushButton(app, command=next_c, text="next", grid=[0,0])
# button5 = PushButton(app, command=prev_c, text="prev", grid=[1,0])



while True:
    i+=1
    print data[i]
    try:
		text_1 = Text(app,text ='Reproduciendo: "'+str(split(split(data[i],"/")[0],".")[0])+'" de '+str(split(data[i],"/")[2]), grid=[0,1])
		play_s()
		new_t = time.clock()-t
		h = new_t//3600
		m = (new_t-h*3600)//60
		s = round(new_t-h*3600-m*60)
		update_txt("Time transcurred: "+str(h)+" h "+str(m)+" m "+str(s)+" s")
    except UnicodeDecodeError:
		print('Error ascii no arquivo: "'+str(split(split(data[i],"/")[0],".")[0])+'" de '+str(split(data[i],"/")[2]))
    except KeyboardInterrupt:
		print("saindo...")
		quit()
    app.display()
