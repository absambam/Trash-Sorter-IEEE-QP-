import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

# constants
num_bins = 3
steps = 171 #170.666
total_steps = 512

delay = 0.001

control_pins = [7,11,13,15]
for pin in control_pins:
  GPIO.setup(pin, GPIO.OUT)
  GPIO.output(pin, 0)

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

backward_halfstep_seq = [
  [1,0,0,0],
  [1,0,0,1],
  [0,0,0,1],
  [0,0,1,1],
  [0,0,1,0],
  [0,1,1,0],
  [0,1,0,0],
  [1,1,0,0],
  [1,0,0,0],
]

def forward(delay, steps):
  for i in range(steps):
    for fwdhalfstep in range(8):
      for pin in range(4):
        GPIO.output(control_pins[pin], forward_halfstep_seq[fwdhalfstep][pin])
      time.sleep(delay)

def backward(delay, steps):
  for i in range(steps):
    for bwdhalfstep in range(8):
      for pin in range(4):
        GPIO.output(control_pins[pin], backward_halfstep_seq[bwdhalfstep][pin])
      time.sleep(delay)

def rotate( bin_name ):
  destination = 0
  if bin_name == "recycling":
    destination = 1
  elif bin_name == "compost":
    destination = 2
  print("Preparing to move ", destination*steps, " steps to bin ", destination )
  forward(delay, steps*destination)
  time.sleep(5)
  #return to position 0
  print("Returning to position 0")
  forward(delay, steps*(num_bins-destination))
  #backward(delay, 1)
  #current_bin -= num_bins
  #position += rotations*steps
  #if position > total_steps: #prevent going over 512 degrees
  #  position -= total_steps

rotate("recycling")
GPIO.cleanup()
