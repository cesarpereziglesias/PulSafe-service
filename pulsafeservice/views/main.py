import paho.mqtt.publish as publish

from pyramid.view import view_config
import pyramid.httpexceptions as exc

class Main:

    def __init__(self, request):
        self._request = request

    @view_config(route_name='home', renderer='main/home.mako')
    def home(self):
        return {}


    @view_config(route_name='broadcast')
    def broadcast(self):
        publish.single("pulsafe/command/publish",
                       qos=2,
                       hostname="broker.mqttdashboard.com")
        raise exc.HTTPFound(self._request.route_url("home"))
