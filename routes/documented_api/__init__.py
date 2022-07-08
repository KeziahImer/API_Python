import email
from flask import Blueprint
from flask_restx import Api
from routes.documented_api.health import namespace as health_ns
from routes.documented_api.longest_common_streak import namespace as lcs_ns
from routes.documented_api.email_validation import namespace as emailValidation_ns

blueprint = Blueprint('documented_api', __name__, url_prefix='/documented_api')

api_extension = Api(
    blueprint,
    title='API',
    version='1.0',
    description='Just a Flask RESTX API',
    doc='/doc'
)

api_extension.add_namespace(health_ns)
api_extension.add_namespace(lcs_ns)
api_extension.add_namespace(emailValidation_ns)
