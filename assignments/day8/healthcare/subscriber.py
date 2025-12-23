import paho.mqtt.client as mqtt
from datetime import datetime

def on_message(client, userdata, msg):
    topic = msg.topic
    payload = msg.payload.decode()
    time_now = datetime.now().strftime("%H:%M:%S")

    # Handle pulse data
    if topic == "health/pulse":
        value = int(payload)
        print(f"{topic} → {value} at {time_now}")

    # Handle SpO2 data
    elif topic == "health/spo2":
        value = int(payload)
        print(f"{topic} → {value} at {time_now}")

        if value < 95:
            print(f"ALERT: SpO2 low ({value}%)")

    # Handle alert messages
    elif topic == "health/alert":
        print(payload)

client = mqtt.Client()
client.on_message = on_message

client.connect("localhost", 1883, 60)

client.subscribe("health/#")  # subscribe to all health topics
client.loop_forever()
