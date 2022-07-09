from flask import request
from flask_restx import Namespace, Resource, fields

namespace = Namespace('emailValidation', 'Checking if the email is good formated')

@namespace.route('')
class emailValidation(Resource):

    @namespace.param('email', 'Example : test@gmail.com')
    @namespace.response(200, 'API sent a response')
    @namespace.response(500, 'Internal Server Error')
    def post(self):
        'Give an email in parameters and it says if it is good formated or not'
