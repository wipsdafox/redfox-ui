global data
try:
    data = json.load(open("sys/config.json")) #Load config file

except:
    log("FATAL: Couldnt load config!")
    while True:
        

#Set some vars.
global enablegamepad
global icon_size
global icon_spacing
enablegamepad = data["enable_gamepad"]
icon_size = 256
#icon_size = data["icon_size"]
#icon_spacing = icon_size / 4
icon_spacing = 64

#Function to load programs. Do not call directly!!!
def app(name):
    log("INFO: Loading file \"" +  name + "\"")
    exec(open(name).read())
