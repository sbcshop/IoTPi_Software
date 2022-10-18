'''
This is the liberary code for IoTPi boards
Devolop by Sb-components
'''

from machine import UART,Pin,I2C,SPI
import utime,time
import machine
uart = UART(1, 115200) # esp8266
rs_485 = UART(0, baudrate=115200, tx=Pin(0), rx=Pin(1)) # RS485 Communication

class Wifi(object):
    lst = []
    def __init__(self,wifi_ssid,wifi_pass,wifi_port,uart=uart):
        self.wifi_ssid = wifi_ssid
        self.wifi_pass = wifi_pass
        self.wifi_port = wifi_port

    def sendCMD(self,cmd,ack,timeout=2000):
        uart.write(cmd+'\r\n')
        t = utime.ticks_ms()
        while (utime.ticks_ms() - t) < timeout:
            s=uart.read()
            if(s != None):
                s=s.decode()
                print(s)
                if cmd =="AT+CIFSR":
                    self.lst.append(s)            
                if(s.find(ack) >= 0):
                    return True
        return False

    def sendData(ID,data):
        self.sendCMD('AT+CIPSEND='+str(ID)+','+str(len(data)),'>')
        uart.write(data)

    def ReceiveData(self):
        data=uart.read()
        if(data != None):
            data=data.decode()
            print(data)
            if(data.find('+IPD') >= 0):
                n1=data.find('+IPD,')
                n2=data.find(',',n1+5)
                ID=int(data[n1+5:n2])
                n3=data.find(':')
                data=data[n3+1:]
                return ID,data
        return None,None
        
    def Wifi_start(self):
        uart.write('+++')
        time.sleep(1)
        if(uart.any()>0):uart.read()
        self.sendCMD("AT","OK")
        self.sendCMD("AT+CWMODE=3","OK")
        self.sendCMD("AT+CWJAP=\""+self.wifi_ssid+"\",\""+self.wifi_pass+"\"","OK",20000)
        self.sendCMD("AT+CIPMUX=1","OK")
        self.sendCMD("AT+CIPSERVER=1,"+self.wifi_port,"OK")
        self.sendCMD("AT+CIFSR","OK")

class Status_led():
    def status_led_on():
        status_led = machine.Pin(24, machine.Pin.OUT)#led_1 connected to pico pin 24
        status_led.value(1)
        
    def status_led_off():
        status_led = machine.Pin(24, machine.Pin.OUT)#led_1 connected to pico pin 24
        status_led.value(0)
      
    def status1_led_on():
        status_led = machine.Pin(22, machine.Pin.OUT)#led_1 connected to pico pin 24
        status_led.value(1)
        
    def status1_led_off():
        status_led = machine.Pin(22, machine.Pin.OUT)#led_1 connected to pico pin 24
        status_led.value(0)
        
class Relay_4ch(object):
        def relay1_on():
            relay1 = machine.Pin(22, machine.Pin.OUT)#relay1 connected to pico pin 22
            relay1.value(1)
            
        def relay2_on():
            relay2 = machine.Pin(26, machine.Pin.OUT)#relay2 connected to pico pin 26
            relay2.value(1)
            
        def relay3_on():
            relay3 = machine.Pin(27, machine.Pin.OUT)#relay3 connected to pico pin 27
            relay3.value(1)
            
        def relay4_on():
            relay4 = machine.Pin(28, machine.Pin.OUT)#relay4 connected to pico pin 28
            relay4.value(1)
           
        def relay1_off():
            relay1 = machine.Pin(22, machine.Pin.OUT)#relay1 connected to pico pin 22
            relay1.value(0)

        def relay2_off():
            relay2 = machine.Pin(26, machine.Pin.OUT)#relay2 connected to pico pin 26
            relay2.value(0)
            
        def relay3_off():
            relay3 = machine.Pin(27, machine.Pin.OUT)#relay3 connected to pico pin 27
            relay3.value(0)
            
        def relay4_off():
            relay4 = machine.Pin(28, machine.Pin.OUT)#relay4 connected to pico pin 28
            relay4.value(0)
            

class Relay_6ch():
        def relay1_on():
            relay1 = machine.Pin(24, machine.Pin.OUT)#relay1 connected to pico pin 24
            relay1.value(1)
            
        def relay2_on():
            relay2 = machine.Pin(25, machine.Pin.OUT)#relay2 connected to pico pin 25
            relay2.value(1)
            
        def relay3_on():
            relay3 = machine.Pin(26, machine.Pin.OUT)#relay3 connected to pico pin 26
            relay3.value(1)
            
        def relay4_on():
            relay4 = machine.Pin(27, machine.Pin.OUT)#relay4 connected to pico pin 27
            relay4.value(1)
            
        def relay5_on():
            relay5 = machine.Pin(28, machine.Pin.OUT)#relay5 connected to pico pin 28
            relay5.value(1)

        def relay6_on():
            relay6 = machine.Pin(29, machine.Pin.OUT)#relay6 connected to pico pin 29
            relay6.value(1)
            
        def relay1_off():
            relay1 = machine.Pin(24, machine.Pin.OUT)#relay1 connected to pico pin 24
            relay1.value(0)

        def relay2_off():
            relay2 = machine.Pin(25, machine.Pin.OUT)#relay2 connected to pico pin 25
            relay2.value(0)
            
        def relay3_off():
            relay3 = machine.Pin(26, machine.Pin.OUT)#relay3 connected to pico pin 26
            relay3.value(0)
            
        def relay4_off():
            relay4 = machine.Pin(27, machine.Pin.OUT)#relay4 connected to pico pin 27
            relay4.value(0)

        def relay5_off():
            relay5 = machine.Pin(28, machine.Pin.OUT)#relay5 connected to pico pin 28
            relay5.value(0)
            
        def relay6_off():
            relay6 = machine.Pin(29, machine.Pin.OUT)#relay6 connected to pico pin 29
            relay6.value(0)
 
class RS485():
    def RS485_Send(self,TX_Data):
        tx_data = TX_Data
        #tx_data = bytes(TX_Data)
        #tx_data = b'RS485 send test...\r\n'
        rs_485.write(tx_data)
        print('RS485 send test')

    def RS485_Receive(self):
        while 1:
            receive_data = bytes()
            while rs_485.any() > 0:
                receive_data = rs_485.read()
                return receive_data
                
