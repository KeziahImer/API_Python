from flask import request
from flask_restx import Namespace, Resource, fields

namespace = Namespace('health', 'Checking if the API is running')

# health_model = namespace.model('Health', {
#     'message': fields.String(
#         readwrite=True,
#         description='Is API Running ?'
#     )
# })

@namespace.route('')
class health(Resource):

    # @namespace.marshal_list_with(health_model)
    @namespace.response(200, 'API is running')
    @namespace.response(505, 'Internal Server Error')
    def get(self):
        'API status endpoint'
