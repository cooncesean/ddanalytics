"""
App loader for ElasticBeanstalk. Amazon expects the app
to be loaded from `project.application.py` through the
use of the `application` var instead of `app`.
"""
from flask import Flask
from flask_environments import Environments
from flask_login import LoginManager
from flask.ext.mongoengine import MongoEngine
from mongoengine.connection import ConnectionError
from raven.contrib.flask import Sentry

# Instatiate the app and the environment
application = Flask(__name__)
env = Environments(application)
env.from_object('ddanalytics.config')
print 'CURRENT ENV: `%s`' % env.default_env

# Instantiate the mongo connection
db = MongoEngine(application)

# Instantiate and configure the login module
login_manager = LoginManager()
login_manager.init_app(application)
login_manager.login_view = 'login'

# Configure Sentry/error logging
sentry = Sentry(
    application,
    dsn='https://cf84591bc153450c9a0ca18e35616d5d:3c1ec9c846da43dbb2981f8ce6a1e7db@app.getsentry.com/4404'
)

# Import the app's views
from ddanalytics.views import *

if __name__ == '__main__':
    application.run(host='0.0.0.0', debug=True)
