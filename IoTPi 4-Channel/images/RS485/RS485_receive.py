#RS485_receive.py
from machine import UART, Pin
import time

uart0 = UART(0, baudrate=115200, tx=Pin(0), rx=Pin(1))

txData = 'RS485 receive test...\r\n'
uart0.write(txData)
print(uart0 )
print('RS485 receive test')
time.sleep(0.2)

while True:
    recvData = bytes()
    while uart0.any() > 0:
        recvData = uart0.read()
        print(recvData)
