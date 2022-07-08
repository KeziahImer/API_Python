from flask import Blueprint

blueprint = Blueprint('longestCommonStreak', __name__, url_prefix='/longestCommonStreak')

@blueprint.route('')
def longestCommonStreak():
    return {'name': 'longestCommonStreak'}
