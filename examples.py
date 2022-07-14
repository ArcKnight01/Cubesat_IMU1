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
#Round all values to 9 decimal places as additional digits are not accurate recorded data.
aX,aY,aZ = accelerometer.accelerometer
ax = round(aX,9)
aY = round(aY,9)
aZ = round(aZ,9)
print(f"Accelerometer output ---> X: {aX} m/s^2 | Y: {aY} m/s^2 | Z: {aZ} m/s^2")

#To measure the vertical acceleration without the addition of gravity simply subtract 9.80665 from the Z axis value as shown below
print(f"Vertical acceleration without gravity: {ax-9.80665} m/s^2")

#To convert the acceleration into G forces, divide the m/s^s value by 9.80665 as shown below
print(f"Acceleration as G Force -> X: {round(aX/9.80665,5)} G | Y: {round(aY/9.80665,5)} G | Z: {round(aZ/9.80665,5)} G")

#---MAGNOMETER EXAMPLES---#

#To get the magnometer values as a tuple, use '.magnometer'.
#This will come in the format (X,Y,Z) which can be split into several variables as shown below.
#Round all values to 1 decimal place as additional digits are not accurate recorded data.
mX,mY,mZ = accelerometer.magnetometer
mx = round(mX,1)
mY = round(mY,1)
mZ = round(mZ,1)
print(f"Magnometer output ---> X: {mX} μT | Y: {mY} μT | Z: {mZ} μT")

#---GYROSCOPE EXAMPLES---#
#IMPORTANT: MAKE SURE YOU ARE USING THE GYROSCOPE SENSOR OBJECT

#To get the gyroscope values as a tuple, use '.gyroscope'.
#This will come in the format (X,Y,Z) which can be split into several variables as shown below.
gX,gY,gZ = gyroscope.gyroscope
print(f"Gyroscope output ---> X: {gX} rad/s | Y: {gY} rad/s | Z: {gZ} rad/s")