# Control the mouse movement using hand gesture
# using accelerometer

import serial,time,pyautogui

ser=serial.Serial(port='/dev/ttyACM1',baudrate=500000,timeout=0.5)
#To find the name of port use ls /dev/serial/by-id/ in terminal
# In Arduino see in the status bar

time.sleep(0.1)#give sometime for port to be ready

while 1:
	ardSer= ser.readline().decode('ascii')
	#removes 'b' and apostrophe  characters from the serial data 

	print(ardSer)

	#performs the desired action
	if 'right' in ardSer:
		pyautogui.moveRel(30,0)
	if 'left' in ardSer:
		pyautogui.moveRel(-30)
		
	if 'up' in ardSer:
		pyautogui.moveRel(0,-30)
	
	if 'down' in ardSer:
		pyautogui.moveRel(0,30)
	if 'stop' in ardSer:
		pyautogui.moveRel(0,0)

	adrSer=""		
	

