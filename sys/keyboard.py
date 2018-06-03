#On screen keyboard stuff
global kbd
kbd = []
r1 =  ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'],
r2 =  ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
r3 =  ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';'],
r4 =  ['Aa', 'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.'],
r5 =  ['Backspace', 'Space', 'Close'],

def handleKeyPress(event):
    item = display.find_closest(event.x, event.y) #Figure out what key we are hovering over and store it's ID in a variable
    key = ''.join(display.gettags(item))[:-7] #Get tags for the key
    master.event_generate("<KeyPress>", keycode=key)

def deleteKeyboard(event):
    global kbd
    for item in kbd:
        display.delete(item)
    kbd = []

def initKeyboard():
    global kbd
    #70
    #37
    #Where do we start drawing the keyboard?
    kbdstartx = (screen_width - 610) / 2
    kbdstarty = screen_height - 290
    kbd.append(display.create_rectangle(kbdstartx, kbdstarty, ((screen_width - 610) / 2) + 610, screen_height, fill = "#36383a")) #Draw keyboard Background
    drawx = kbdstartx + 10
    drawy = kbdstarty + 10

    #Sorry for the copy/paste, got frustrated trying to do it the right way

    for list in r1:
        for key in list:
            #Draw + bind key and increment X pos.
            kbd.append(display.create_rectangle(drawx, drawy, drawx + 50, drawy + 30, fill = "#a4abb2", tags = key))
            display.tag_bind(kbd[len(kbd) - 1], '<ButtonPress -1>', handleKeyPress)
            kbd.append(display.create_text(drawx + 25, drawy + 15, fill = black, text = key, tags = key))
            display.tag_bind(kbd[len(kbd) - 1], '<ButtonPress -1>', handleKeyPress)
            drawx = drawx + 60
    drawx = kbdstartx + 10 #Return X pos
    drawy = drawy + 40 #Increment Y pos

    for list in r2:
        for key in list:
            #Draw + bind key and increment X pos.
            kbd.append(display.create_rectangle(drawx, drawy, drawx + 50, drawy + 50, fill = "#a4abb2", tags = key))
            display.tag_bind(kbd[len(kbd) - 1], '<ButtonPress -1>', handleKeyPress)
            kbd.append(display.create_text(drawx + 25, drawy + 25, fill = black, text = key, tags = key))
            display.tag_bind(kbd[len(kbd) - 1], '<ButtonPress -1>', handleKeyPress)
            drawx = drawx + 60
    drawx = kbdstartx + 10 #Return X pos
    drawy = drawy + 60 #Increment Y pos

    for list in r3:
        for key in list:
            #Draw + bind key and increment X pos.
            kbd.append(display.create_rectangle(drawx, drawy, drawx + 50, drawy + 50, fill = "#a4abb2", tags = key))
            display.tag_bind(kbd[len(kbd) - 1], '<ButtonPress -1>', handleKeyPress)
            kbd.append(display.create_text(drawx + 25, drawy + 25, fill = black, text = key, tags = key))
            display.tag_bind(kbd[len(kbd) - 1], '<ButtonPress -1>', handleKeyPress)
            drawx = drawx + 60
    drawx = kbdstartx + 10 #Return X pos
    drawy = drawy + 60 #Increment Y pos

    for list in r4:
        for key in list:
            #Draw + bind key and increment X pos.
            kbd.append(display.create_rectangle(drawx, drawy, drawx + 50, drawy + 50, fill = "#a4abb2", tags = key))
            display.tag_bind(kbd[len(kbd) - 1], '<ButtonPress -1>', handleKeyPress)
            kbd.append(display.create_text(drawx + 25, drawy + 25, fill = black, text = key, tags = key))
            display.tag_bind(kbd[len(kbd) - 1], '<ButtonPress -1>', handleKeyPress)
            drawx = drawx + 60
    drawx = kbdstartx + 10 #Return X pos
    drawy = drawy + 60 #Increment Y pos
    for list in r5:
        for key in list:

            if(key != 'Space'):
                if(key == "Close"):
                    kbd.append(display.create_rectangle(drawx, drawy, drawx + 110, drawy + 50, fill = "#a4abb2", tags = key))
                    display.tag_bind(kbd[len(kbd) - 1], '<ButtonPress -1>', deleteKeyboard)
                    kbd.append(display.create_text(drawx + 55, drawy + 25, fill = black, text = key, tags = key))
                    display.tag_bind(kbd[len(kbd) - 1], '<ButtonPress -1>', deleteKeyboard)
                else:
                    kbd.append(display.create_rectangle(drawx, drawy, drawx + 110, drawy + 50, fill = "#a4abb2", tags = key))
                    display.tag_bind(kbd[len(kbd) - 1], '<ButtonPress -1>', handleKeyPress)
                    kbd.append(display.create_text(drawx + 55, drawy + 25, fill = black, text = key, tags = key))
                    display.tag_bind(kbd[len(kbd) - 1], '<ButtonPress -1>', handleKeyPress)
                drawx = drawx + 60
            else:
                kbd.append(display.create_rectangle(drawx, drawy, drawx + 350, drawy + 50, fill = "#a4abb2", tags = key))
                drawx = drawx + 300
            drawx = drawx + 60
    drawx = kbdstartx + 10 #Return X pos
    drawy = drawy + 60 #Increment Y pos
