import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("Conectado al broker")

def on_message(client, userdata, message):
    print("Mensaje recibido Soy S3: " + message.payload.decode())

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", 1883)
client.subscribe("topic/example")

# Bucle infinito para recibir mensajes
while True:
    client.loop()
