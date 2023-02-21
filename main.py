# HBO-ICT-proefstuderen: Traffic Light Example with the Raspberry Pi Pico
# Based on https://www.waveshare.com/wiki/Template:Raspberry_Pi_Pico_Example#Traffic_Light_System_Testing
# Changes 2023 by noharm, hagen-git

from machine import Pin
from time import sleep_ms

button = Pin(16, Pin.IN, Pin.PULL_DOWN)
led_red = Pin(15, Pin.OUT)
led_orange = Pin(14, Pin.OUT)
led_green = Pin(13, Pin.OUT)
buzzer = Pin(12, Pin.OUT)

global button_pressed
button_pressed = False


def beep_ten_times():
    for i in range(10):
        buzzer.value(1)
        sleep_ms(200)
        buzzer.value(0)
        sleep_ms(200)


# initialisation, turn buzzer off
buzzer.value(0)
# self test, flash all LEDs three times
# range(0) means i loops 0, 1, 2, 3, 4, 5, 6
# (i & 1) == 0 if i is divisible by two
for i in range(7):
    led_red.value(i & 1)
    led_green.value(i & 1)
    led_orange.value(i & 1)
    sleep_ms(200)

while True:
    if button.value() == 1:
        led_red.value(1)
        beep_ten_times()
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

# eof
