import sys
import transaction

from datetime import datetime

import paho.mqtt.client as mqtt
from paho.mqtt.client import MQTTv311, MQTTv31

from sqlalchemy import engine_from_config

from pyramid.paster import get_appsettings
from pyramid.scripts.common import parse_vars

from pulsafeservice.models import initialize_sql, DBSession, Log

def on_connect(client, userdata, flags, rc):
    client.subscribe("pulsafe/#", 2)


def on_disconnect(client, userdata, rc):
    print("Disconnected with result code "+str(rc))


def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    levels = msg.topic.split("/")
    resource = levels[1]
    if resource == "users":
        save_user_log(levels[2], levels[3], msg.payload)
    

def save_user_log(user, type_log, value):
    with transaction.manager:
        l = Log(user=user,
                datetime=datetime.now(),
                type_log=type_log,
                value=value)
        DBSession.add(l)


def main(argv):

    config_uri = argv[1]
    options = parse_vars(argv[2:])
    settings = get_appsettings(config_uri, options=options)
    engine = engine_from_config(settings, 'sqlalchemy.')
    initialize_sql(engine)

    client = mqtt.Client(protocol=3)
    client.on_connect = on_connect
    client.on_disconnect = on_disconnect
    client.on_message = on_message

    client.connect("broker.mqttdashboard.com", 1883, 60)

    client.loop_start()
    raw_input("Press a key to quit\n")
    client.loop_stop()

if __name__ == '__main__':
    main(sys.argv)
