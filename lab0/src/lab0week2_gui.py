"""!
@file lab0example.py
Run real or simulated dynamic response tests and plot the results. This program
demonstrates a way to make a simple GUI with a plot in it. It uses Tkinter, an
old-fashioned and ugly but useful GUI library which is included in Python by
default.

This file is based loosely on an example found at
https://matplotlib.org/stable/gallery/user_interfaces/embedding_in_tk_sgskip.html

@author Spluttflob
@date   2023-12-24 Original program, based on example from above listed source
@copyright (c) 2023 by Spluttflob and released under the GNU Public Licenes V3
"""

# imports from example
import math
import time
import tkinter
import serial
from random import random
from serial import Serial
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
                                               NavigationToolbar2Tk)

# import we need to add
# import serial
# from serial import Serial
# import time
# import math
from matplotlib import pyplot


def step_reponse(plot_axes, plot_canvas, xlabel, ylabel):
    # doxygen values need to be updated
    """!
    Make an example plot to show a simple(ish) way to embed a plot into a GUI.
    The data is just a nonsense simulation of a diving board from which a
    typically energetic otter has just jumped.
    @param plot_axes The plot axes supplied by Matplotlib
    @param plot_canvas The plot canvas, also supplied by Matplotlib
    @param xlabel The label for the plot's horizontal axis
    @param ylabel The label for the plot's vertical axis
    """
    # set the serial port for reading
    ser = serial.Serial("COM4", 9600)
    
    # reset and send stuff to the board
    print("sending to board")
    ser.write(bytearray('\x03','ascii')) # ascii code for ctrl+c
    ser.write(bytearray('\x02','ascii')) # ctrl+b
    ser.write(bytearray('\x04','ascii')) # ctrl+d
    
    # create our values for printing
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

    # our code
    # think it needs to work a little differently
#     pyplot.plot(t, volts, label = 'Measured Response Data', color = 'deepskyblue', marker = '.' )
#     pyplot.plot(t, data, label = 'Simulated Data', color = 'black', linestyle = '-')
#     pyplot.xlabel('Time [ms]')
#     pyplot.ylabel('Volts [v]')
#     pyplot.title('Simulated and Measured Step Response')
#     pyplot.legend()
#     pyplot.axis([0, 2000, 0, 3.5])
#     pyplot.show()
    
    # code from the example
    # plot_axes works differently with the gui instead of making a new figure
    # Draw the plot. Of course, the axes must be labeled. A grid is optional
    plot_axes.clear()	# clear the axes so there is no repeat legend
    plot_axes.plot(t, volts, label = 'Measured Response Data', color = 'deepskyblue', marker = '.' )
    plot_axes.plot(t, data, label = 'Simulated Data', color = 'black', linestyle = '-')
    plot_axes.set_xlabel(xlabel)
    plot_axes.set_ylabel(ylabel)
    plot_axes.grid(True)
    plot_axes.legend()
    plot_axes.axis([0, 2000, 0, 3.5])
    plot_canvas.draw()


def tk_matplot(plot_function, xlabel, ylabel, title):
    """!
    Create a TK window with one embedded Matplotlib plot.
    This function makes the window, displays it, and runs the user interface
    until the user closes the window. The plot function, which must have been
    supplied by the user, should draw the plot on the supplied plot axes and
    call the draw() function belonging to the plot canvas to show the plot. 
    @param plot_function The function which, when run, creates a plot
    @param xlabel The label for the plot's horizontal axis
    @param ylabel The label for the plot's vertical axis
    @param title A title for the plot; it shows up in window title bar
    """
    # Create the main program window and give it a title
    tk_root = tkinter.Tk()
    tk_root.wm_title(title)

    # Create a Matplotlib 
    fig = Figure()
    axes = fig.add_subplot()

    # Create the drawing canvas and a handy plot navigation toolbar
    canvas = FigureCanvasTkAgg(fig, master=tk_root)
    toolbar = NavigationToolbar2Tk(canvas, tk_root, pack_toolbar=False)
    toolbar.update()

    # Create the buttons that run tests, clear the screen, and exit the program
    button_quit = tkinter.Button(master=tk_root,
                                 text="Quit",
                                 command=tk_root.destroy)
    button_clear = tkinter.Button(master=tk_root,
                                  text="Clear",
                                  command=lambda: axes.clear() or canvas.draw())
    button_run = tkinter.Button(master=tk_root,
                                text="Run Test",
                                command=lambda: plot_function(axes, canvas,
                                                              xlabel, ylabel))

    # Arrange things in a grid because "pack" is weird
    canvas.get_tk_widget().grid(row=0, column=0, columnspan=3)
    toolbar.grid(row=1, column=0, columnspan=3)
    button_run.grid(row=2, column=0)
    button_clear.grid(row=2, column=1)
    button_quit.grid(row=2, column=2)

    # This function runs the program until the user decides to quit
    tkinter.mainloop()


# This main code is run if this file is the main program but won't run if this
# file is imported as a module by some other main program
if __name__ == "__main__":
    tk_matplot(step_reponse,
               xlabel='Time [ms]',
               ylabel='Volts [v]',
               title='Simulated and Measured Step Response')
        
    # our labels
      #pyplot.xlabel('Time [ms]')
#     pyplot.ylabel('Volts [v]')
#     pyplot.title('Simulated and Measured Step Response')

