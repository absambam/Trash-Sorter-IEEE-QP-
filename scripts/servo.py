import RPi.GPIO as GPIO
import time

p = 0

def tilt():
  print('initializing servo...')
  servoPIN = 12
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(servoPIN, GPIO.OUT)

  p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
  p.start(2.5) # Initialization
  for dc in range(0, 18, 1):
    p.ChangeDutyCycle(float(float(2.5)+float(dc/5.0)))
    # print(float(float(2.5)+float(dc/5.0)))
    time.sleep(0.05)
  p.ChangeDutyCycle(2.5)
  time.sleep(0.5)

  p.stop()

if __name__ == "__main__":
  tilt()
