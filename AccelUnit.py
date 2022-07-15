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
        print("X: " + str(round(sensor.accelerometer[0],9)) + "m/s^2",
        "Y: " + str(round(sensor.accelerometer[1],9))+"m/s^2",
        "Z: " + str(round(sensor.accelerometer[2],9))+"m/s^2")
        time.sleep(1)

senseVals()
