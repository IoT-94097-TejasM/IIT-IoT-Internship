import paho.mqtt.client as mqtt
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="healthcare"
)
cursor = db.cursor()

pulse = None
spo2 = None

def on_message(client, userdata, msg):
    global pulse, spo2

    value = int(msg.payload.decode())

    if msg.topic == "health/pulse":
        pulse = value
        print("Pulse:", pulse)

    elif msg.topic == "health/spo2":
        spo2 = value
        print("SpO2:", spo2)

    if pulse is not None and spo2 is not None:
        # Store data
        cursor.execute(
            "INSERT INTO patient_data (pulse, spo2) VALUES (%s, %s)",
            (pulse, spo2)
        )
        db.commit()

        # Check thresholds
        if pulse < 60 or pulse > 100:
            alert_msg = f"ALERT: Abnormal Pulse = {pulse} BPM"
            send_alert(alert_msg)

        if spo2 < 95:
            alert_msg = f"ALERT: Low SpO2 Level = {spo2}%"
            send_alert(alert_msg)

        pulse = None
        spo2 = None

def send_alert(message):
    print(message)

    cursor.execute(
        "INSERT INTO alerts (message) VALUES (%s)",
        (message,)
    )
    db.commit()

    client.publish("health/alert", message)

client = mqtt.Client()
client.connect("localhost", 1883, 60)

client.subscribe("health/pulse")
client.subscribe("health/spo2")

client.on_message = on_message

print("Healthcare Monitoring Subscriber Started...")
client.loop_forever()