#Nevin Thinagar
#July 13, 2022

import time
import os
import board
import busio
import numpy as np
import adafruit_fxos8700
import adafruit_fxas21002c

i2c = busio.I2C(board.SCL, board.SDA)
accelerometer = adafruit_fxos8700.FXOS8700(i2c)
gyroscope = adafruit_fxas21002c.FXAS21002C(i2c)

def checkPrecision(testAccel, testGyro, sampleLength = 1, zeroG = False):
    """This function checks the precision of the accelerometer/magnometer
    connected to the Raspberry Pi. Leave the sensor on a flat surface 
    and do not disturb it while the test is running.

    Args:
        testAccel: The accelerometer that is being tested. Must be anadafruit_fxos8700.FXOS8700 sensor object.
        testGyro: The gyroscope that is being tested. Must be adafruit_fxas21002c.FXAS21002C sensor object.
        sampleLength: The duration for which the test should be carried out in seconds. Must be an integer, default time is 1 second.
        zeroG: Set value as true to ignore the effect of gravity on accelerometer. Set to False if left empty. 
    
    Returns:
        The average deviation from the calibrated values in all axis and 
        sensor modes during the sample time as a dictionary in the format {'Accelerometer':[X,Y,Z], 'Gyroscope':[X,Y,Z]} 
        where X, Y, and Z are floats. For example:
            checkPrecision(accel,gyro,2) -> {'Accelerometer':[0.123,-1.234 ,0.123],'Gyroscope':[0.00123,0.00123,0.00123]}

    Raises:
        AssertionError: Raised when incorrect sensor objects are inputted or the sample time is not an integer
    """
    assert type(testAccel) is adafruit_fxos8700.FXOS8700 and type(testGyro) is adafruit_fxas21002c.FXAS21002C and type(sampleLength) is int
    
    sumAccel, sumGyro = (np.array([0.0,0.0,0.0]) for i in range(2))

    end = time.time_ns() + sampleLength*1000000000
    reps = 0
    
    while time.time_ns() < end:
        sumAccel += np.array(testAccel.accelerometer)
        sumGyro += np.array(testGyro.gyroscope)
        reps += 1

    sumAccel = sumAccel/reps
    sumGyro = sumGyro/reps

    if zeroG == False:
        sumAccel -= np.array([0.0,0.0,9.81])

    out = {}
    
    out.update({'Accelerometer':(sumAccel.tolist())})
    out.update({'Gyroscope':(sumGyro.tolist())})
    print(out)
    return out