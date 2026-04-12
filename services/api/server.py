from flask import Flask, request, jsonify
import paho.mqtt.client as mqtt

app = Flask(__name__)

# koneksi ke MQTT broker
mqtt_client = mqtt.Client()
mqtt_client.connect("broker", 1883, 60)

# endpoint lama (GET)
@app.route("/data", methods=["GET"])
def get_data():
    return jsonify({"message": "Gunakan POST /send untuk kirim data suhu"})

# 🔥 endpoint baru (POST)
@app.route("/send", methods=["POST"])
def send_data():
    suhu = request.form.get("suhu")

    if not suhu:
        return jsonify({"error": "Suhu tidak boleh kosong"}), 400

    data = f"Suhu: {suhu}°C"

    mqtt_client.publish("sensor/suhu", data)

    return jsonify({
        "status": "berhasil",
        "data_dikirim": data
    })

app.run(host="0.0.0.0", port=5000)