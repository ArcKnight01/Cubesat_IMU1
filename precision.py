import time
import os
import board
import busio
import adafruit_fxos8700
import adafruit_fxas21002c

i2c = busio.I2C(board.SCL, board.SDA)
accelerometer = adafruit_fxos8700.FXOS8700(i2c)
gyroscope = adafruit_fxas21002c.FXAS21002C(i2c)

def checkPrecision(testAccel, testGyro, sampleLength):
    """This function checks the precision of the accelerometer/magnometer
    connected to the Raspberry Pi. Leave the sensor on a flat surface 
    and do not disturb it while the test is running.

    Args:
        testAccel: The accelerometer that is being tested. Must be anadafruit_fxos8700.FXOS8700 sensor object.
        testGyro: The gyroscope that is being tested. Must be adafruit_fxas21002c.FXAS21002C sensor object.
        sampleLength: The ammount of time for which the test should be carried out in seconds. Must be an integer. 
    
    Returns:
        The average deviation from the calibrated values in all axis and 
        sensor modes during the sample time as a string. For example:
            checkPrecision(sensor,2) -> 

    Raises:
        AssertionError: Raised when incorrect sensor object is inputted or sample time in not an integer
    """
    assert type(testAccel) is adafruit_fxos8700.FXOS8700 and type(testGyro) is adafruit_fxas21002c.FXAS21002C and type(sampleLength) is int

    aXlist, aYlist, aZlist, gXlist, gYlist, gZlist = ([] for i in range(6))
    sensVals = [accelX,accelY,accelZ,gyroX,gyroY,gyroZ]
    valsToList = {accelX:aXlist, accelY:aYlist, accelZ:aZlist, gyroX:gXlist, gyroY:gYlist, gyroY:gYlist}

    end = time.time_ns() + sampleLength*1000000000
    
    while time.time_ns() < end:
        accelX, accelY, accelZ = testAccel.accelerometer
        gyroX, gyroY, gyroZ = testGyro.gyroscope
        for val in sensVals:
            valsToList[val].append(val)
    print(aXlist)

checkPrecision(accelerometer,gyroscope,5)

    

