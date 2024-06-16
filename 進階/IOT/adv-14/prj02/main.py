#########################匯入模組#########################
import time
import mcu
from machine import Pin, I2C, ADC
import dht
import json
import ssd1306


#########################函式與類別定義#########################
def on_message(topic, msg):
    global m
    msg = msg.decode("utf-8")  # Byte to str
    topic = topic.decode("utf-8")
    print(f"my subscribe topic:{topic}, msg:{msg}")
    m = msg


#########################宣告與設定#########################
gpio = mcu.gpio()
i2c = I2C(scl=Pin(gpio.D1), sda=Pin(gpio.D2))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

wi = mcu.wifi("SingularClass", "Singular#1234")
wi.setup(ap_active=False, sta_active=True)
if wi.connect():
    print(f"IP={wi.ip}")

mqtt_client = mcu.MQTT(
    "owo", "mqtt.singularinnovation-ai.com", "singular", "Singular#1234"
)
mqtt_client.connect()
mqtt_client.subscribe("owo_AI", on_message)

m = "no message"
i2c = I2C(scl=Pin(gpio.D1), sda=Pin(gpio.D2))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
d = dht.DHT11(Pin(gpio.D0, Pin.IN))
msg_json = {}
adc = ADC(0)
LED = mcu.LED(gpio.D5, gpio.D6, gpio.D7)
servo = mcu.servo(gpio.D8)

#########################主程式#########################
while True:
    light_value = adc.read()
    d.measure()
    temp = d.temperature()
    hum = d.humidity()
    oled.fill(0)
    oled.text(f"Humidity:{hum:02d}", 0, 0)
    oled.text(f"Temperture:{temp:02d}C", 0, 10)
    oled.text(f"Light:{light_value:02d}", 0, 20)
    oled.show()
    msg_json["humidity"] = hum
    msg_json["temperture"] = temp
    msg_json["light sensor reading"] = light_value
    msg = json.dumps(msg_json)
    mqtt_client.publish("owo_home", msg)
    mqtt_client.check_msg()
    if m == "on":
        LED.RED.value(1)
        LED.GREEN.value(1)
        LED.BLUE.value(1)
    elif m == "off":
        LED.RED.value(0)
        LED.GREEN.value(0)
        LED.BLUE.value(0)
    if m == "0":
        servo.angle(0)
    elif m == "90":
        servo.angle(90)
    time.sleep(1)
