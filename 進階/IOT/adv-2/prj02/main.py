from machine import Pin, PWM
from time import sleep

frequency = 1000
duty_cycle = 0
led = PWM(Pin(2), freq=frequency, duty=duty_cycle)
delay = 0.002
while True:
    for duty_cycle in range(1023, -1, -1):
        led.duty(duty_cycle)
        sleep(delay)
    for duty_cycle in range(1024):
        led.duty(duty_cycle)
        sleep(delay)
