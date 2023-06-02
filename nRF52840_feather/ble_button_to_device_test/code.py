# NOTE: This script receives button presses from Bluefruit LE Connect
#       app's Control Pad and prints out relevant info on the screen.

from adafruit_ble import BLERadio
from adafruit_ble.advertising.standard import ProvideServicesAdvertisement
from adafruit_ble.services.nordic import UARTService

from adafruit_bluefruit_connect.packet import Packet
from adafruit_bluefruit_connect.button_packet import ButtonPacket

# initialize BLE
ble = BLERadio()
uart = UARTService()
advertisement = ProvideServicesAdvertisement(uart)

while True:

    # start advertising and wait for connection
    ble.start_advertising(advertisement)
    print('BLE advertising...')
    while not ble.connected:
        pass

    print('BLE connection to central established')

    while ble.connected:
        if uart.in_waiting:
            packet = Packet.from_stream(uart)
            if isinstance(packet, ButtonPacket):
                if packet.pressed:
                    if packet.button == ButtonPacket.BUTTON_1:
                        print('1 button pressed')
                    elif packet.button == ButtonPacket.UP:
                        print('UP button pressed')
                    else:
                        print('WARNING: This button is not supported')

    # NOTE: If we got here, we lost the connection. Go up to the top and start
    #       advertising again and waiting for a connection.
