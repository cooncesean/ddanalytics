from flask import Flask
from flask_environments import Environments
from flask_login import LoginManager
from flask.ext.mongoengine import MongoEngine
from mongoengine.connection import ConnectionError
from raven.contrib.flask import Sentry

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

# Configure Sentry/error logging
sentry = Sentry(
    app,
    dsn='https://cf84591bc153450c9a0ca18e35616d5d:3c1ec9c846da43dbb2981f8ce6a1e7db@app.getsentry.com/4404'
)

# Import the app's views
from ddanalytics.views import *
