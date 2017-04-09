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
def hello_world():
            # From 0 to 180 degrees
        for angle in range(0, 180):
            myServo.write(angle)
            time.sleep(0.005)

        return "Done"

@app.route('/right')
def hello_world():
        for angle in range(180, -1, -1):
            myServo.write(angle)
            time.sleep(0.005)
        return "Done"


