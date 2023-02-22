# HBO-ICT-proefstuderen: Traffic Light Example with the Raspberry Pi Pico
# Based on https://www.waveshare.com/wiki/Template:Raspberry_Pi_Pico_Example#Traffic_Light_System_Testing
# Changes 2023 by noharm, hagen-git

from machine import Pin
from time import sleep_ms

# Hardware definitions (which pin has which function)
button = Pin(16, Pin.IN, Pin.PULL_DOWN)
led_red = Pin(15, Pin.OUT)
led_orange = Pin(14, Pin.OUT)
led_green = Pin(13, Pin.OUT)
buzzer = Pin(12, Pin.OUT)


# Function definitions ------------------------------------

def beep_n_times(number):
    """ Beep ten times, on/off time is 200 milliseconds. """
    for i in range(number):
        buzzer.value(1)
        sleep_ms(200)
        buzzer.value(0)
        sleep_ms(200)
    return


def setup():
    """ Setup function. Initialize hardware, run a small self test. """
    # beep one time, ensures the beeper is off afterwards
    beep_n_times(1)
    # flash all LEDs three times
    # range(7) means the variable i loops through 0, 1, 2, 3, 4, 5, 6
    # (i & 1) == 0 if i is divisible by two, so the LED is on when i==1,3,5 and off when i==0,2,4,6
    # By counting up to an even number we make sure all LEDs are turned off at the end.
    for i in range(7):
        led_red.value(i & 1)
        led_green.value(i & 1)
        led_orange.value(i & 1)
        sleep_ms(200)
    return


def loop():
    """ This is the main execution loop. """
    if button.value() == 1:  # if button is pressed
        led_red.value(1)
        beep_n_times(10)  # beep ten times
        sleep_ms(5000)
        led_orange.value(1)
        sleep_ms(2000)
        led_red.value(0)
        led_orange.value(0)
        led_green.value(1)
        sleep_ms(5000)
        led_green.value(0)
        led_orange.value(1)
        sleep_ms(5000)
        led_orange.value(0)
    # else: (otherwise) we do nothing
    return


# main program --------------------------------------------
# With setup() and loop() our program structure is similar to an Arduino sketch.
setup()
while True:
    loop()

# eof
