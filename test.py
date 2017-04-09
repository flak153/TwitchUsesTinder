from Servo import *
import time, sys
leftRight = Servo("First Servo")
upDown = Servo("Second Servo")
# Attaches the servo to pin 3 in Arduino Expansion board
leftRight.attach(3)
upDown.attach(5)

for angle in range(45, 135):
    leftRight.write(angle)
    time.sleep(0.005)
for angle in range(135, 45, -1):
    leftRight.write(angle)
    time.sleep(0.005)

for angle in range(45, 135):
    upDown.write(angle)
    time.sleep(0.005)
for angle in range(135, 45, -1):
    upDown.write(angle)
    time.sleep(0.005)