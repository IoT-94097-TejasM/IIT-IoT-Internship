import paho.mqtt.client as mqtt
import time
import random

client = mqtt.Client()
client.connect("localhost", 1883, 60)

while True:
    ldr_value = random.randint(200, 900)
    temp_value = round(random.uniform(22, 35), 2)

    client.publish("sensor/ldr", ldr_value)
    client.publish("sensor/lm35", temp_value)

    print(f"Published LDR={ldr_value}, Temp={temp_value}")
    time.sleep(5)