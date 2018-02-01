from guizero import App, PushButton
def do_nothing():
    print("Nothing happened")
def sair():
    quit()
app = App(title="Player",width = 165, height = 40, layout="grid")
button1 = PushButton(app, command=do_nothing, text="play", grid=[0,0])
button2 = PushButton(app, command=do_nothing, text="pause", grid=[1,0])
button2 = PushButton(app, command=sair, text="close", grid=[2,0])
app.display()
