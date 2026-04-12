import time
import paho.mqtt.client as mqtt
import random
import sys

print("Publisher started...", flush=True)

client = mqtt.Client()
client.connect("broker", 1883, 60)

while True:
    suhu = random.randint(20, 35)
    data = f"Suhu Otomatis: {suhu}°C"

    print("[PUBLISHER] Kirim:", data, flush=True)

    client.publish("sensor/suhu", data)

    time.sleep(5)