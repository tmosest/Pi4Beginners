#!/usr/bin/python

# This is a file that shows how to turn off GIPO pins

import RPi.GPIO as GPIO

# Set the Pin Schema
GPIO.setmode(GPIO.BCM)
# Cleanup
GPIO.cleanup()
# Turn off warnings
GPIO.setwarnings(False)

# Setup pins
GPIO.setup(17, GPIO.OUT)
# GPIO.setup(27, GPIO.OUT)

print "Lights on!"

# Turn on the pins
GPIO.output(17, GPIO.HIGH)
# GPIO.output(27, GPIO.HIGH)
