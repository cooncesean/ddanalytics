import os
import sys
from flask import Flask
from flask_environments import Environments
from flask_login import LoginManager
from flask.ext.mongoengine import MongoEngine
from mongoengine.connection import ConnectionError

# Instatiate the app and the environment
app = Flask(__name__)
env = Environments(app)
env.from_object('ddanalytics.config')

# Instantiate the mongo connection
db = MongoEngine(app)

# Instantiate and configure the login module
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Import the app's views
from ddanalytics.views import *
