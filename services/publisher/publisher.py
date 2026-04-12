import time
import paho.mqtt.client as mqtt
import random

client = mqtt.Client()
client.connect("broker", 1883, 60)

while True:
    suhu = random.randint(20, 35)
    data = f"Suhu Otomatis: {suhu}°C"

    print("[PUBLISHER] Kirim:", data)

    client.publish("sensor/suhu", data)

    time.sleep(5)