import time
import paho.mqtt.client as mqtt

client = mqtt.Client()
client.connect("broker", 1883, 60)

while True:
    suhu = input("Masukkan suhu: ")
    data = f"Suhu: {suhu}°C"
    print("[PUBLISHER] Kirim:", data)
    client.publish("sensor/suhu", data)