#NeilNoronha

#July 13, 2022

import time
import os
import board
import busio
import adafruit_fxos8700

i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_fxos8700.FXOS8700(i2c)


def senseVals ():
    """This code prints out the acceleration values the IMU is reading once per second."""
    while True:
        print(str(round(sensor.accelerometer[0],4)) + "m/s^2",
        str(round(sensor.accelerometer[1],4))+"m/s^2",
        str(round(sensor.accelerometer[2],4))+"m/s^2")
        time.sleep(1)

senseVals()
