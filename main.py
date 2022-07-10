from flask import Flask, redirect
from routes.documented_api import blueprint as documented_api
from routes.health import blueprint as health
from routes.longest_common_streak import blueprint as lcs
from routes.email_validation import blueprint as emailValidation

app = Flask(__name__)
app.config['RESTX_MASK_SWAGGER'] = False

@app.route('/')
def home():
    return redirect('/doc')

app.register_blueprint(health)
app.register_blueprint(lcs)
app.register_blueprint(emailValidation)
app.register_blueprint(documented_api)

if __name__ == "__main__":
    app.run()
