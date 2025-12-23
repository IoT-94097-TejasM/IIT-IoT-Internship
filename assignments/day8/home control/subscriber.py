import paho.mqtt.client as mqtt
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="home_control"
)
cursor = db.cursor()

# Ensure one row exists
cursor.execute("INSERT IGNORE INTO appliance_status (id, light_status, fan_status) VALUES (1, 'OFF', 'OFF')")
db.commit()

def on_message(client, userdata, msg):
    status = msg.payload.decode()

    if msg.topic == "home/light":
        cursor.execute(
            "UPDATE appliance_status SET light_status=%s WHERE id=1",
            (status,)
        )
        print("Light turned", status)

    elif msg.topic == "home/fan":
        cursor.execute(
            "UPDATE appliance_status SET fan_status=%s WHERE id=1",
            (status,)
        )
        print("Fan turned", status)

    db.commit()

client = mqtt.Client()
client.connect("localhost", 1883, 60)

client.subscribe("home/light")
client.subscribe("home/fan")

client.on_message = on_message

print("Appliance status subscriber running...")
client.loop_forever()