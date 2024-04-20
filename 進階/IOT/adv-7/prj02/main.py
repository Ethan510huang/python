#########################匯入模組#########################

from umqtt.simple import MQTTClient
import sys
import time
import mcu
from machine import Pin, ADC


def on_message(topic, msg):
    global m
    msg = msg.decode("utf-8")
    m = msg
    topic = topic.decode("utf-8")
    print(f"my subscribe topic:{topic}, msg:{msg}123")
    if msg == "on":
        print("OK")
        RED.value(1)
        GREEN.value(1)
        BLUE.value(1)
    elif msg == "off":
        RED.value(0)
        GREEN.value(0)
        BLUE.value(0)


#########################宣告與設定#########################
gpio = mcu.gpio()
light_sensor = ADC(0)
RED = Pin(gpio.D5, Pin.OUT)
GREEN = Pin(gpio.D6, Pin.OUT)
BLUE = Pin(gpio.D7, Pin.OUT)
wi = mcu.wifi("SingularClass", "Singular#1234")
wi.setup(ap_active=False, sta_active=True)
if wi.connect():
    print(f"IP={wi.ip}")
mq_server = "mqtt.singularinnovation-ai.com"
mqttClientId = "Ethan"
mqtt_username = "singular"
mqtt_password = "Singular#1234"
mqttClient0 = MQTTClient(
    mqttClientId, mq_server, user=mqtt_username, password=mqtt_password, keepalive=30
)
try:
    mqttClient0.connect()
except:
    sys.exit()
finally:
    print("connected MQTT server")
mqttClient0.set_callback(on_message)
mqttClient0.subscribe("owo")
m = ""
while True:
    light_sensor_reading = light_sensor.read()
    mqttClient0.check_msg()
    mqttClient0.ping()

    if m == "auto":
        if light_sensor_reading > 400:
            RED.value(1)
            GREEN.value(1)
            BLUE.value(1)
        else:
            RED.value(0)
            GREEN.value(0)
            BLUE.value(0)
    time.sleep(0.1)
