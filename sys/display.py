#Basic graphics stuff
master = Tk()

#Get screen size
screen_width = master.winfo_screenwidth()
screen_height = master.winfo_screenheight()

#Make window fullscreen
master.attributes("-fullscreen", True)

#Setup canvas
display = Canvas(master, width=screen_width, height=screen_height)
display.pack()
display.focus_set()

#Define colors
black = "#000000"
white = "#fff"

#Prepare global variables
global appicons #App icon storage
appicons = []
global appImages
appImages = []
global currentDialog #Dialog storage
currentDialog = []
global imageStorage
imageStorage = []
global clock #Clock

#Graphics functions
def preloadImage(path):
    img = PhotoImage(file = path) #Load image into memory
    imageStorage.append(img) #Store it in the global image variable
    return img #Return the file

def setPosition(item, x, y):
    display.coords(item, x, y)

def changePosition(item, x=0, y=0):
    display.move(item, x, y)

def displayImage(x, y, path, tag=0, onclick=0):
    imgFile = preloadImage(path) #Load the image
    imgId = display.create_image(x, y, image = imgFile, anchor = NW, tags = tag) #Display the image and get an ID
    if(onclick != 0):
        display.tag_bind(imgId, '<ButtonPress-1>', onclick)
    return imgId #Return the ID

def displayLine(x, y, x2, y2, color="#000000", onclick=0):
    id = display.create_line(x, y, x2, y2, fill=color)
    if(onclick != 0):
        display.tag_bind(id, '<ButtonPress-1>', onclick)

def displayRectangle(x, y, x2, y2, color="#000000", onclick = 0):
    id = display.create_rectangle(x, y, x2, y2, fill = color)
    if(onclick != 0):
        display.tag_bind(id, '<ButtonPress-1>', onclick)

def displayText(x, y, txt, color="#000000", onclick=0, center=0):
    if(center == 0):
        id = display.create_text(x, y, text = txt, fill = color, anchor=NW)
    else:
        id = display.create_text(x, y, text = txt, fill = color)
    if(onclick != 0):
        display.tag_bind(id, '<ButtonPress-1>', onclick)

def deleteDialog(event):
    global currentDialog
    for item in currentDialog:
        display.delete(item) #Delete text + message box
    currentDialog = [] #Clear dialog storage

def createDialog(message):
    global currentDialog
    #Create message box and text, then store them in the currentDialog variable
    currentDialog.append(display.create_rectangle(screen_width / 2 - 128, screen_height / 2 - 64, screen_width / 2 + 128, screen_height / 2 + 64, fill = black))
    currentDialog.append(display.create_text(screen_width / 2, screen_height / 2, fill = white, text = message, width=236))
    display.tag_bind(currentDialog[0],'<ButtonPress -1>', deleteDialog) #Bind left ButtonPress action to deleting the message box

def launchApp(event):
    item = display.find_closest(event.x, event.y) #Figure out what icon we are hovering over and store it's ID in a variable
    filename = ''.join(display.gettags(item))[:-7] #Get tags for the app icon, telling us where to find the file.
    app("apps/" + filename) #Run the app.

def drawAppIcon(x, y, app):
    global appicons
    appConfig = json.load(open("apps/" + app + "-config.json")) #Parse app config.json file
    if(appConfig["icon"] == "none"): #If the app has no icon file,
        #Create a rectangle with the background color, and add some text with the app name
        save = display.create_rectangle(x, y, x + icon_size, y + icon_size, fill = appConfig["bgcolor"], tags = appConfig["file"])
        display.create_text(x + (icon_size / 2), y + (icon_size / 2), text = appConfig["displayname"], fill = white)
    else:
        try:
            save = displayImage(x, y, "apps/" + appConfig["icon"], tag = appConfig["file"])
        except:
            log("Error displaying app icon!")
            save = display.create_rectangle(x, y, x + icon_size, y + icon_size, fill = appConfig["bgcolor"], tags = appConfig["file"])
            display.create_text(x + (icon_size / 2), y + (icon_size / 2), text = appConfig["displayname"], fill = white)

    appicons.append(save) #Add ID to appicons variable.
    display.tag_bind(appicons[len(appicons) - 1], '<ButtonPress-1>', launchApp) #Bind it to the launchApp function.

def updateClock():
    global clock
    display.delete(clock) #Delete clock text
    clock = display.create_text(3, 3, text = strftime("%H:%M", localtime()), fill = black, anchor = NW) #Draw time
    master.after(1000, updateClock) #Tell window to do this every second.

def drawHome():
    log("drawHome start!")
    global icon_size
    global icon_spacing
    global clock
    log("clearing screen...")
    display.delete(all) #Clear screen incase we are updating the whole display
    log("drawing background...")
    display.create_rectangle(0, 0, screen_width, screen_height, fill = white) #Draw Background
    if(data["wallpaper"] != "none"):
        try:
            log("drawing wallpaper...")
            global wallpaper
            wallpaper = PhotoImage(file = data["wallpaper"])
            display.create_image(screen_width / 2, screen_height / 2, image = wallpaper) #Draw wallpaper
        except:
            log("wallpaper error!")
    display.create_rectangle(0, 0, screen_width, 18, fill = "#c9ced6", outline = "#c9ced6", stipple = "gray50") #Draw statusbar
    clock = display.create_text(3, 3, text = strftime("%H:%M", localtime()), fill = black, anchor = NW) #Draw clock on status bar
    updateClock()
    #Draw all app icons.
    log("drawing app icons...")
    x = icon_spacing
    y = icon_spacing
    xx = 0
    yy = 0
    #Get max amount of icons per row and column.
    iconsPerRow = (screen_width / icon_size + icon_spacing) + icon_spacing
    iconsPerColumn = (screen_height / icon_size + icon_spacing) + icon_spacing
    json_files = [pos_json for pos_json in os.listdir('apps/') if pos_json.endswith('-config.json')] #Get all config files
    for config in json_files:
        log(config)
        appname = config[:-12] #Remove "-config.json" from string
        xx + 1
        if(iconsPerRow != xx + 1):
            drawAppIcon(x, y, appname) #Draw app icon.
            x = x + icon_size + icon_spacing
        else:
            xx = 0
            x = icon_spacing
            y = y + icon_size + icon_spacing
            if(iconsPerColumn != yy + 1):
                drawAppIcon(x, y, appname) #Draw app icon.
