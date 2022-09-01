# RGBMatrix
You will need
Adafruit RGB Matrix + Real Time Clock HAT for Raspberry Pi

Assemble as here
https://learn.adafruit.com/adafruit-rgb-matrix-plus-real-time-clock-hat-for-raspberry-pi/driving-matrices

Machine with SD card reader
  microSD needs an adapter

https://www.raspberrypi.com/software/
install for your machine

run the imager
choose latest rasperrry pi and storage is your sd card

Put the microSD card in the Raspberry Pi and boot up.

Fetch https://github.com/hzeller/rpi-rgb-led-matrix/tree/master/bindings/python
Fetch https://github.com/hzeller/rpi-rgb-led-matrix/blob/master/bindings/python/samples/image-draw.py
Fetch https://github.com/RoyWilliams/RGBMatrix

connections
Pi:
-- usb power
-- 5V power
-- hdmi screen
-- usb mouse
-- usb keyboard
-- usb thumb drive
-- 5V red/black to matrix
-- ribbon to matrix

Matrix
-- 5V red/black from pi
-- ribbon from pi

Check it works with image-draw.py

sudo python3 master.py
crontab with fetch_market.py

