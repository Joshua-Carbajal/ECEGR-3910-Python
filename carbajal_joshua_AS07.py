# File Name: carbajal_joshua_AS07.py
# File Path: /home/carbaja1/Python/Python/carbajal_joshua_AS07.py
# Run Command: sudo python3 /home/carbaja1/Python/carbajal_joshua_AS07.py

# Joshua Carbajal
# Date (10/18/19)
# AS.07
# Purpose: Analog input to digital readout from a Joystick

import time # Time library
import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn

# create the spi bus
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)

# create the cs (chip select)
cs = digitalio.DigitalInOut(board.D5)

# create the mcp object
mcp = MCP.MCP3008(spi, cs)

# create an analog input channel on pin 0 & 1
chan_0 = AnalogIn(mcp, MCP.P0)
chan_1 = AnalogIn(mcp, MCP.P1)

while True:
    print('Raw ADC Value: ', chan_0.value >> 6)
    print('ADC Voltage: ' + str(chan_0.voltage) + 'V')
    print('Raw ADC Value: ', chan_1.value >> 6)
    print('ADC Voltage: ' + str(chan_1.voltage) + 'V')
    time.sleep(0.5)

