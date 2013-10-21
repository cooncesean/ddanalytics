env = None
db = None
login_manager = None
application = None

def create_application(default_env='DEVELOPMENT'):
    """
    Util method to create a fully configured `Flask app` object for
    production/development/testing envs. We set all config'd objects
    as globals so they can be imported at the module level.
    """
    from flask import Flask
    from flask_environments import Environments
    from flask_login import LoginManager
    from flask.ext.mongoengine import MongoEngine
    from mongoengine.connection import ConnectionError
    from raven.contrib.flask import Sentry

    global application
    global env
    global db
    global login_manager

    # Instatiate the app and the environment
    application = Flask(__name__)
    env = Environments(application, default_env=default_env)
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

    # Import (and route) all views
    from ddanalytics.views import *

    return application
