from ddanalytics import app as application, login_manager
# from ddanalytics.views import *

@application.route('/test')
def test():
    return 'test works'

if __name__ == '__main__':
    application.run(host='0.0.0.0', debug=True)