# https://learn.adafruit.com/adafruits-raspberry-pi-lesson-8-using-a-servo-motor/software
  2 import time
  3 import wiringpi
  4 
  5 wiringpi.wiringPiSetupGpio()
  6 
  7 # Set pin #12 to be a PWM output by doing the following on command line:
  8 # gpio -g mode 12 pwm. (if not using pin #18, just change value.)
  9 
 10 wiringpi.pinMode(18, wiringpi.GPIO.PWM_OUTPUT)
 11 wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)
 12 
 13 # Servos need a 50Hz frequency output
 14 # so 19200000Hz/pwmClock/pwmRange = 50
 15 # set pwmClock to 192 and pwmRange to 2000 for now,
 16 # but feel free to change numbers as long as we get
 17 # a 50Hz output.
 18 # make sure to write on command line:
 19 # gpio pwm-ms
 20 # gpio pwmc 192
 21 # gpio pwmr 2000
 22 
 23 wiringpi.pwmSetClock(192)
 24 wiringpi.pwmSetRange(2000)
 25 
 26 # gpio -g 18 100 //to set servo to all the way to left
 27 # gpio -g pwm 18 150 //to middle
 28 # gpio -g pwm 18 200
 29 # face left = 1.0ms, face up = 1.5ms, face right = 2.0ms
 30 delay_period = 0.05
 31 return_delay = 0.01
 32 
 33 # sudo apt-get install -y python-pip
 34 # sudo pip instll wiringpi
 35 #nano servo.py
 36 
 37 for pulse in range(50, 116, 1):
 38     wiringpi.pwmWrite(18, pulse)
 39     time.sleep(delay_period)
 40 
 41 for pulse in range(116, 50, -1):
 42     wiringpi.pwmWrite(18, pulse)
 43     time.sleep(return_delay)
