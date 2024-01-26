# code for the week 2 lab 0 assignment
# test for the serial stuff

import serial
from serial import Serial
import time
import math
from matplotlib import pyplot 

ser = serial.Serial("COM5", 9600)

print("sending to board")
ser.write(bytearray('\x03','ascii')) # ascii code for ctrl+c
ser.write(bytearray('\x02','ascii')) # ctrl+b
ser.write(bytearray('\x04','ascii')) # ctrl+d



array =[]
cont = 1
time=[]
volts=[]
while cont == 1:
#      line=ser.readline().decode('utf-8').strip()	# read data from the serial port
#      print(line)
    value = ser.readline().decode('utf-8').strip()
    if value == 'end':
        cont = 0
    else:
        array.append(value)
for i in array:
    index = i.split(',')
    try:  
        timeval  =float(index[0].strip('('))
        voltval = float(index[1].strip(')'))
        time.append(timeval)
        volts.append(voltval)
    except:
        pass
#print(volts)
       




#Simulated response Plot - This works
t = []
for i in range(len(time)):
    t.append(2*i)

v_max = 3.03
r = 100
c = 3.3
data = []

for i in t:
    value = (3.03*(1-math.exp(-i/(r*c))))
    data.append(value)
    
print(data)


pyplot.plot(t, volts, label = 'Measured Response Data', color = 'deepskyblue', marker = '.' )
pyplot.plot(t, data, label = 'Simulated Data', color = 'black', linestyle = '-')
pyplot.xlabel('Time [ms]')
pyplot.ylabel('Volts [v]')
pyplot.title('Simulated and Measured Step Response')
pyplot.legend()
pyplot.axis([0, 2000, 0, 3.5])
pyplot.show()

















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