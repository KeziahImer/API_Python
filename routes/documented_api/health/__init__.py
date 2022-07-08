from flask import request
from flask_restx import Namespace, Resource, fields

namespace = Namespace('health', 'Checking if the API is running')

@namespace.route('')
class health(Resource):

    @namespace.response(200, 'API is running')
    @namespace.response(505, 'Internal Server Error')
    def get(self):
        'API status endpoint'
