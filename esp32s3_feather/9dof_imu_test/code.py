import adafruit_bno08x
from adafruit_bno08x.uart import BNO08X_UART
from adafruit_bno08x import BNO_REPORT_ROTATION_VECTOR
import time
import board
import busio

# configure BNO08x breakout board to use UART for communication
# NOTE: BNO08x's I2C implementation violates some aspects of I2C protocol so
#       it does not play nicely with ESP32-S3 Feather board
#       (i.e. misleading 'no pull up resistor' error ).
uart = busio.UART(board.TX, board.RX, baudrate=3000000, receiver_buffer_size=2048)

bno = BNO08X_UART(uart)
print('Connection to BNO08x established')

bno.enable_feature(BNO_REPORT_ROTATION_VECTOR)
print('Rotation Vector Quaterion report enabled')

while True:
    print("Rotation Vector Quaternion:")
    quat_i, quat_j, quat_k, quat_real = bno.quaternion
    print("I: %0.6f  J: %0.6f K: %0.6f  Real: %0.6f" % (quat_i, quat_j, quat_k, quat_real))
    time.sleep(1.0)
