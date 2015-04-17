import sys
import paho.mqtt.client as mqtt
from paho.mqtt.client import MQTTv311, MQTTv31

from pyramid.paster import bootstrap

from pulsafeservice.models import initialize_sql, DBSession, Log

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("pulsafe/+", 2)

def on_disconnect(client, userdata, rc):
    print("Disconnected with result code "+str(rc))

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))


def main(argv):

    client = mqtt.Client(protocol=3)
    client.on_connect = on_connect
    client.on_disconnect = on_disconnect
    client.on_message = on_message

    #client.username_pw_set("somkzabk", "_phIeEBlWnxP")
    #client.connect("m20.cloudmqtt.com", 11741, 60)
    #client.connect("test.mosquitto.org", 8884, 60)
    client.connect("broker.mqttdashboard.com", 1883, 60)

    client.loop_forever()

if __name__ == '__main__':
    main(sys.argv)
