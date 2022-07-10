from flask_restx import Namespace, Resource, fields

namespace = Namespace('emailValidation', 'Checking if the email is good formated')

ev_model = namespace.model('emailValidation', {
    'result': fields.String(example='True'),
})

@namespace.route('')
class emailValidation(Resource):

    @namespace.param('email', 'Example : test@gmail.com')
    @namespace.marshal_with(ev_model)
    @namespace.response(500, 'Internal Server Error')
    def post(self):
        'Give an email in parameters and it says if it is good formated or not'
