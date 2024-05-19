import mcu
from machine import Pin, I2C
import ssd1306
import time


def on_message(topic, msg):
    global m
    msg = msg.decode("utf-8")
    m = msg
    topic = topic.decode("utf-8")
    print(f"my subscribe topic:{topic}, msg:{msg}")


wi = mcu.wifi("SingularClass", "Singular#1234")
wi.setup(ap_active=False, sta_active=True)
if wi.connect():
    print(f"IP={wi.ip}")
gpio = mcu.gpio()
i2c = I2C(scl=Pin(gpio.D1), sda=Pin(gpio.D2))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
oled.fill(0)

MQTT = mcu.MQTT("Ethan", "mqtt.singularinnovation-ai.com", "singular", "Singular#1234")
MQTT.connect()
MQTT.subscribe("owo", on_message)
m = 0
servo = mcu.servo(gpio.D8)

while True:
    MQTT.check_msg()
    servo.angle(int(m))
    time.sleep(1)
