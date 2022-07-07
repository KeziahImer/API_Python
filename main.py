from flask import Flask, request
from documented_api import blueprint as documented_api

app = Flask(__name__)
app.config['RESTPLUS_MASK_SWAGGER'] = False

app.register_blueprint(documented_api)

@app.route('/health')
def is_running():
    return {
        'name': 'health',
        'message': 'API is running'
    }

@app.route('/longestCommonStreak')
def longest():
    return {'name': 'longestCommonStreak'}

@app.route('/emailValidation')
def is_valid():
    return {'name': 'emailValidation'}
    if 1==1:
        return True
    else:
        return False

if __name__ == "__main__":
    app.run()
