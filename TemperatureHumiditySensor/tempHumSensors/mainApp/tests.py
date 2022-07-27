from django.test import TestCase

import time
import paho.mqtt.client as mqtt
# Create your tests here.
def on_message(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)
timetokill= 0
client =mqtt.Client(client_id='Cliente3')
client.on_message= on_message
client.connect("192.168.1.109", port=1883)
if client.is_connected:
    print('cliente conectado')
    client.subscribe("/temperatura")
    
    print("Subscribing to topic","/temperatura")
else:
    print('nada que conecta')
while client.is_connected:
    client.loop_start() #start the loop
    #client.loop_stop() #stop the loop