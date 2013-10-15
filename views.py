""""
This is the flask file that will define the views
necessary to serve the app.
"""
from flask import render_template
from ddanalytics.conf import MOCK_USERNAME, SECRET_KEY
from ddanalytics import app


# Main Navigation ##########################
@app.route('/')
def home():
    """
    Renders the home page for an-unauth'd user. Users who
    are auth'd will be redirected to their `analytics` page.
    """
    # if request.user.is_authenticated():
    #     return redirect(url_for('analytics'))
    return render_template('home.html')

@app.route('/analytics/')
def analytics():
    """
    Show auth'd users their `anaytlics` page based on mock
    data pulled in from their DroneDeploy account.
    """
    return render_template('analytics.html')

@app.route('/fleet/')
def fleet():
    """
    Show auth'd users their `fleet` page. It renders all drone
    types in their personal fleet and shows recommendations to
    optimize their fleet based on their drones' configurations
    compared to that of the rest of the community.
    """
    return render_template('fleet.html')

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
    app.run(debug=True)
