## Lasair data monitoring RGB matrix
The simplest way to run the event display uses a compute monitor, and does not require installing hardware. Simply install the [OpenCV](https://pypi.org/project/opencv-python/) package, and in the `settings.py` file put `RGBmatrix = False`. Then `python3 master.py` on the command line and the display will come up.

The instructions below are about the wall-mounted display, with `RGBmatrix = True`.

This wall-mounted display shows the status of the Lasair data flow, and can be adapted for other purposes. Total cost is about $130. There is a 32x32 RGB matrix powered by a Raspberry Pi, and they can be mounted in a box-frame to make a wall-mounted display. There are two power cables, one a USB to power the RPi, the other a 5V supply for the matrix. The RPi needs to be on a wifi network, and the instructions below assume an external computer is on the same wifi. 

Each alert that arrives has RA and Dec in the sky: RA is 0-360 left to right, and Dec is -25-90 bottom to top. The corresponding LED lights up, and fades gradually over about 10 minutes. Further, there is [Conway's Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life) that is triggered, so that rapid movement continues on the matrix even after the alerts stop.

![ ](/image01.jpg)

### You will need
* [Raspberry Pi](https://www.adafruit.com/product/4295) $30
* [32x32 RGB LED Matrix Panel](https://www.adafruit.com/product/2026) $35
* [Adafruit Hat for matrix](https://www.adafruit.com/product/2345) $25
* [SD/MicroSD Memory Card with adapter](https://www.adafruit.com/product/1294) $10
* [5V power supply for the matrix](https://www.adafruit.com/product/276) $8
* [3D box frame](https://www.amazon.com/KAPIX-Picture-Plexiglass-Memorabilia-Keepsake/dp/B097Y4PGKW/ref=sr_1_12) $14 -- to show the matrix and keep the RPi in the back
* [Micro USB powercable](https://www.amazon.com/dp/B078QHT2KY/ref=sspa_dk_detail_0) $5
* A computer for connecting and controlling, with SD card slot.
* A wifi network that both the RPi and the external computer can use.
* External screen, USB mouse, USB keyboard.

## Assembly and Software
* Put your microSD into its adapter and connect to your external computer.
* Install a [Raspberry Pi imager](https://www.raspberrypi.com/software/) on your external computer.
* Run the imager, select latest RPi and install to the SD card.
* Follow the [Adafruit instructions](https://learn.adafruit.com/adafruit-rgb-matrix-plus-real-time-clock-hat-for-raspberry-pi/driving-matrices), steps 1-5.
* Connect a screen to the RPi with the Micro-HDMI, and connect the mouse and keyboard.
* Put the microSD card into the RPi and switch on power, give it username and password when prompted. YOu will need to connect it to your wifi network.
* Enable ssh for the RPi with `sudo raspi-config` then select Interface Options / SSH. Then use `hostname -I` to get the IP address so you can ssh to it.
 * Now you can put the RPi and matrix into the frame and hang it on the wall.  Plug in both the USB and 5V power.
 * Connect to your RPi with 
 * Continue the [Adafruit instructions](https://learn.adafruit.com/adafruit-rgb-matrix-plus-real-time-clock-hat-for-raspberry-pi/driving-matrices) with step 6. Make sure the examples work.

### Kafka and Lasair software

* Build librdkafka from source like this
```cd; cd matrix
git clone https://github.com/edenhill/librdkafka.git
cd librdkafka
./configure
make
sudo make install
```
* Install confluent kafka. I used a slightly downrev version for this:
```pip3 install --upgrade pip
pip3 install confluent_kafka==1.8.2
```
* Fetch the code that uses Lasair for the matrix
```
git clone https://github.com/RoyWilliams/RGBMatrix
```
* Now see if it works
```
sudo python3 master.py
```
* You can install `screen` so that it runs even when the SSH is disconnected
```
sudo apt-get install screen
```
