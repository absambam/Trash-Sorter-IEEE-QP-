# https://learn.adafruit.com/adafruits-raspberry-pi-lesson-8-using-a-servo-motor/software
import time
import wiringpi

wiringpi.wiringPiSetupGpio()

# Set pin #18 to be a PWM output by doing the following on command line:
# gpio -g mode 18 pwm. (if not using pin #18, just change value.)

wiringpi.pinMode(18, wiringpi.GPIO.PWM_OUTPUT)
wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)

# Servos need a 50Hz frequency output
# so 19200000Hz/pwmClock/pwmRange = 50
# set pwmClock to 192 and pwmRange to 2000 for now,
# but feel free to change numbers as long as we get
# a 50Hz output.
# make sure to write on command line:
# gpio pwm-ms
# gpio pwmc 192
# gpio pwmr 2000

wiringpi.pwmSetClock(192)
wiringpi.pwmSetRange(2000)

# gpio -g 18 100 to wet ervo to all the way to left
# gpio -g pwm 18 150 to middle
# gpio -g pwm 18 200
# face left = 1.0ms, face up = 1.5ms, face right = 2.0ms
delay_period = 0.01

# sudo apt-get install -y python-pip
# sudo pip instll wiringpi
#nano servo.py
