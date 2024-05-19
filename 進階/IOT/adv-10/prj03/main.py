from machine import Pin
import dht
import time
import mcu


gpio = mcu.gpio()
d = dht.DHT11(Pin(gpio.D0, Pin.IN))

while True:
    d.measure()
    temp = d.temperature()
    hum = d.humidity()
    print(f"humidity: {hum:02d}, Temperture: {temp:02d}{'\u00b0'}C")
    time.sleep(1)