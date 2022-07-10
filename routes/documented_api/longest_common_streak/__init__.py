from curses import raw
from flask_restx import Namespace, Resource, fields

namespace = Namespace('longestCommonStreak', 'Give the longest common streak between all words')

lcs_model = namespace.model('longestCommonStreak', {
    '1 et 2': fields.String
})

@namespace.route('')
class longestCommonStreak(Resource):

    @namespace.param('Words', 'List of words to compare (separated by space)', 'body')
    @namespace.marshal_with(lcs_model)
    @namespace.response(505, 'Internal Server Error')
    def post(self):
        'Give words and it gives back the longest common streak'
