"""
Title        : RetroPie-Coin
Author       : zzeromin, member of Raspberrypi Village and Tentacle Team
Creation Date: Oct 15, 2017
Cafe         : http://cafe.naver.com/raspigamer
Blog         : http://rasplay.org, http://forums.rasplay.org/, https://zzeromin.tumblr.com/
Github       : https://github.com/rasplay, https://github.com/zzeromin
Thanks to    : Team Tentacle
Free and open for all to use. But put credit where credit is due.
"""

import RPi.GPIO as GPIO
import time

# check your SELECT gpio(BCM) pin number at https://pinout.xyz/
# Joysticks connected to GPIOs at https://github.com/recalbox/mk_arcade_joystick_rpi
SELECT = 21 # GPIO Pin Number
SENSOR = 29 # GPIO Pin Number
DELAY = 1

GPIO.setmode(GPIO.BOARD)

GPIO.setup(SENSOR, GPIO.IN)
GPIO.setup(SELECT, GPIO.OUT)
try:
	while True:
        
		if GPIO.input(SENSOR) == GPIO.LOW:
			if DELAY == 1:
				time.sleep(0.5)
				GPIO.output(SELECT, GPIO.LOW) # select ON           	
				time.sleep(0.05)
				DELAY=0
				#print "Coin Detected"
			else:
				GPIO.output(SELECT, GPIO.LOW) # select ON            
		else:
			DELAY=1
			GPIO.output(SELECT, GPIO.HIGH) # select OFF
			time.sleep(0.05)
			#print "Coin no detected"
            

except KeyboardInterrupt:
    GPIO.stop()
