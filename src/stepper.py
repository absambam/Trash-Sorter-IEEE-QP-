import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

enable_pin = 18
coil_A_1_pin = 4
coil_A_2_pin = 17
coil_B_1_pin = 23
coil_B2_pin = 24

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

# rotate 1, 2, 3, or 4 * 90 degrees
# rotations is a value between 1 to 4 corresponding to the number of quarters
# to rotate.
def rotate( int rotations )
    delay = .25
    steps = 128 #128 = 90 degree rotation
    print("Preparing to move ", rotations*steps, " steps...")
    forward(delay, steps*rotations)
    print("Moved " rotations*steps, " steps")
