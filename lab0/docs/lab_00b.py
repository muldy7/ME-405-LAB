import micropython
import time
import cqueue

 

def main():
    output_array=[]  # array where the outputted values will go before printing
    step = 0.001   
    time=my_list = [float(i) * step for i in range(int(0.001 / step), int(2.001 / step))]  #list of times to print alongside output_array
  
    pinC0 = pyb.Pin(pyb.Pin.board.PC0, pyb.Pin.OUT_PP)  #initializes the pin as an outport pin
    #need to intialize the output pin i think in the same way
    
    pinB0 = pyb.Pin (pyb.Pin.board.PB0, pyb.Pin.IN)
    
    time_int = pyb.Timer (1,freq = 1000)      # timer 1 running at 1000 Hz
    time_int.counter()                         # gets the timer value
    micropython.alloc_emergency_exception_buf(100) # alocates buffer for emergency exception handling, used when memory is a constraint
    
    QUEUE_SIZE = 2000                               # this is the size of the que to collect 2 seconds of data at 1 ms interupts
    int_queue = cqueue.IntQueue(QUEUE_SIZE)
    step_response()
    
    
    


def timer_int(tim_num):
    """!
    Doxygen style docstring for interrupt callback function
    """
  
    #COLLECT ADC
    int_queue.put(pinB0.value())  #read and put into queue. inside the put() is the value that will be read from the pin. this has not been set up in the code yet
    int_queue.full()
    if value.int_queue.full() == True:
            timer_int.callback(None)          #If que is full, disable Callback 
    else:
        pass
   
    pass 
      


def step_response():# run this function when requeste dby user or through GUI
    """!
    Doxygen style docstring for this function 
    """
    # Function code here
    timer_int.callback(time_int)  #configure and enable the calllback. example : timmy.callback(timer_cb)
    pinC0.high()                   #set the trigger pin to high pin.high   (pinC0.value(1)
    while not int_que.full():                             #wait for a full queue ( while not my_que.full()
            pass						#     pass
            pinC0.high ()                 #	Set pin back to low
                                    
    while not int_que.empty():          #iterate through the queue to and add to the array output_array
        output=int_que.get()
        output_array.append(output)
    print('done')


if __name__ == "__main__":
    main()