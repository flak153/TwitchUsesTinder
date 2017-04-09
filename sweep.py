#!/usr/bin/env python

"""
Sweep.py

This example shows how to use a servo motor attached to a PWM pin.

This example code is in the public domain.

Revision History
----------------------------------------------------------
    Author		   Date		  Description
----------------------------------------------------------
Diego Villalobos	02-12-2015	Example created

"""

# Libraries required
from Servo import *
import time
from flask import Flask
app = Flask(__name__)

# Create a new servo object with a reference name
leftRight = Servo("First Servo")
upDown = Servo("Second Servo")

# Attaches the servo to pin 3 in Arduino Expansion board
leftRight.attach(3)
upDown.attach(5)

# Print servo settings


@app.route('/left')
def left():
    for angle in range(90, 110):
        leftRight.write(angle)
        time.sleep(0.005)
    for angle in range(70, 120):
        upDown.write(angle)
        time.sleep(0.005)

    for angle in range(120, 70, -1):
        upDown.write(angle)
        time.sleep(0.005)
    for angle in range(110, 90, -1):
        leftRight.write(angle)
        time.sleep(0.005)


    return "Done"

@app.route('/right')
def right():
    for angle in range(90, 70, -1):
        leftRight.write(angle)
        time.sleep(0.005)
    for angle in range(70, 120):
        upDown.write(angle)
        time.sleep(0.005)

    for angle in range(120, 70, -1):
        upDown.write(angle)
        time.sleep(0.005)
    for angle in range(70, 90):
        leftRight.write(angle)
        time.sleep(0.005)
    return "Done"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
