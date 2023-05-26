import board
import digitalio
import time

# NOTE: This requires a button/switch conected to GPIO4 and GND

# connect button to GPIO4
button_1 = digitalio.DigitalInOut(board.D4)
button_1.direction = digitalio.Direction.INPUT
# enable a built-in pull-up resistor
button_1.pull = digitalio.Pull.UP

while True:
    if not button_1.value:
        # NOTE: Since we are using a internal pull-up resistor on the GPIO the pin will be 
        #       in a 'high' state by default, which corresponds to button_1.value == True.
        #       Once the button is pressed: button_1.value == False.
        print('Button pressed')
    else:
        print('Button released')

    time.sleep(0.5)
