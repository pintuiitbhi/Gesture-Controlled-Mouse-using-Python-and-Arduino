# To plot the x,y,z data of accelerometer
# Makes a subplot

import serial,time
import matplotlib.pyplot as plt
import numpy as np


ser=serial.Serial(port='/dev/ttyACM12',baudrate=500000,timeout=0.5)
#To find the name of port use ls /dev/serial/by-id/ in terminal
# In Arduino see in the status bar
time.sleep(0.1)

x=[0]*50
y=[0]*50
z=[0]*50

plt.ion()# it opens the interactive session (changes in graph appears at once )
#plt.ioff# off the interactive graph

f, (ax1, ax2, ax3) = plt.subplots(3, sharex=True, sharey=False)

f.suptitle("Accelerometer Data")#adds a main title

while 1:
	ardSer= ser.readline().decode('ascii').split(" ")
	#removes 'b' and apostrophe  characters from the serial data 

	while ser.inWaiting()==0: #if no data is coming then stay here only
		pass
	if len(ardSer)==3:#so that if other string comes graph does not give error

		x.append(float(ardSer[1]))
		y.append(float(ardSer[0]))	
		z.append(float(ardSer[2]))

		del(y[0])
		del(x[0])
		del(z[0])


		ax1.clear()
		ax2.clear()
		ax3.clear()

		ax1.plot(x)
		ax2.plot(y) 
		ax3.plot(z)

		ax1.set_title('X Data')
		ax2.set_title('Y Data')
		ax3.set_title('Z Data')
		plt.pause(0.001)

		print(ardSer)

		adrSer=""		
	

