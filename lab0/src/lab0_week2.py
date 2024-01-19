# code for the week 2 lab 0 assignment
# test for the serial stuff

import serial
from serial import Serial
import time


ser = serial.Serial("COM4", 9600)

for i in range(4):	# will have to test if there's data
    try:
        cc=str(ser.readline())
        print(cc)
    finally:
        pass

print("writing to board")
ser.write(bytearray('\x03','ascii')) # ascii code for ctrl+c
ser.write(bytearray('\x02','ascii')) # ctrl+b
ser.write(bytearray('\x04','ascii')) # ctrl+d
# ser = serial.Serial("COM11", 9600)
while True:
     cc=str(ser.readline())	# read data from the serial port
     print(cc)