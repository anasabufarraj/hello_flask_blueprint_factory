from application.api import api


@api.route('/')
def hello_world():
    return {'Hello': 'api'}
