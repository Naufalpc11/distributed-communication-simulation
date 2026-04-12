from flask import Flask, request, jsonify
import paho.mqtt.client as mqtt

# Flask API that publishes temperature input to MQTT.
app = Flask(__name__)

# Shared MQTT client used by route handlers.
mqtt_client = mqtt.Client()

latest_auto = "Belum ada data"
latest_manual = "Belum ada data"

def on_message(client, userdata, msg):
    global latest_auto, latest_manual

    data = msg.payload.decode()

    if data.startswith("AUTO:"):
        latest_auto = data.replace("AUTO:", "")
        print("[API] Data AUTO:", latest_auto, flush=True)

    elif data.startswith("MANUAL:"):
        latest_manual = data.replace("MANUAL:", "")
        print("[API] Data MANUAL:", latest_manual, flush=True)


@app.route("/")
def home():
    return """
    <h2>Input Suhu</h2>
    <form action="/send" method="post">
        <input type="text" name="suhu" placeholder="Masukkan suhu">
        <button type="submit">Kirim</button>
    </form>
    """

@app.route("/data", methods=["GET"])
def get_data():
    return jsonify({
        "latest_data (auto)": latest_auto,
        "latest_manual": latest_manual

    })

# Validate form input then publish to topic sensor/suhu.
@app.route("/send", methods=["POST"])
def send_data():
    suhu = request.form.get("suhu")

    if not suhu:
        return jsonify({"error": "Suhu tidak boleh kosong"}), 400

    data = f"Suhu Input Manual: {suhu}°C"

    mqtt_client.publish("sensor/suhu", data)

    return jsonify({
        "status": "berhasil",
        "data_dikirim": data
    })

app.run(host="0.0.0.0", port=5000)