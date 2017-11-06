#!/usr/bin/python

# This is a file that shows how to turn off GIPO pins

import RPi.GPIO as GPIO
import time

# Set the Pin Schema
GPIO.setmode(GPIO.BCM)
# Cleanup
GPIO.cleanup()
# Turn off warnings
GPIO.setwarnings(False)

# Setup pins
GPIO.setup(17, GPIO.OUT)
# GPIO.setup(27, GPIO.OUT)

print "Lights off!"

# Turn on the pins
GPIO.output(17, GPIO.LOW)
# GPIO.output(27, GPIO.HIGH)

for i in range(10):
	print "Blink On " + str(i) 
	GPIO.output(17, GPIO.HIGH)
	time.sleep(1)
	print "Blink off " + str(i)
	GPIO.output(17, GPIO.LOW)
	time.sleep(1)

GPIO.cleanup()
