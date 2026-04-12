import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("[SUBSCRIBER] Terhubung ke broker", flush=True)
    client.subscribe("sensor/suhu")

def on_message(client, userdata, msg):
    print("[SUBSCRIBER] Terima:", msg.payload.decode(), flush=True)

def on_message(client, userdata, msg):
    data = msg.payload.decode()
    print("[SUBSCRIBER] Terima:", data, flush=True)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("broker", 1883, 60)

client.loop_forever()