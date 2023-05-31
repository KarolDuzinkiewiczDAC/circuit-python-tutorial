# NOTE: Use serial console to be able to see the output & input stuff in the
#       terminal to interact with the board.

import time

while True:
    print('What\'s your name?')
    name = input()
    print(f'Hello, {name}. Nice to meet you :)')
    time.sleep(0.5)
