from flask import Flask, render_template
from flask_login import LoginManager
application = Flask(__name__)

@application.route('/test')
def test():
    return render_template('home.html')

# from ddanalytics.views import *

if __name__ == '__main__':
    application.run(host='0.0.0.0', debug=True)