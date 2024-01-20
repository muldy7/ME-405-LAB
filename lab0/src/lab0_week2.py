# code for the week 2 lab 0 assignment
# test for the serial stuff

import serial
from serial import Serial
import time
from matplotlib import pyplot as plt


ser = serial.Serial("COM4", 9600)


try:
    cc=str(ser.readline()) # this has way to many values for things that arent numbers
    print(cc) # data is read as a string
    cc.split(",") # can split string into a list
    
    print(cc[1])
    
#     fig, ax = plt.subplots()
#     t = range(len(cc))
#     ax.plot(t, cc)  # create a plot of the filtered data
#     ax.set_title("Plot for HW0")    # create a title for the plot
#     plt.show() 

finally:
    pass


# for i in range(4):	# will have to test if there's data
#     try:
#         cc=str(ser.readline())
#         print(cc)
#         time.sleep(5)
#     finally:
#         pass

# print("writing to board")
# ser.write(bytearray('\x03','ascii')) # ascii code for ctrl+c
# ser.write(bytearray('\x02','ascii')) # ctrl+b
# ser.write(bytearray('\x04','ascii')) # ctrl+d
# # ser = serial.Serial("COM11", 9600)
# 
# while True:
#      cc=str(ser.readline())	# read data from the serial port
#      print(cc)