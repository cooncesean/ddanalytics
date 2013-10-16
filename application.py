"""
App loader for ElasticBeanstalk. Amazon expects the app
to be loaded from `project.application.py` through the
use of the `application` var instead of `app`.
"""
from flask import Flask, render_template
from flask_login import LoginManager
from raven.contrib.flask import Sentry

application = Flask(__name__)
sentry = Sentry(
    application,
    dsn='https://cf84591bc153450c9a0ca18e35616d5d:3c1ec9c846da43dbb2981f8ce6a1e7db@app.getsentry.com/4404'
)

@application.route('/test')
def test():
    return render_template('home.html')

from ddanalytics.views import *




if __name__ == '__main__':
    application.run(host='0.0.0.0', debug=True)