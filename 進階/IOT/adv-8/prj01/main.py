#########################匯入模組#########################
import time
import mcu
from machine import Pin, ADC


def on_message(topic, msg):
    global m
    msg = msg.decode("utf-8")
    m = msg
    topic = topic.decode("utf-8")
    print(f"my subscribe topic:{topic}, msg:{msg}")
    if msg == "on":
        print("OK")
        Led.RED.value(1)
        Led.GREEN.value(1)
        Led.BLUE.value(1)
    elif msg == "off":
        Led.RED.value(0)
        Led.GREEN.value(0)
        Led.BLUE.value(0)


#########################宣告與設定#########################
wi = mcu.wifi("SingularClass", "Singular#1234")
wi.setup(ap_active=False, sta_active=True)
if wi.connect():
    print(f"IP={wi.ip}")


MQTT = mcu.MQTT("Ethan", "mqtt.singularinnovation-ai.com", "singular", "Singular#1234")
MQTT.connect()
MQTT.subscribe("owo", on_message)
gpio = mcu.gpio()
Led = mcu.LED(gpio.D5, gpio.D6, gpio.D7, pwm=False)

Led.RED.value(0)
Led.GREEN.value(0)
Led.BLUE.value(0)
light_sensor = ADC(0)
m = ""
while True:
    MQTT.check_msg()
    light_sensor_reading = light_sensor.read()

    if m == "auto":
        if light_sensor_reading > 400:
            Led.RED.value(1)
            Led.GREEN.value(1)
            Led.BLUE.value(1)
        else:
            Led.RED.value(0)
            Led.GREEN.value(0)
            Led.BLUE.value(0)
    time.sleep(0.1)
