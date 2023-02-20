# Original example taken from https://www.waveshare.com/wiki/Template:Raspberry_Pi_Pico_Example#Traffic_Light_System_Testing
# Adjusted for introduction course 'HBO-ICT proefstuderen'. Traffic Light Example with the Raspberry Pi Pico.
# 2023 by noharm

import machine
import utime
import _thread

led_red = machine.Pin(15, machine.Pin.OUT)
led_orange = machine.Pin(14, machine.Pin.OUT)
led_green = machine.Pin(13, machine.Pin.OUT)
button = machine.Pin(16, machine.Pin.IN, machine.Pin.PULL_DOWN)
buzzer = machine.Pin(12, machine.Pin.OUT)

global button_pressed
button_pressed = False

def button_reader_thread(): 
    while True:
        if button.value() == 1:
            print("button pressed")
            button_pressed = True
            
_thread.start_new_thread(button_reader_thread, ())

while True:
    if button_pressed == True: 
        led_red.value(1) 
        for i in range(10): 
            buzzer.value(1) 
            utime.sleep(0.2) 
            buzzer.value(0) 
            utime.sleep(0.2) 
        button_pressed = False
    led_red.value(1) 
    utime.sleep(5) 
    led_orange.value(1) 
    utime.sleep(2) 
    led_red.value(0) 
    led_orange.value(0) 
    led_green.value(1) 
    utime.sleep(5) 
    led_green.value(0) 
    led_orange.value(1) 
    utime.sleep(5) 
    led_orange.value(0)