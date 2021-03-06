from label_image import process_picture
import RPi.GPIO as GPIO
import time

# constants
num_bins = 3
steps = 171 #170.666
total_steps = 512

delay = 0.001
p = 0
servoPIN = 12
control_pins = [4,17,27,22] #for GPIO.BCM
#control_pins = [7,11,13,15] for GPIO.BOARD

GPIO.setmode(GPIO.BCM)

forward_halfstep_seq = [
  [1,0,0,0],
  [1,1,0,0],
  [0,1,0,0],
  [0,1,1,0],
  [0,0,1,0],
  [0,0,1,1],
  [0,0,0,1],
  [1,0,0,1]
]

def init_button():
  GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def init_stepper():
  for pin in control_pins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, 0)

def init_servo():
  GPIO.setup(servoPIN, GPIO.OUT)


def tilt():
  print('initializing servo...')
  init_servo()
  p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
  p.start(2.5) # Initialization
  for dc in range(0, 18, 1):
    p.ChangeDutyCycle(float(float(2.5)+float(dc/5.0)))
    time.sleep(0.05)
  p.ChangeDutyCycle(2.5)
  time.sleep(0.5)

  p.stop()

def forward(delay, steps):
  for i in range(steps):
    for fwdhalfstep in range(8):
      for pin in range(4):
        GPIO.output(control_pins[pin], forward_halfstep_seq[fwdhalfstep][pin])
      time.sleep(delay)


def rotate( bin_name ):
  init_stepper()
  destination = 0
  if bin_name == "recycling":
    destination = 1
  elif bin_name == "compost":
    destination = 2
  print("Preparing to move ", destination*steps, " steps to bin ", destination )
  forward(delay, steps*destination)
  tilt()
  time.sleep(5)

  #return to position 0
  print("Returning to position 0")
  if destination != 0:
    init_stepper()
    forward(delay, steps*(num_bins-destination))

init_button()
while True:
  input_state = GPIO.input(18)
  if input_state == False:
    print('boop UwU')
    label = process_picture()
    print(label)
    rotate(label)
    init_button()
    time.sleep(0.2)

