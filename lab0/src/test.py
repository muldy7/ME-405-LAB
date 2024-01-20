# import micropython
import micropython
import time
import math
#import matplotlib
#from matplotlib import pyplot as plt

t = []
for i in range(100):
    t.append(i*10)

v_max = 3.03
r = 100
c = 3.3
data = []

for i in t:
    value = (3.03*(1-math.exp(-i/(r*c))))
    data.append(value)
    
while True:
    print(data)
    time.sleep(5)


# fig, ax = plt.subplots() 
# ax.plot(t, data)  # create a plot of the filtered data
# ax.set_title("Plot for HW0")    # create a title for the plot
# plt.show() 