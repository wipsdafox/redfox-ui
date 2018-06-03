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
global clock #Clock

#Graphics functions
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
        save = display.create_rectangle(x, y, x + 256, y + 256, fill = appConfig["bgcolor"], tags = appConfig["file"])
        display.create_text(x + 128, y + 128, text = appConfig["displayname"], fill = white)
    else:
        try:
            #Otherwise, display the image.
            img = PhotoImage(file = "apps/" + appConfig["icon"])
            appImages.append(img)
            save = display.create_image(x, y, image = img, tags = appConfig["file"], anchor = NW)

        except:
            print("Error displaying app icon!")
            #Create a rectangle with the background color, and add some text with the app name
            save = display.create_rectangle(x, y, x + 256, y + 256, fill = appConfig["bgcolor"], tags = appConfig["file"])
            display.create_text(x + 128, y + 128, text = appConfig["displayname"], fill = white)

    appicons.append(save) #Add ID to appicons variable.
    display.tag_bind(appicons[len(appicons) - 1], '<ButtonPress-1>', launchApp) #Bind it to the launchApp function.

def updateClock():
    global clock
    display.delete(clock) #Delete clock text
    clock = display.create_text(3, 3, text = strftime("%H:%M", localtime()), fill = black, anchor = NW) #Draw time
    master.after(1000, updateClock) #Tell window to do this every second.

def drawHome():
    global clock
    display.delete(all) #Clear screen incase we are updating the whole display
    display.create_rectangle(0, 0, screen_width, screen_height, fill = white) #Draw Background
    if(data["wallpaper"] != "none"):
        try:
            global wallpaper
            wallpaper = PhotoImage(file = data["wallpaper"])
            display.create_image(screen_width / 2, screen_height / 2, image = wallpaper) #Draw wallpaper
        except:
            print("Error while displaying wallpaper!")
    display.create_rectangle(0, 0, screen_width, 18, fill = "#c9ced6", outline = "#c9ced6", stipple = "gray50") #Draw statusbar
    clock = display.create_text(3, 3, text = strftime("%H:%M", localtime()), fill = black, anchor = NW) #Draw clock on status bar
    updateClock()
    #Draw all app icons.
    x = 64
    y = 64
    xx = 0
    yy = 0
    #Get max amount of icons per row and column.
    iconsPerRow = (screen_width / 320) + 64
    iconsPerColumn = (screen_height / 320) + 64
    json_files = [pos_json for pos_json in os.listdir('apps/') if pos_json.endswith('-config.json')] #Get all config files
    for config in json_files:
        appname = config[:-12] #Remove "-config.json" from string
        xx + 1
        if(iconsPerRow != xx + 1):
            drawAppIcon(x, y, appname) #Draw app icon.
            x = x + 320
        else:
            xx = 0
            x = 64
            y = y + 320
            if(iconsPerColumn != yy + 1):
                drawAppIcon(x, y, appname) #Draw app icon.
