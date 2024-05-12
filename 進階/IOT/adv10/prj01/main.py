import time
import mcu

wi = mcu.wifi("SingularClass", "Singular#1234")
wi.setup(ap_active=False, sta_active=True)
if wi.connect():
    print(f"IP={wi.ip}")
mqtt_client = mcu.MQTT(
    "Ethan", "mqtt.singularinnovation-ai.com", "singular", "Singular#1234"
)
mqtt_client.connect()
while True:
    msg = input("enter publish message:")
    mqtt_client.publish("owo", msg)
    time.sleep(0.1)
