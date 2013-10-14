from flask import Flask
app = Flask(__name__)

from ddanalytics.views import *

if __name__ == '__main__':
    app.run()
