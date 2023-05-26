# NOTE: This does not work for UGeek Stepper Motor HAT v.0.2
# NOTE: This will work only for Adafruit's Raspberry Pi Motor HAT (https://learn.adafruit.com/adafruit-dc-and-stepper-motor-hat-for-raspberry-pi)
# NOTE: You need to connect DC motor to M1, also for bigger motors you need to provide external power.

import time
from adafruit_motorkit import MotorKit

kit = MotorKit()

while True:
    kit.motor1.throttle = 1.0
    time.sleep(0.5)
    kit.motor1.throttle = 0
    time.sleep(0.5)
