import time
import os
import board
import busio
import adafruit_fxos8700

i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_fxos8700.FXOS8700(i2c)

def checkPrecision(testSensor, sampleLength):
    """This function checks the precision of the accelerometer/magnometer
    connected to the Raspberry Pi. Leave the sensor on a flat surface 
    and do not disturb it while the test is running.

    Args:
        testSensor: The sensor that is being tested. Must be anadafruit_fxos8700.FXOS8700 sensor object.
        sampleLength: The ammount of time for which the test should be carried out in seconds. Must be an integer. 
    
    Returns:
        The average deviation from the calibrated values in all axis and 
        sensor modes during the sample time as a string. For example:
            checkPrecision(sensor,2) -> 

    Raises:
        AssertionError: Raised when incorrect sensor object is inputted or sample time in not an integer
    """
    assert type(testSensor) is adafruit_fxos8700.FXOS8700 and type(sampleLength) is int

    end = time.time_ns() + sampleLength*1000000000
    
    while time.time_ns() < end:
        accelX, accelY, accelZ = testSensor.accelerometer
    print(accelX)

checkPrecision(sensor,5)

    

