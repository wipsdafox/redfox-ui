global data
data = json.load(open("sys/config.json")) #Load config file

#Set some vars.
enablegamepad = data["enable_gamepad"]

#Function to load programs. Do not call directly!!!
def app(name):
    print("INFO: Loading file \"" +  name + "\"")
    exec(open(name).read())
