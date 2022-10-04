import time,utime
from machine import I2C, Pin, SPI
from sgp40 import SGP40
import bme280
import tcs34725
import sht31
import st7789
import vga1_bold_16x32 as font
import vga1_8x16 as font1

i2c = I2C(1,scl=Pin(7), sda=Pin(6), freq=40000)#all sensor connected through I2C

rst = machine.Pin(3, machine.Pin.OUT)#GPIO 3(OUTPUT) pin to enable address of temperature and humidity sht21 sensor
rst.value(1)#high GPIO 3 pin to enable address of temperature and humidity sht21 sensor

spi = SPI(1, baudrate=40000000, sck=Pin(10), mosi=Pin(11))
tft = st7789.ST7789(spi,135,240,reset=Pin(12, Pin.OUT),cs=Pin(9, Pin.OUT),dc=Pin(8, Pin.OUT),rotation=1)#SPI interface for tft screen

bme = bme280.BME280(i2c=i2c) #pressure,temperature and humidity sensor
color = tcs34725.TCS34725(i2c)#color sensor
air_quality = SGP40(i2c, 0x59)#air quality sensor
temp_hum = sht31.SHT31(i2c, addr=0x45)#temperature and humidity

relay = machine.Pin(26, machine.Pin.OUT)#relay connected to RP2040 pin 26
relay.value(0)



def info():
    tft.init()
    utime.sleep(0.2)
    tft.text(font,"SB COMPONENTS", 15,20)
    tft.fill_rect(15, 60, 210,10, st7789.RED)
    
    tft.text(font,"IoTPi 4/6 CH", 15,80,st7789.YELLOW)
    tft.fill_rect(15, 140, 210, 10, st7789.BLUE)
    time.sleep(2)
    tft.fill(0) #clear screen
    
info()

def info1():
    tft.init()
    tft.fill(st7789.BLACK)
    time.sleep(0.5)#time delay
    tft.text(font1,"SB-COMPONENTS PICO SENSE HAT",5,5,st7789.RED)
    tft.text(font1,"SENSOR READING",70,25,st7789.RED)
    tft.text(font1,"PRESSURE    : ",10,50,st7789.YELLOW)
    tft.text(font1,"TEMPERATURE :",10,65,st7789.YELLOW)
    tft.text(font1,"HUMIDITY    :  ",10,80,st7789.YELLOW)
    tft.text(font1,"AIR QUALITY :",10,95,st7789.YELLOW)
    tft.text(font1,"COLOR       :",10,110,st7789.YELLOW)
    
info1()   
while True:
    #temp,hum,press = bme.temperature,bme.humidity,bme.pressure #uncomment this line for use of temperature and humidity
    pressure = bme.pressure # we use only pressure from BME sensor, you can also read temperature and humidity as ewll
    Temp_Humid = temp_hum.get_temp_humi()
    Temp_Humid = list(Temp_Humid)
    Air_quality = air_quality.measure_raw()
    Color = color.read('rgb')
    
    temperature = "{0}{1:.2f}C".format("", Temp_Humid[0])
    humidity = "{0}{1:.2f}%".format("", Temp_Humid[1])
    
    print("Prssure  ",pressure)
    print("Temperature = ",temperature)    
    print("humidity = ",humidity)
    print("Air quality = ",Air_quality)
    print("Color = ",Color)#R,G,B,C
    
    
    if Temp_Humid[0] > 32:
        relay.value(1)
    else:
        relay.value(0)
        
    '''
    # **** uncomment this if you need temperature in fahrenheit ********
    
    fahrenheit = float(Temp_Humid[0]) * 1.8 + 32
    fahrenheit = "{:.2f}".format(fahrenheit)
    print("Temperature in fahrenheit  = ",fahrenheit)
    '''

    '''
    # **** uncomment this if you need pressure in psi, mmhg and atm ********

    press = pressure.split('h')
    kpa = float(press[0]) * 10
    psi = kpa / 6.89475729
    mmhg = kpa * 760 / 101.325
    atm = kpa / 101.325
    print("Pounds per square inch: %.2f psi"  % (psi))
    print("Millimeter of mercury: %.2f mmHg" % (mmhg))
    print("Atmosphere pressure: %.2f atm." % (atm))
    '''
    
    tft.text(font1,pressure, 120,50,st7789.WHITE)# print on tft screen
    tft.text(font1,str(temperature), 120,65,st7789.WHITE)# print on tft screen
    tft.text(font1,str(humidity), 120,80,st7789.WHITE)# print on tft screen
    tft.text(font1,str(Air_quality), 120,95,st7789.WHITE)# print on tft screen
    tft.text(font1,str(Color), 120,110,st7789.WHITE)# print on tft screen
    
    time.sleep(0.1)
    
    tft.text(font1,pressure, 120,50,st7789.WHITE)# print on tft screen
    tft.text(font1,str(temperature), 120,65,st7789.WHITE)# print on tft screen
    tft.text(font1,str(humidity), 120,80,st7789.WHITE)# print on tft screen
    tft.text(font1,str(Air_quality), 120,95,st7789.WHITE)# print on tft screen
    tft.text(font1,str(Color), 120,110,st7789.WHITE)# print on tft screen
    


