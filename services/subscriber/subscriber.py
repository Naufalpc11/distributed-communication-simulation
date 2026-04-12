import paho.mqtt.client as mqtt

def on_message(client, userdata, msg):
    print("[SUBSCRIBER] Terima:", msg.payload.decode())

client = mqtt.Client()
client.connect("broker", 1883, 60)

client.subscribe("sensor/suhu")
client.on_message = on_message

client.loop_forever()