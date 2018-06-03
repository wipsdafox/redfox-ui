printf("Press A to print a string or press B to exit.\n")
updateTerm()
while(1):
	gp_refresh()
	if(gp_buttons["a"]):
		createDialog("It works!\n")
	if(gp_buttons["b"]):
		break;
	updateTerm()
