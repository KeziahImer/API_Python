from flask import request
from flask_restx import Namespace, Resource, fields

namespace = Namespace('emailValidation', 'Checking if the email is good formated')

@namespace.route('')
class emailValidation(Resource):

    @namespace.param('Query String', 'http://ipadress:port/emailValidation?email=youremail')
    @namespace.response(False, 'Email is not valid')
    @namespace.response(True, 'Email is valid')
    def post(self):
        'Checking email'
