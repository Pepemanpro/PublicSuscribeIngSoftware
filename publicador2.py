import time
import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("Conectado al broker")

def on_publish(client, userdata, mid):
    print("Mensaje publicado")

client = mqtt.Client()
client.on_connect = on_connect
client.on_publish = on_publish

client.connect("localhost", 1883)

# Bucle infinito para publicar mensajes
while True:
    message = "Hola soy el publicador 2"
    client.publish("topic/example", message)
    time.sleep(10)

