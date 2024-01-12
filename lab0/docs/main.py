# from matplotlib import pyplot
import time

adc0 = pyb.ADC(pyb.Pin.board.PC0)
y = []
for x in range(100):
    time.sleep(0.1)
    y.append(adc0.read())
    print(y[x])
    
print(y)
    
