from umqtt.simple import MQTTClient
import sys
import time
import mcu


def on_message(topic, msg):
    msg = msg.decode("utf-8")
    topic = topic.decode("utf-8")
    print(f"my subscribe topic:{topic}, msg:{msg}")


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
while True:
    mqttClient0.check_msg()
    mqttClient0.ping()
    time.sleep(0.1)
