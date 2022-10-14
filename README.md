# IoTPi

<img src ="https://github.com/sbcshop/IoTPi/blob/main/images/IotPi%20Banner.png"  />

## IoTPi is an industrial board that consists of onboard RP2040, ESP8266 WIFI(ESP-12E) and RS-485 communication that can control up to 4/6 appliances/devices on a load    of, photo-coupling isolation Optocoupler EL357NC, allowing users to safely control high voltages or current devices. IoTPi makes appliances smart, which users can operate via the PiRelay app on their electronic device. IoTPi is also consist of addition GPIOs pins for connecting extra Hardware to this board.

## RS-485
### RS-485 is an industrial specification that defines the electrical interface and physical layer for point-to-point communication of electrical devices. The RS-485 standard allows for long cabling distances in electrically noisy environments and can support multiple devices on the same bus. It is a serial communication protocols and are ubiquitous device interfaces.
It is used to communicate with RS485 sender by connecting its A-terminal and B-terminal to A-terminal and B-terminal of the sender module respectively. Power port should be connected in the right direction (positive terminal to positive and negative terminal to negative of sender and receiver) in boards.

## Reserved Pins Of IoT-Pi 4/6CH Board

<img src ="https://github.com/sbcshop/IoTPi/blob/main/images/PinReserved-IoT4ch.png" />
<img src = "https://github.com/sbcshop/IoTPi/blob/main/images/PinReserved_IoT6ch.png" />

### Steps To Follow for Working with IoT-Pi Boards

* Step.1 - Download the Zip file of IoTPi package and extract it in your computer system, for this click on code—>download Zip (Highlighted with Red)

<img src ="https://github.com/sbcshop/IoTPi/blob/main/images/Iotpi_SC1.PNG" />

* Step.2 - After downloading and extracting the Zip file you will get the following files under the “IoTPi-main” folder

<img src ="https://github.com/sbcshop/IoTPi/blob/main/images/Screenshot%20(22).png" />

* Step.3 - After that open the folder IoTPi 4-channel if you have our 4-channel board or if you have 6-channel board then open IoTPi 6-channel folder. Under this you get   two python files as shown in below image
<img src ="https://github.com/sbcshop/IoTPi/blob/main/images/SC3.PNG" />

* Step.4 - File “home_automation_4ch” is the main file and “IoTPi” is the library file for our IoTPi boards. To open these files you should have Thonny IDE installed in your system, If you don’t have Thonny IDE follow the link below to install it. Click here

* Step.5 - First Open both files in your IDE and connect your IoTPi board to your computer via using micro-usb cable.
<img src ="https://github.com/sbcshop/IoTPi/blob/main/images/Screenshot%20(7).png" />

* Step.6 - Now select the interpreter by clicking on “Run” button in IDE and follow the image instructions below 
<img src ="https://github.com/sbcshop/IoTPi/blob/main/images/Screenshot%20(16).png" />
<img src ="https://github.com/sbcshop/IoTPi/blob/main/images/Screenshot%20(14).png" />
<img src ="https://github.com/sbcshop/IoTPi/blob/main/images/Screenshot%20(15).png" />
* Step.7 - After selecting the interpreter click on the “Stop” button for restarting your board. If your board is properly connected you will get the RP2040 information as , shown below 
<img src ="https://github.com/sbcshop/IoTPi/blob/main/images/Screenshot%20(18).png" />

* Step.8. Now click on “IoTPi” file and save it in your RP2040, for this click on “file” (upper left corner in your IDE) under that click on “save as” you will get a window asking for where you want to save your copy file, click on “Raspberry Pi PICO” and save it by naming it “IoTPi” and click on “Ok”. Your file will be saved in RP2040 of your IoTPi Board
<img src ="https://github.com/sbcshop/IoTPi/blob/main/images/Screenshot%20(1).png" />
<img src ="https://github.com/sbcshop/IoTPi/blob/main/images/Screenshot%20(2).png" />
<img src ="https://github.com/sbcshop/IoTPi/blob/main/images/Screenshot%20(3).png" />

*Step.9 - After that you have to save the code file (home_automation_4ch) in RP2040 same as the library file(step.5), only change is you have to save it by naming it “main.py” and then click on “Ok”. You can also see that your library file already saved here that you recently saved in it. 

<img src ="https://github.com/sbcshop/IoTPi/blob/main/images/Screenshot%20(8).png" />

Step.10 - Now, both the library and main file are saved in your board and it is ready to control relays of it and so on appliances that you want by providing the command accordingly
<img src ="https://github.com/sbcshop/IoTPi/blob/main/images/Screenshot%20(11).png" />

### Downloading Android Application
As in previous steps we completed the code saving and other important steps to work with the IoTPi board. Now in this section we will learn how to control it.

* Step.1 - In the IoTPi_main folder you will also get a folder named with “Android Application”
<img src ="https://github.com/sbcshop/IoTPi/blob/main/images/Screenshot%20(20).png" />

* Step.2 - Open this folder and under this you will get a .apk file named with  “IoTPi.apk” download and install this application in your android phone for controlling your IoTPi Board
<img src ="https://github.com/sbcshop/IoTPi/blob/main/images/Screenshot%20(21).png" />

* Step.3 - After installing the app, open it and you will get the interfaces as following below

<img src ="https://github.com/sbcshop/IoTPi/blob/main/images/IMG-20221013-WA0003.jpg" />

<img src ="https://github.com/sbcshop/IoTPi/blob/main/images/IMG-20221013-WA0005.jpg" />

* Step.4 - For connecting this application to your board provide IP address of your WiFi which your using at that time, in my case my it was 192.168.43.18 as shown below
<img src ="https://github.com/sbcshop/IoTPi/blob/main/images/Screenshot%20(28).png" />

* Step.5 - Initially the button setting should be as shown in below image for giving ON/OFF commands. After that you can change it according to your code
<img src ="https://github.com/sbcshop/IoTPi/blob/main/images/Screenshot_20221014.jpg" />

### Communication Using RS485
The IoTPi  board also has the feature of rs485. You can use this feature by making one of your boards as the sender and another one as receiver. Fer this follow the steps below

* Step.1 - Locate  the RS485 directory inside the IoTPi_main folder and open it, inside this folder you will get a file named with “rs485_test” 
<img src ="https://github.com/sbcshop/IoTPi/blob/main/images/Screenshot%20(23).png" />
* Step. 2 - Open the “RS485_test” file and you will get two blocks of codes, one is for making a receiver and the other one is for making your board as a sender.

* Step. 3 - Uncomment the sender code and save it in RP2040 of your board and now it is ready for working as a rs485 sender device.
<img src ="https://github.com/sbcshop/IoTPi/blob/main/images/Screenshot%20(26).png" />
* Step.4 - Now, uncomment the receiver block of code(sender block should be commented this time) and save it  in another board
<img src ="https://github.com/sbcshop/IoTPi/blob/main/images/Screenshot%20(27).png" />

* Step.5 - Now, your sender and receiver board is ready for communicating to each other by using rs485 protocol.

* Step.6 - Connect to RS485 port of  your boards as shown below and Power port should be connected in the right direction to a 5V dc  power supply

<img src ="https://github.com/sbcshop/IoTPi/blob/main/images/IMG_5938%20-%20Edited%20(1).png" />
