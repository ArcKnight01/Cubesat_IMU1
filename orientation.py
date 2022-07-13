import time
import os
import board
import busio
import adafruit_fxos8700
import adafruit_fxas21002c

i2c = busio.I2C(board.SCL, board.SDA)
fxos = adafruit_fxos8700.FXOS8700(i2c)
fxas = adafruit_fxas21002c.FXAS21002C(i2c)

while True:
    accelX, accelY, accelZ = fxos.accelerometer
    magnetX, magnetY, magnetZ = fxos.magnetometer
    gyroX, gyroY, gyroZ = fxas.gyroscope


    #gyroX, gyroY, gyroZ = sensor.gyro
    #gravityX, gravityY, gravityZ = sensor.gravity

    print('gyroX:', gyroX, ' gyroY:', gyroY, ' gyroZ:', gyroZ)
    time.sleep(1)


print('code runs')
