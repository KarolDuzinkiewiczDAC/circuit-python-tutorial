# NOTE: This script uses a built-in LED, so no additional HW elements are
#       required for it to work.

import board
import digitalio
import time

# configure built-in red LED
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

# turn the LED on and off in a loop
while True:
    # turn LED on
    led.value = True
    time.sleep(1.0)

    # turn LED off
    led.value = False
    time.sleep(0.5)
