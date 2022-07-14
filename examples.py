#How to use the IMU

#impoerting libraries
import board
import busio
import adafruit_fxos8700
import adafruit_fxas21002c

#define I2C connection as well as accelerometer and gyroscope sensor objects
i2c = busio.I2C(board.SCL, board.SDA)
accelerometer = adafruit_fxos8700.FXOS8700(i2c)
gyroscope = adafruit_fxas21002c.FXAS21002C(i2c)

#---ACCELEROMETER EXAMPLES---#

#To get the accelerometer values as a tuple, use '.accelerometer'.
#This will come in the format (X,Y,Z) which can be split into several variables as shown below.
X,Y,Z = accelerometer.accelerometer
print(f"Accelerometer output ---> X: {X} m/s^2 | Y: {Y} m/s^2 | Z: {Z} m/s^2")

#---MAGNOMETER EXAMPLES---#

#To get the magnometer values as a tuple, use '.magnometer'.
#This will come in the format (X,Y,Z) which can be split into several variables as shown below.
X,Y,Z = accelerometer.magnetometer
print(f"Magnometer output ---> X: {X} μT | Y: {Y} μT | Z: {Z} μT")

#---GYROSCOPE EXAMPLES---#
#IMPORTANT: MAKE SURE YOU ARE USING THE GYROSCOPE SENSOR OBJECT

#To get the gyroscope values as a tuple, use '.gyroscope'.
#This will come in the format (X,Y,Z) which can be split into several variables as shown below.
X,Y,Z = accelerometer.magnetometer
print(f"Magnometer output ---> X: {X} μT | Y: {Y} μT | Z: {Z} μT")

print(gyroscope._device.i2c)