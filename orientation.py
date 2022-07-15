#Grant Sims
#July 13, 2022

import time
import os
import board
import numpy as np
import busio
import math
import adafruit_fxos8700
import adafruit_fxas21002c

i2c = busio.I2C(board.SCL, board.SDA)
fxos = adafruit_fxos8700.FXOS8700(i2c)
fxas = adafruit_fxas21002c.FXAS21002C(i2c)

orientation = [0.0, 0.0, 0.0]
magCal = [-49.85, -56.2, -85.8]
gyroCal = [0.0158, 0.0035, -0.03]


def get_attitude():
    prev_time = time.time()
    accelVals = get_accel()
    yaw = get_magnet()
    time.sleep(0.01)
    gyroX, gyroY, gyroZ = fxas.gyroscope
    gyro = [gyroX, gyroY, gyroZ]
    curr_time = time.time()


    deltaAngle = [gyro[0] * (curr_time-prev_time), gyro[1] * (curr_time-prev_time), gyro[2] * (curr_time-prev_time)]
    prev_time = curr_time
    orientation[0] = 0.98 * (orientation[0] + deltaAngle[0]) + 0.02*accelVals[0]
    orientation[1] = 0.98 * (orientation[1] + deltaAngle[1]) + 0.02*accelVals[1]
    orientation[2] = 0.98 * (orientation[2] + deltaAngle[2]) + 0.02*yaw

    #orientation[0] *= -1 #flip pitch reading. Messes up entire code for some reason. Need to debug

    orientationDegrees = [i * 180/math.pi for i in orientation]
    print('pitch: ', orientationDegrees[0], ' roll: ', orientationDegrees[1], ' yaw: ', orientationDegrees[2])
    return orientation
    

def get_accel():
    accelX, accelY, accelZ = fxos.accelerometer
    accel = [accelX, accelY, accelZ]
    roll = math.atan2(accelY, accelZ)
    pitch = math.atan2(-accelX, math.sqrt(accelY*accelY + accelZ * accelZ))
    #print('roll: ', roll*180/math.pi, ' pitch: ', pitch*180/math.pi)
    return [roll, pitch]
    #time.sleep(0.01)

def get_magnet():
    magnetX, magnetY, magnetZ = fxos.magnetometer
    magnet = [magnetX - magCal[0], magnetY - magCal[1], magnetZ - magCal[2]]
    accelVals = get_accel()
    roll = accelVals[0]
    pitch = accelVals[1]
    yCompensated = (magnet[0]*math.cos(pitch))+(magnet[1]*math.sin(pitch)*math.sin(roll)) + (magnet[2]*math.cos(roll) * math.sin(pitch))
    xCompensated = (-1.0*magnet[1] * math.cos(roll)) + (magnet[2]*math.sin(roll))
    yaw = math.atan2(xCompensated, yCompensated)
    #orientation compensation
    if yaw <0: yaw += math.pi
    else: yaw -= math.pi
    print(yaw*180/math.pi)
    return yaw



print('code runs')
while True:
    get_attitude()
    #get_magnet()

    #time.sleep(0.05)
