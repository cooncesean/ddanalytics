from flask import Flask
from flask_login import LoginManager

app = Flask(__name__)

from ddanalytics.views import *

login_manager = LoginManager()
login_manager.init_app(app)
