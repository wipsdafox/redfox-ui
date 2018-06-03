def log(text):
    print(text)
    with open("log.txt", "a") as myfile:
        myfile.write(text)

log("INFO: Importing libraries...")
from time import gmtime, strftime, localtime
import sys, importlib, os, json
#from inputs import devices, get_gamepad
if sys.version_info[0] == 2: #Check python version
    from Tkinter import *
else:
    from tkinter import *

#Load system stuff
log("INFO: Loading system files...")
exec(open("sys/system.py").read())
exec(open("sys/display.py").read())
exec(open("sys/keyboard.py").read())

if(enablegamepad == 1):
    log("INFO: Loading gamepad...")
    exec(open("sys/gamepad.py").read())

drawHome()
mainloop()
