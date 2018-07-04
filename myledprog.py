#!/usr/bin/env python


import RPi.GPIO as GPIO
import time

slidePin = 17
led1Pin = 18
led2Pin = 27

GPIO.setwarnings(False)

def print_message():
	print ("========================================")
	print ("|              Slide Switch            |")
	print ("|    ------------------------------    |")
	print ("|      Middle pin of slide switch      |")
	print ("|         connect to gpio0;            |")
	print ("|                                      |")
	print ("|slide switch to contral which led on. |")
	print ("|                                      |")
	print ("|                            SunFounder|")
	print ("========================================\n")
	print 'Program is running...'
	print 'Please press Ctrl+C to end the program...'
	raw_input ("Press Enter to begin\n")

# Define a setup function for some setup
def setup():
	# Set the GPIO modes to BCM Numbering
#	GPIO.cleanup()
	GPIO.setmode(GPIO.BCM)
	# Set slidePin input
	# Set ledPin output, 
	# and initial level to High(3.3v)
	GPIO.setup(slidePin, GPIO.OUT, initial=GPIO.HIGH)
	GPIO.setup(led1Pin, GPIO.IN)
	GPIO.setup(led2Pin, GPIO.IN)

def main():
	# Print messages
#	print_message()
	while True:
		if GPIO.input(led1Pin) == 1:
#			print ("ALEXA")
			return "ALEXA"
		if GPIO.input(led2Pin) == 1:
#			print ("GOOGLE")
			return "GOOGLE"
def destroy():
	# Release resource
	GPIO.cleanup()
#	print "it terminated correctly"
#If run this script directly, do:
if __name__ == '__main__':
	setup()
	Result = main()
	print Result
#	file = open("testfile.txt","w")
#	file.write(Result)
#	file.close()
	# When 'Ctrl+C' is pressed, the child program
	# destroy() will be  executed.
	destroy()
#	print "it terminated correctly"
