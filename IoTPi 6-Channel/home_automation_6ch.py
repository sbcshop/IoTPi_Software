'''
This is the Example code of home automation for conntrolling 4-ch relays by using Android App
This code is Devolop by Sb-componetns 
'''

from IoTPi import Wifi
from IoTPi import Relay_6ch,Status_led
import time

WiFi_SSID='Tech SB_2G'             # Enter Wifi SSID here
WiFi_password = 'jc643111h@'       # Enter WiFi Password here
Port = '8080'

iot_pi = Wifi(WiFi_SSID,WiFi_password,Port)
iot_pi.Wifi_start()
Status_led1.status_led_on() # turn of status led write 'Status_led.status1_led_off()'

while True:
    Connection_ID,data=iot_pi.ReceiveData()
    if(Connection_ID != None):
        print(data)# Print Received data
        if data == "Relay1_ON":
            Relay_6ch.relay1_on()
            
        if data == "Relay1_OFF":
            Relay_6ch.relay1_off()
            
        if data == "Relay2_ON":
            Relay_6ch.relay2_on()
            
        if data == "Relay2_OFF":
            Relay_6ch.relay2_off()
                      
        if data == "Relay3_ON":
            Relay_6ch.relay3_on()
            
        if data == "Relay3_OFF":
            Relay_6ch.relay3_off()
                     
        if data == "Relay4_ON":
            Relay_6ch.relay4_on()
            
        if data == "Relay4_OFF":
            Relay_6ch.relay4_off()           
        if data == "Relay5_ON":
            Relay_6ch.relay5_on()
            
        if data == "Relay5_OFF":
            Relay_6ch.relay5_off()
                     
        if data == "Relay6_ON":
            Relay_6ch.relay6_on()
            
        if data == "Relay6_OFF":
            Relay_6ch.relay6_off()
