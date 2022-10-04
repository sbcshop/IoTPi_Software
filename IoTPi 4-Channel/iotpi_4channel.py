#IoTPi 4 Channel
from machine import UART,Pin,I2C
import utime,time

uart = UART(1, 115200)             # Default Baud rate of ESP8266

WiFi_SSID='WIFI NAME'             # Enter Wifi SSID here
WiFi_password = 'PASSWORD'       # Enter WiFi Password here
Port = '8080'                      # TCP Server Port

status_led = machine.Pin(24, machine.Pin.OUT)#led_1 connected to pico pin 24
status_led.value(0)

relay1 = machine.Pin(22, machine.Pin.OUT)#relay1 connected to pico pin 22
relay2 = machine.Pin(26, machine.Pin.OUT)#relay2 connected to pico pin 26
relay3 = machine.Pin(27, machine.Pin.OUT)#relay3 connected to pico pin 27
relay4 = machine.Pin(28, machine.Pin.OUT)#relay4 connected to pico pin 28

relay1.value(0)
relay2.value(0)
relay3.value(0)
relay4.value(0)


lst = []
def sendCMD(cmd,ack,timeout=2000):
    uart.write(cmd+'\r\n')
    t = utime.ticks_ms()
    while (utime.ticks_ms() - t) < timeout:
        s=uart.read()
        if(s != None):
            s=s.decode()
            print(s)
            if cmd =="AT+CIFSR":
                lst.append(s)            
            if(s.find(ack) >= 0):
                return True
    return False

########  Function to send data  ###############

def sendData(ID,data):
    sendCMD('AT+CIPSEND='+str(ID)+','+str(len(data)),'>')
    uart.write(data)

########  Function to receive data  ###############

def ReceiveData():
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
      
uart.write('+++')
time.sleep(1)
if(uart.any()>0):uart.read()
sendCMD("AT","OK")
sendCMD("AT+CWMODE=3","OK")
sendCMD("AT+CWJAP=\""+WiFi_SSID+"\",\""+WiFi_password+"\"","OK",20000)
sendCMD("AT+CIPMUX=1","OK")
sendCMD("AT+CIPSERVER=1,"+Port,"OK")
sendCMD("AT+CIFSR","OK")

x = lst[0]
y = x.split(",")
y = y[3].split("+")
y = y[0].replace('"',"")
y = y.split(".")
y = list(map(str.strip,y))
s = int(y[0])+int(y[1])+int(y[2])

if s > 0:
    status_led.value(1)
else:
    status_led.value(0)

while True:
    Connection_ID,data=ReceiveData()
    if(Connection_ID != None):
        print(data)# Print Received data
        if data == "Relay1_ON":
            relay1.value(1)
            
        if data == "Relay1_OFF":
            relay1.value(0)
            
        if data == "Relay2_ON":
            relay2.value(1)
            
        if data == "Relay2_OFF":
            relay2.value(0)
                      
        if data == "Relay3_ON":
            relay3.value(1)
            
        if data == "Relay3_OFF":
            relay3.value(0)
                     
        if data == "Relay4_ON":
            relay4.value(1)
            
        if data == "Relay4_OFF":
            relay4.value(0)           
        
        if data == "relay one on":
            relay1.value(1)
            
        if data == "relay one off " or data == "relay one off" :
            relay1.value(0)
            
