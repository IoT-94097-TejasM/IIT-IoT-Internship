from flask import Flask, request

app = Flask(__name__)

# ---------- Home ----------
@app.route("/")
def home():
    return "Flask Server Running Successfully"


# ---------- Store Temperature ----------
@app.route("/send_temperature")
def send_temperature():
    temp = request.args.get("value")

    if temp is None:
        return "Error: temperature value missing", 400

    with open("temperature.txt", "a") as f:
        f.write(temp + "\n")

    return "Temperature stored successfully"


# ---------- Store Light Intensity ----------
@app.route("/send_light")
def send_light():
    light = request.args.get("value")

    if light is None:
        return "Error: light value missing", 400

    with open("light.txt", "a") as f:
        f.write(light + "\n")

    return "Light intensity stored successfully"


# ---------- Display Temperature ----------
@app.route("/get_temperature")
def get_temperature():
    try:
        with open("temperature.txt", "r") as f:
            data = f.read()
    except FileNotFoundError:
        data = "No temperature data available"

    return "<pre>" + data + "</pre>"


# ---------- Display Light ----------
@app.route("/get_light")
def get_light():
    try:
        with open("light.txt", "r") as f:
            data = f.read()
    except FileNotFoundError:
        data = "No light data available"

    return "<pre>" + data + "</pre>"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
