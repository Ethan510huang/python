from machine import Pin
from time import sleep

RED = Pin(14, Pin.OUT)
GREEN = Pin(12, Pin.OUT)
BLUE = Pin(13, Pin.OUT)
while True:
    RED.value(1)
    GREEN.value(0)
    BLUE.value(0)
    sleep(1)
    RED.value(0)
    GREEN.value(1)
    BLUE.value(0)
    sleep(1)
    RED.value(1)
    GREEN.value(1)
    BLUE.value(0)
    sleep(1)
