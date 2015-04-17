from pyramid.view import view_config

from pulsafeservice.models import DBSession, Log

class Logs:

    def __init__(self, request):
        self.request = request

    @view_config(route_name='log_list', renderer='json')
    def list(self):
        return {'logs': [log.to_dict() for log in DBSession.query(Log).order_by(Log.datetime.desc())]}
