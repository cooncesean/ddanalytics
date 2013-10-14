""""
This is the flask file that will define the views
necessary to serve the app.
"""
from flask import Flask

from ddanalytics.conf import MOCK_USERNAME, SECRET_KEY


app = Flask(__name__)

# Main Navigation ##########################
@app.route('/')
def home():
    return 're'


@app.route('/analytics/')
def analytics():
    """
    Show auth'd users their `anaytlics` page based on mock
    data pulled in from their DroneDeploy account.
    """
    return 'analytics'

@app.route('/fleet/')
def fleet():
    """
    Show auth'd users their `fleet` page. It renders all drone
    types in their personal fleet and shows recommendations to
    optimize their fleet based on their drones' configurations
    compared to that of the rest of the community.
    """
    return 'fleet'

# Authentication ###########################
@app.route('/login/')
def login():
    """
    'Authenticate' the user coming back from the fake
    DroneDeploy site with a mock oauth token and redirect
    them to the analytics view.
    """
    if 'token' in request.GET:
        session['username'] = MOCK_USERNAME
        return redirect(url_for('analytics'))
    return Http404

@app.route('/logout/')
def logout():
    " De-authenticate (is that a word?) the user. "
    session.pop('username', None)
    return redirect(url_for('index'))


app.secret_key = SECRET_KEY
if __name__ == '__main__':
    app.run()
