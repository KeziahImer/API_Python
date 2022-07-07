from flask import Blueprint
from flask_restx import Api
from documented_api.hello_world import namespace as hello_world_ns

blueprint = Blueprint('documented_api', __name__, url_prefix='/documented_api')

api_extension = Api(
    blueprint,
    title='API',
    version='1.0',
    description='Just a Flask RESTX API',
    doc='/doc'
)

api_extension.add_namespace(hello_world_ns)
