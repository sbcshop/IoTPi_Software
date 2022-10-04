#RS485_send.py
from machine import UART, Pin
import time

uart0 = UART(0, baudrate=115200, tx=Pin(0), rx=Pin(1))
b=0
txData = b'RS485 send test...\r\n'
uart0.write(txData)
print('RS485 send test')
time.sleep(0.1)
while True:
    b=b+1
    time.sleep(0.5) 
    print(b)
    uart0.write("{}\r\n".format(b))