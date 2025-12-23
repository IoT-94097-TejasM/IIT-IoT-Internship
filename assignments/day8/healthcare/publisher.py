import paho.mqtt.client as mqtt
import random
import time

client = mqtt.Client()
client.connect("localhost", 1883, 60)

while True:
    pulse = random.randint(55, 110)
    spo2 = random.randint(90, 100)

    client.publish("health/pulse", pulse)
    client.publish("health/spo2", spo2)

    print(f"Published Pulse={pulse} BPM, SpO2={spo2}%")
    time.sleep(5)