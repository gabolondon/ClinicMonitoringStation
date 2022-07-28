from django.shortcuts import redirect, render
from django.http import HttpResponse
import paho.mqtt.client as mqtt

msg=['','']
def on_message(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)    
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)
    if message.topic == '/temperatura':
        msg[0]=str(message.payload.decode("utf-8"))
    elif message.topic == '/humedad':
        msg[1]=str(message.payload.decode("utf-8"))

client =mqtt.Client(client_id='Cliente3')
client.on_message= on_message
client.connect("192.168.1.109", port=1883)
client.subscribe("/temperatura")
client.subscribe("/humedad")
client.loop_start()

def index(request):
    global mensaje
    
    if client.is_connected:
        isConected='cliente conectado y suscrito a /temperatura'
    else:
        isConected='nada que conecta'

    return render(request, 'index.html', {
        'seConecto': isConected,
        'temp': msg[0],
        'hum': msg[1]
    })

# Create your views here.
