#NeilNoronha

#July 13, 2022

import time
import os
import board
import busio
import adafruit_fxos8700
import matplotlib.pyplot as plt 

i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_fxos8700.FXOS8700(i2c)

def AccelPlot():
	timed = 0
	elapT = []
	accelX = []
	accelY = []
	accelZ = []
	while True:
		accelX.append(sensor.accelerometer[0])
		accelY.append(sensor.accelerometer[1])
		accelZ.append(sensor.accelerometer[2])
		elapT.append(timed)
		print(elapT)
		fig, ax = plt.subplots()
		ax.plot(accelX, elapT, accelY, accelZ)
		ax.grid(True)
		ax.set_ylabel("Acclereration (m/s^2)")
		ax.set_xlabel("Elapsed time (sec)")
		ax.set_title("Acceleration over time")
		plt.show()
		print("showing")
		timed +=1
		time.sleep(3)
		plt.close()
		print("closed")

AccelPlot()
