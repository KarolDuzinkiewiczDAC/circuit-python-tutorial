# NOTE: This does not work for UGeek Stepper Motor HAT v.0.2
# NOTE: This will work only for Adafruit's Raspberry Pi Motor HAT (https://learn.adafruit.com/adafruit-dc-and-stepper-motor-hat-for-raspberry-pi)
# NOTE: You need to connect DC motor to M1, also for bigger motors you need to provide external power.

import time
import board
import pwmio
from adafruit_motor import servo

DEGREES_STEP = 5
MIN_ANGLE_IN_DEGREES = 0
MAX_ANGLE_IN_DEGREES = 180

# create a PWMOut object on Pin D5.
pwm = pwmio.PWMOut(board.D5, duty_cycle=2 ** 15,  frequency=50)

# create a servo object
servo = servo.Servo(pwm)

# move the servo back and fourth by 5 degrees
while True:
    # 0 - 180 degrees, 5 degrees at a time.
    for angle in range(MIN_ANGLE_IN_DEGREES, MAX_ANGLE_IN_DEGREES, DEGREES_STEP):  
        servo.angle = angle
        time.sleep(0.2)
    
    # 180 - 0 degrees, 5 degrees at a time.
    for angle in range(MAX_ANGLE_IN_DEGREES, MIN_ANGLE_IN_DEGREES, -DEGREES_STEP):
        servo.angle = angle
        time.sleep(0.2)