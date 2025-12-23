import paho.mqtt.client as mqtt
import mysql.connector

# Database connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="smart_home_monitor"
)
cursor = db.cursor()

ldr = None
temp = None

def on_message(client, userdata, msg):
    global ldr, temp

    value = float(msg.payload.decode())

    if msg.topic == "sensor/ldr":
        ldr = value
        print("LDR Received:", ldr)

    elif msg.topic == "sensor/lm35":
        temp = value
        print("Temperature Received:", temp)

    # Insert only when both values are received
    if ldr is not None and temp is not None:
        sql = "INSERT INTO sensor_readings (ldr_value, temp_value) VALUES (%s, %s)"
        cursor.execute(sql, (ldr, temp))
        db.commit()
        print("Data inserted into database\n")

        ldr = None
        temp = None

client = mqtt.Client()
client.connect("localhost", 1883, 60)

client.subscribe("sensor/ldr")
client.subscribe("sensor/lm35")

client.on_message = on_message

print("MQTT Subscriber Started...")
client.loop_forever()
