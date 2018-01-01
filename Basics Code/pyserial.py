#Basic code to read from serial in Python
import serial,time
#time.sleep(2)  # delays for 2 seconds

ser=serial.Serial(port='/dev/ttyACM1', baudrate=19200,timeout=1)
#To find the name of port use ls /dev/serial/by-id/ in terminal
# In Arduino see in the status bar

while 1:
	#data=ser.readline() # gives out in binary prefixed with b
	data=ser.readline().decode('ascii')# it decodes the ascii value in readable form

	print(data)