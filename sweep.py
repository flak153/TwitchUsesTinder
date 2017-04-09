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
myServo = Servo("First Servo")

# Attaches the servo to pin 3 in Arduino Expansion board
myServo.attach(3)

# Print servo settings


@app.route('/left')
def left():
    for angle in range(90, 180):
        myServo.write(angle)
        time.sleep(0.005)
    for angle in range(180, 90, -1):
        myServo.write(angle)
        time.sleep(0.005)


    return "Done"

@app.route('/right')
def right():
    for angle in range(90, 0, -1):
        myServo.write(angle)
        time.sleep(0.005)

        # From 180 to 0 degrees
    for angle in range(0, 90,):
        myServo.write(angle)
        time.sleep(0.005)
    return "Done"

if __name__ == "__main__":
    myServo.write(90)
    app.run(host='0.0.0.0', port=8000)
