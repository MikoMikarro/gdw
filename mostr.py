from guizero import App, Text, PushButton
from string import split
size = 20

def ex():
    file = open("filt.txt","r")
    filt = file.read()
    file.close
    def ret_txt():
        txt = ""
        if protocol == 1:
            for l in data[val.value*size:size+val.value*size]:
                txt += split(l,"/")[0]+"\n"
        else:
            for l in data[val.value*size:size+val.value*size]:
                txt += l[:-1]+"\n"
        return txt
    if filt == "aut":
        protocol = 1
        file_name = "authors.txt"
    if filt == "xen":
        protocol = 0
        file_name = "genres.txt"
    if filt == "alb":
        protocol = 1
        file_name = "albumes.txt"
    if filt == "can":
        protocol = 1
        file_name = "audio_data.txt"
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
    appp = App(title="Menu", height = 470)
    text = Text(appp, align = 'left')
    prev = PushButton(appp, command = go_prev, text = "Prev")
    next_b = PushButton(appp, command = go_next, text = "Next")
    val = Text(appp,grid = [10,10])
    val.hide()
    val.value = 0
    text.append(ret_txt())
    prev.disable()
    if size > lenght:
        next_b.disable()
    appp.display()
