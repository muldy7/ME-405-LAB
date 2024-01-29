This folder contains lab code for ME-405

This program uses a simple GUI to control the Nucleo board and generate a step response in the circuit below.
An input voltage is applied and the repsonse due to the capacitor is measured and logged on the board. 
Once the step response test has concluded, the data is read through a serial connection to the user laptop and graphed against a theoretical response. 

![Alt text](circuit_diagram.png)


Figure 1. Circuit diagram for step response test. 


![Alt text](plot_response_image-1.png)


Figure 2. Example step response result plotted against the theoretical curve. 

the source files are lab_00b.py and lab0week2_final.py. 

lab_00b.py ontains code which computes the answer to lab0 week 1.

This code sets up a timer interrupt to generate a step reponse from the physical circuit we created. This same code is used in the main.py file stored on the microcontroller for our lab0 week2 code.

lab0week2_final.py contains code to run program on a laptop or desktop which creates a user interface that can send a signal to the microcontroller to run a step response.

The code then takes the results of the step response from the microcontroller and plots it in the user interface. Included in the GUI plot as well is a plot of a simulated V_max(1-e^-t/RC) curve. The V_max, R, and C values are from are circuit and are 3.03 V, 100K Ohms, and 3.3 microF respectively.

