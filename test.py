from Servo import *
import time, sys
leftRight = Servo("First Servo")
upDown = Servo("Second Servo")
# Attaches the servo to pin 3 in Arduino Expansion board
leftRight.attach(3)
upDown.attach(5)

leftRight.write(90)
time.sleep(0.01)
upDown.write(90)
time.sleep(0.01)