# CircuitPython Tutorial

This is a repository for illustrating different usages of CircuitPython.

Currently is includes examples for:
* Raspberry Pi (`cicruit-python-tutorial/raspberry_pi`)

## Raspberry Pi

### Prerequisites

Setup your Raspberry Pi & install Blinka. See https://learn.adafruit.com/circuitpython-on-raspberrypi-linux/installing-circuitpython-on-raspberry-pi for more details.

The easiest way to interact with the code on Raspberry Pi is to use **Visual Studio Code** and the **Remote - SSH extension** to conveniently edit the source code on your local computer but be able to run it on the target device (i.e. Raspberry Pi). For more details on installing Remote - SSH extension see https://code.visualstudio.com/docs/remote/ssh. 

TBD...

## Adafruit ESP32-S3 Feather

Setup your ESP32-S3 Feather and install CicruitPython. See https://learn.adafruit.com/adafruit-esp32-s3-feather/circuitpython for more details.

When CircuitPython is correctly installed, the board connected over USB will be manifested by a `CIRCUITPY` drive. In order for your code to work you would need to drag-and-drop the `code.py` file onto this drive each time you make a change. 

**NOTE:** The name of the file is important - it has to be named `code.py`.
**NOTE:** Once the `code.py` file changes the boards resets and the code is executed right after boot up.
