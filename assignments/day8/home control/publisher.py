import paho.mqtt.client as mqtt

client = mqtt.Client()
client.connect("localhost", 1883, 60)

while True:
    print("\n1. Light ON")
    print("2. Light OFF")
    print("3. Fan ON")
    print("4. Fan OFF")

    choice = input("Enter choice: ")

    if choice == "1":
        client.publish("home/light", "ON")
    elif choice == "2":
        client.publish("home/light", "OFF")
    elif choice == "3":
        client.publish("home/fan", "ON")
    elif choice == "4":
        client.publish("home/fan", "OFF")