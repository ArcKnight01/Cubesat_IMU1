import time
import os
import board
import busio
import adafruit_fxos8700


i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_fxos8700.FXOS8700(i2c)


while True:
    accelX, accelY, accelZ = sensor.accelerometer
    magnetX, magnetY, magnetZ = sensor.magnetic
    gyroX, gyroY, gyroZ = sensor.gyro
    gravityX, gravityY, gravityZ = sensor.gravity

    print('accelX':, accelX)


print('code runs')
