"""
This file is used in conjuction with `flask-environments`
to correctly configure the app with development/prod/testing
settings.

http://pythonhosted.org/Flask-Environments/
"""
PROJECT_NAME = __name__.split('.')[0]
class Config(object):
    SECRET_KEY = 'rt3VA0Zr98j3yXRXHHjmNLWX'
    DEBUG = False
    TESTING = False
    REFERRER_PARTER_NAME = 'dronedeploy-analytics'
    MOCK_USERNAME = 'Mock User'
    ADMINS = ['cooncesean@gmail.com']
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_HOST_USER = 'stompapp@gmail.com'
    EMAIL_HOST_PASSWORD = 'c0ln1elmustard'
    EMAIL_PORT = 587

class Development(Config):
    # DEBUG = True
    MONGODB_SETTINGS = {
        'db': '%s_development_db' % PROJECT_NAME,
    }

class Production(Config):
    MONGODB_SETTINGS = {
        'db': '%s' % PROJECT_NAME,
        'username': 'coonce',
        'password': 'KvzLK8JPn6tsye',
        'host': 'mongodb://coonce:KvzLK8JPn6tsye@paulo.mongohq.com:10079/ddanalytics',
        'port': 10079
    }

class Test(Config):
    DEBUG = True
    MONGODB_SETTINGS = {
        'db': '%s_test_db' % PROJECT_NAME,
    }
    TESTING = True
