from machine import Pin
import time
import mcu

gpio = mcu.gpio()
earthquake = Pin(gpio.D3, Pin.IN)

while True:
    print(earthquake.value())
    if earthquake.value() == 1:
        print("Earthquake!")
    time.sleep(1)
