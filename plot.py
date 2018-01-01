# To plot the x,y,z data of accelerometer
# Plot x-axis data
# To plot all axes graph in the same graph UNCOMMENT all the COMMENTED statements
# in the below code 


import serial,time
import matplotlib.pyplot as plt
import numpy as np


ser=serial.Serial(port='/dev/ttyACM12',baudrate=500000,timeout=0.5)
#To find the name of port use ls /dev/serial/by-id/ in terminal
# In Arduino see in the status bar
time.sleep(0.1)


#plt.close('all')
y=[0]*50
#z=[0]*50
#x=[0]*50
plt.ion()# it opens the interactive session (changes in graph appears at once )
#plt.ioff# off the interactive graph

line,=plt.plot(y,'ro-',label='y')
# line1,=plt.plot(x,'b',label='x')
# line2,=plt.plot(z,label='z')

#plt.ylim([100,500])

plt.legend(loc='upper left')
plt.title("Accelerometer Data")
plt.ylabel('Data')
plt.grid(True)


while 1:
	ardSer= ser.readline().decode('ascii').split(" ")

	while ser.inWaiting()==0: #if no data is coming then stay here only
		pass
	if len(ardSer)==3:#so that if other string comes graph does not give error
		ymin=float(min(ardSer))-5
		ymax=float(max(ardSer))+5
		plt.ylim([ymin,ymax])

		y.append(float(ardSer[0]))
		#x.append(float(ardSer[1]))	
		#z.append(float(ardSer[2]))

		del(y[0])
		#del(x[0])
		#del(z[0])

		#line.set_xdata(np.arange(len(y)))
		line.set_ydata(y) #updating the value on graph
		#line1.set_ydata(x)
		#line2.set_ydata(z)
		
		plt.draw()# without this statement also it will work
		plt.pause(0.00001) # give pause so that graph doesn't crash

		print(ardSer)

		adrSer=""		
	

