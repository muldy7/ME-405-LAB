  """! @file main.py
  Doxygen style docstring for the file 
  """
  import micropython
  import time
  
  micropython.alloc_emergency_exception_buf(100)
  QUEUE_SIZE = 2
  int_queue = cqueue.IntQueue(QUEUE_SIZE)
  
  x = 1
  count = 1

  def timer_int(tim_num):
      """!
      Doxygen style docstring for interrupt callback function
      """
      # Code goes here
      


  def step_response():
      """!
      Doxygen style docstring for this function 
      """
      # Function code here
      while x == 1

  if __name__ == "__main__":
      step_response()