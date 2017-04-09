from Servo import *
import time, sys
leftRight = Servo("First Servo")
upDown = Servo("Second Servo")
# Attaches the servo to pin 3 in Arduino Expansion board
leftRight.attach(3)
upDown.attach(5)

for angle in range(90, int(sys.argv[1])):
    leftRight.write(angle)
    time.sleep(0.005)

time.sleep(1)

for angle in range(90, int(sys.argv[2])):
    upDown.write(angle)
    time.sleep(0.005)

leftRight.write(90)
upDown.write(90)