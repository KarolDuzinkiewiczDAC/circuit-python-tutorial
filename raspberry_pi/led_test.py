import board
import digitalio
import time

# NOTE: This requires LED connected to GOPIO18 with a resitor conected to GND in series

led = digitalio.DigitalInOut(board.D18)
led.direction = digitalio.Direction.OUTPUT

while True:
    led.value = True
    time.sleep(0.5)
    led.value = False
    time.sleep(0.5)
