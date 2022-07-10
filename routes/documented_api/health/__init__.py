from doctest import Example
from flask_restx import Namespace, Resource, fields

namespace = Namespace('health', 'Checking if the API is running')

health_model = namespace.model('health', {
    'message': fields.String(example='Api is running')
})

@namespace.route('')
class health(Resource):

    @namespace.marshal_with(health_model)
    @namespace.response(505, 'Internal Server Error')
    def get(self):
        'API status'
