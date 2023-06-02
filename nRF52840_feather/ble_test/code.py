# NOTE: Currently this will only work on Adrafruit's nRF feathers.
#       No ESP32 feathers support as of this moment (5.2023).

from adafruit_ble import BLERadio
from adafruit_ble.advertising.standard import ProvideServicesAdvertisement
from adafruit_ble.services.nordic import UARTService

ble = BLERadio()
uart = UARTService()
advertisement = ProvideServicesAdvertisement(uart)

ble.start_advertising(advertisement)
print('BLE advertising started')

while True:
    # Normally other work would be done here after connecting.
    pass
