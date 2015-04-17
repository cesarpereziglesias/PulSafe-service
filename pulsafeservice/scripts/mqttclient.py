import sys
import paho.mqtt.client as mqtt
from paho.mqtt.client import MQTTv311

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.publish("pulsafe/thetest", "This is the content", qos=2)

def on_disconnect(client, userdata, rc):
    print("Disconnected with result code "+str(rc))

def on_publish(client, userdata, mid):
    print("Message published")

def main(argv):

    client = mqtt.Client(protocol=MQTTv311)
    client.on_connect = on_connect
    client.on_disconnect = on_disconnect
    client.on_publish = on_publish

    client.username_pw_set("somkzabk", "_phIeEBlWnxP")
    client.connect("m20.cloudmqtt.com", 11741, 60)

    client.loop_forever()

if __name__ == '__main__':
    main(sys.argv)
