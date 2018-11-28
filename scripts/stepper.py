import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

enable_pin = 18
coil_A_1_pin = 4
coil_A_2_pin = 17
coil_B_1_pin = 23
coil_B2_pin = 24

# constants
num_bins = 3
delay = 0.25
steps = 171 #170.666666
total_steps = 512

# global vars
current_bin = 0 #trash = 0, recycling = 1, compost = 2
position = 0


GPIO.setup(enable_pin, GPIO.OUT)
GPIO.setup(coil_A_1_pin, GPIO.OUT);
GPIO.setup(coil_A_2_pin, GPIO.OUT);
GPIO.setup(coil_B_1_pin, GPIO.OUT);
GPIO.setup(coil_B_2_pin, GPIO.OUT);

GPIO.output(enable_pin, 1)

def forward(delay, steps):
    for i in range(0, steps):
        setStep(1, 0, 1, 0)
        time.sleep(delay)
        setStep(0, 1, 1, 0)
        time.sleep(delay)
        setStep(0, 1, 0, 1)
        time.sleep(delay)
        setStep(1, 0, 0, 1)


def backwards(delay, steps):
    for i in range(0, steps):
        setStep(1, 0, 0, 1)
        time.sleep(delay)
        setStep(0, 1, 0, 1)
        time.sleep(delay)
        setStep(0, 1, 1, 0)
        time.sleep(delay)
        setStep(1, 0, 1, 0)

def setStep(w1, w2, w3, w4):
    GPIO.output(coil_A_1_pin, w1)
    GPIO.output(coil_A_2_pin, w2)
    GPIO.output(coil_B_1_pin, w3)
    GPIO.output(coil_B_2_pin, w4)

# rotate 1, 2, or 3 * 120 degrees
# bin_name is a string with any of the three values trash, recycling, or compost

def rotate( bin_name ):
    destination = 0
    if bin_name == "recycling":
        destination = 1
    elif bin_name == "compost":
        destination = 2
    rotations = ((360 + (destination - current_bin)*120) % 360) / 120
    current_bin = rotations + current_bin
    print("Preparing to move ", rotations*steps, " steps...")
    forward(delay, steps*rotations)
    if current_bin >= num_bins:
        backwards(delay, 1)
        current_bin -= num_bins
    position += rotations*steps
    if position > total_steps: #prevent going over 512 degrees
        position -= total_steps
    print("Moved " rotations*steps, " steps. Now at position ", position, "steps and at bin ", current_bin)
