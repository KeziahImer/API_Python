from flask_restx import Namespace, Resource

namespace = Namespace('longestCommonStreak', 'Give the longest common streak between all words')

@namespace.route('')
class longestCommonStreak(Resource):

    @namespace.response(200, 'Gave all longest common streak')
    @namespace.response(505, 'Internal Server Error')
    def post(self):
        'Give words and it gives back the longest common streak'
