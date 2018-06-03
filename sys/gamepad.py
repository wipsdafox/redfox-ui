global gp_buttons

gp_buttons = {'a': 0, 'b': 0, 'x': 0, 'y': 0, 'ls': 0, 'rs': 0, 'lt': 0, 'rt': 0, 'pad_lx': 0, 'pad_rx': 0, 'pad_ly': 0, 'pad_ry': 0, }

gp_tdeadzone = data["gamepad_trigger_deadzone"]
gp_deadzone_high = data["gamepad_deadzone_high"]
gp_deadzone_low = data["gamepad_deadzone_high"]
gp_fix = data["gamepad_linux_fix"]

def gp_refresh():
	global gp_buttons
	gp_buttons = {'a': 0, 'b': 0, 'x': 0, 'y': 0, 'ls': 0, 'rs': 0, 'lt': 0, 'rt': 0, 'pad_lx': 0, 'pad_rx': 0, 'pad_ly': 0, 'pad_ry': 0, }
	events = get_gamepad()
	for event in events:
		if(event.code == "BTN_SOUTH"):
			gp_buttons["a"] = event.state
		
		if(event.code == "BTN_EAST"):
			gp_buttons["b"] = event.state
			
		if(gp_fix == 1):
			if(event.code == "BTN_WEST"):
				gp_buttons["y"] = event.state
			if(event.code == "BTN_NORTH"):
				gp_buttons["x"] = event.state
		else:
			if(event.code == "BTN_NORTH"):
				gp_buttons["y"] = event.state
			if(event.code == "BTN_WEST"):
				gp_buttons["x"] = event.state
			
		if(event.code == "BTN_TL"):
			gp_buttons["ls"] = event.state
		
		if(event.code == "BTN_TR"):
			gp_buttons["rs"] = event.state
			
		if(event.code == "ABS_RZ" and event.state > gp_tdeadzone):
			gp_buttons["rt"] = 1
		else:
			gp_buttons["rt"] = 0
		
		if(event.code == "ABS_Z" and event.state > gp_tdeadzone):
			gp_buttons["lt"] = 1
		else:
			gp_buttons["lt"] = 0
		
		if(event.code == "ABS_X" and event.state > gp_deadzone_high):
			gp_buttons["pad_lx"] = 1
		elif(event.code == "ABS_X" and event.state < gp_deadzone_low):
			gp_buttons["pad_lx"] = -1
		else:
			gp_buttons["pad_lx"] = 0
			
		if(event.code == "ABS_RX" and event.state > gp_deadzone_high):
			gp_buttons["pad_rx"] = 1
		elif(event.code == "ABS_RX" and event.state < gp_deadzone_low):
			gp_buttons["pad_rx"] = -1
		else:
			gp_buttons["pad_rx"] = 0
			
		if(event.code == "ABS_Y" and event.state > gp_deadzone_high):
			gp_buttons["pad_ly"] = 1
		elif(event.code == "ABS_Y" and event.state < gp_deadzone_low):
			gp_buttons["pad_ly"] = -1
		else:
			gp_buttons["pad_ly"] = 0
			
		if(event.code == "ABS_RY" and event.state > gp_deadzone_high):
			gp_buttons["pad_ry"] = 1
		elif(event.code == "ABS_RY" and event.state < gp_deadzone_low):
			gp_buttons["pad_ry"] = -1
		else:
			gp_buttons["pad_ry"] = 0
