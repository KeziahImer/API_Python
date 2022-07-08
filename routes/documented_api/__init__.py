from flask import Blueprint
from flask_restx import Api
from routes.documented_api.health import namespace as health_ns

blueprint = Blueprint('documented_api', __name__, url_prefix='/documented_api')

api_extension = Api(
    blueprint,
    title='API',
    version='1.0',
    description='Just a Flask RESTX API',
    doc='/doc'
)

api_extension.add_namespace(health_ns)
