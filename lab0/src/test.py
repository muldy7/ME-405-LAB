import micropython
import time

pinC0 = pyb.Pin (pyb.Pin.board.PC0, pyb.Pin.OUT_PP)
time.sleep(2)
pinC0.high()
time.sleep(5)
pinC0.low()

# pinC0.high()
# pinB0 = pyb.Pin(pyb.Pin.board.PB0, pyb.Pin.IN)
# if pinB0.value():
#     print("good")
#     print(pinB0.value())
#     
#     pinC0.low()