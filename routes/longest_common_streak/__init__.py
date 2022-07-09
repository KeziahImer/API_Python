from crypt import methods
from flask import Blueprint, request

blueprint = Blueprint('longestCommonStreak', __name__, url_prefix='/longestCommonStreak')

@blueprint.route('', methods=['POST'])
def longestCommonStreak():
    return {'name': 'longestCommonStreak'}
