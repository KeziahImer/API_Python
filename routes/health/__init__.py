from flask import Blueprint

blueprint = Blueprint('health', __name__, url_prefix='/health')

@blueprint.route('')
def health():
    return {'message': 'API is running'}
