import micropython
import time
import cqueue



interrupt = pyb.Timer (1,freq = 1000)
pinC0 = pyb.Pin (pyb.Pin.board.PC0, pyb.Pin.OUT_PP, value = 0)  #initializes the pin as an outport pin
pinB0 = pyb.Pin (pyb.Pin.board.PB0, pyb.Pin.IN, value = 0) #need to intialize the output pin i think in the same way
adcpin = pyb.ADC(pinB0)

QUEUE_SIZE = 1000
int_queue = cqueue.IntQueue(QUEUE_SIZE)
output_array=[]  # array where the outputted values will go before printing
step = 0.001   
time = list(range(QUEUE_SIZE)) #list of times to print alongside output_array


def main():
    micropython.alloc_emergency_exception_buf(100) # alocates buffer for emergency exception handling, used when memory is a constraint
    
    interrupt.counter()                         # gets the timer value
    step_response()
    

def timer_int(tim_num):
    """!
    Doxygen style docstring for interrupt callback function
    """
  
    #COLLECT ADC
    int_queue.put(adcpin.read())  #read and put into queue. inside the put() is the value that will be read from the pin. this has not been set up in the code yet
    int_queue.full()
    if int_queue.full() == True:
            interrupt.callback(None)          #If queue is full, disable Callback 
    else:
        pass
    pass 
      


def step_response():# run this function when requeste dby user or through GUI
    """!
    Doxygen style docstring for this function 
    """
    # Function code here
    
    interrupt.callback (timer_int)  			#configure and enable the calllback. example : timmy.callback(timer_cb)
    pinC0.high()                   			#set the trigger pin to high pin.high   (pinC0.value(1)
    while not int_queue.full():                             #wait for a full queue ( while not my_que.full()
            pass						#     pass
                                                                          # Set pin back to low
    pinC0.low ()
    
    while int_queue.any():          			#iterate through the queue to and add to the array output_array
        output=int_queue.get()
        output_array.append(output)
    output_array_f = [(3.3/4096)*x for x in output_array]
    pairs = list(zip(time, output_array_f))
    for line in pairs:
        print(line)
    

if __name__ == "__main__":
    main()