from subprocess import call
def ex(i):
    call("nircmd.exe setappvolume python.exe " + str(float(i)/100) )
    return "Cambiar volume a "+str(i)+"%"
