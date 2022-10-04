# Zero-Barcode-HAT

<img src= "https://github.com/sbcshop/Zero-Barcode-Hat/blob/main/images/img2.JPG" />
<img src= "https://github.com/sbcshop/Zero-Barcode-Hat/blob/main/images/img1.JPG" />

### Zero Barcode HAT for Raspberry Pi is a robust and compact barcode scanner board that consists of a DE2120 scanner module, buzzer, 1.14” LCD screen, micro-USB port. It is designed to scan 20 different barcode symbologies in the segment of both 1D and 2D symbology like barcodes and QR codes.

### Enable the SPI first in raspberry pi, for this go to cmd then type ```sudo raspi-config``` then go to ->interface option -> SPI - YES

## Setup Pi Zero Barcode HAT
First, you need to change the mode of the Zero Barcode HAT. Put Zero Barcode HAT at the top of the raspberry pi, then you need to scan the below barcode settings before running the code 

 * Mode is TTL/RS232 (serial communication interface(UART)) for this you need to scan below the barcode, Connect USB to Zero Barcode Hat.
  
<img src= "https://github.com/sbcshop/Pi-Barcode-HAT/blob/main/images/ttl_rs232.JPG" />
   
 * Change the baud rate to (9600) for this you need to scan the below barcode by pressing the scan button on the Zero Barcode Hat.

 <img src= "https://github.com/sbcshop/Pi-Barcode-HAT/blob/main/images/baudrate.JPG" />

## Use Zero Barcode Hat without Raspberry Pi( Via USB Cable )
For this you need to scan below barcode settings
 <img src= "https://github.com/sbcshop/Pi-Barcode-HAT/blob/main/images/img7.JPG" />
  
## Working
<img src= "https://github.com/sbcshop/Zero-Barcode-Hat/blob/main/images/img6.png" />

## Applications
First of all, move all the files from the applications folder to the outside folder which is the Zero Barcode HAT folder, so that main.py could access the files in the lib sub-directory
* Pins of the ultrasonic sensor (we use this sensor to avoid pressing the push button to scan the barcode ), we use 3v ultrasonic sensor
   * Trig is connected to GPIO 4
   * Echo is connected to GPIO 17
* Servo motor
   * Servo motor pin is connected to GPIO 2

## Working of Applications 
  * Smart shopping
  <img src= "https://github.com/sbcshop/Zero-Barcode-Hat/blob/main/images/img1.png" />
  
  * Smart Library Management System
  <img src= "https://github.com/sbcshop/Zero-Barcode-Hat/blob/main/images/img4.png" />
  
  * Smart Attendence System
  <img src= "https://github.com/sbcshop/Zero-Barcode-Hat/blob/main/images/img2.png" />

   


