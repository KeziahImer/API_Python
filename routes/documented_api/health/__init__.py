from flask_restx import Namespace, Resource

namespace = Namespace('health', 'Checking if the API is running')

@namespace.route('')
class health(Resource):

    @namespace.response(200, 'Api is running')
    @namespace.response(505, 'Internal Server Error')
    def get(self):
        'API status'
