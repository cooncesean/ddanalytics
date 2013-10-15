from flask import Flask
from flask_login import LoginManager
from flask.ext.mongoengine import MongoEngine
from ddanalytics.conf import SECRET_KEY

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {'DB': 'ddanalytics'}
app.config['SECRET_KEY'] = SECRET_KEY

db = MongoEngine(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

from ddanalytics.views import *

# app.run(debug=True)
