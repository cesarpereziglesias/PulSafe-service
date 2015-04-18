import sys
import json
import paho.mqtt.client as mqtt
from paho.mqtt.client import MQTTv311

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    message = {"position": "(42.42324, 8.12393)",
               "bpm": 60.6}
    #client.publish("pulsafe/users/cesar/HEARTRATE", json.dumps(message), qos=2)
    client.publish("pulsafe/command/publish", json.dumps(message), qos=2)

def on_disconnect(client, userdata, rc):
    print("Disconnected with result code "+str(rc))

def on_publish(client, userdata, mid):
    print("Message published")

def main(argv):

    client = mqtt.Client(protocol=MQTTv311)
    client.on_connect = on_connect
    client.on_disconnect = on_disconnect
    client.on_publish = on_publish

    client.connect("broker.mqttdashboard.com", 1883, 60)

    client.loop_start()
    raw_input("Press a key to quit\n")
    client.loop_stop()


if __name__ == '__main__':
    main(sys.argv)
