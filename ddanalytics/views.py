from flask import render_template, request, url_for, redirect, \
    abort
from flask_login import login_user, login_required, logout_user, \
    current_user
from ddanalytics import login_manager, application
from ddanalytics.utils import load_user, format_number


# Main Navigation ##########################
@application.route('/')
def home():
    """
    Renders the home page for an-unauth'd user. Users who
    are auth'd will be redirected to their `analytics` page.
    """
    if current_user.is_authenticated():
        return redirect(url_for('analytics'))
    return render_template('home.html')

@application.route('/analytics/')
@login_required
def analytics():
    """
    Show auth'd users their `anaytlics` page based on mock
    data pulled in from their DroneDeploy account.
    """
    # Get `flights over time` data for the current user
    flight_history = current_user.flight_history_by_month_and_drone()

    # Format a few user fields
    current_user.highest_flight = format_number(current_user.highest_flight)
    current_user.cumulative_flights = format_number(current_user.cumulative_flights)
    current_user.formatted_drone_usage = [[k, v] for k, v in current_user.drone_usage.iteritems()]
    return render_template('analytics.html', flight_history=flight_history)

@application.route('/fleet/')
@login_required
def fleet():
    """
    Show auth'd users their `fleet` page. It renders all drone
    types in their personal fleet and shows recommendations to
    optimize their fleet based on their drones' configurations
    compared to that of the rest of the community.
    """
    recommendations = [
        {
            'drone': 'Parrot AR 2.0',
            'current_spec': {
                'battery': 'Default AR Lipo',
                'propeller': 'Default AR Propellers',
                'motor': 'Brushless Parrot Motor',
            },
            'recommendation': [
                {
                    'type': 'Battery',
                    'name': 'AR Max Life Lipo',
                    'benefit': '15% increase in batery life',
                    'link': 'http://www.amazon.com/Parrot-AR-Drone-Battery-LiPo-Replacement/dp/B0041G5Y8W?referrer_partner=%s' % application.config.get('REFERRER_PARTER_NAME')
                },
                {
                    'type': 'Propeller',
                    'name': '16" Carbon Fiber Props',
                    'benefit': '56% increase in lift',
                    'link': 'http://www.amazon.com/Parrot-Upgrade-Propeller-Blades-Carbon/dp/B00CCJL3BC?referrer_partner=%s' % application.config.get('REFERRER_PARTER_NAME')
                }
            ]
        },
        {
            'drone': 'MD4-1000',
            'current_spec': {
                'battery': 'MD4-5500 Lipo',
                'propeller': 'MD4 Prop',
                'motor': 'Brushless MD4 Motor',
            },
            'recommendation': [
                {
                    'type': 'Motor',
                    'name': 'Traxxas 3351',
                    'benefit': '32% increase in power',
                    'link': 'http://www.amazon.com/Traxxas-3351-Velineon-Brushless-Motor/dp/B000SU3VCG?referrer_partner=%s' % application.config.get('REFERRER_PARTER_NAME')
                }
            ]
        },
        {
            'drone': 'DJI Phantom',
            'current_spec': {
                'battery': 'DJI Flight Battery',
                'propeller': 'DJI Carbon Props',
                'motor': 'Brushless DJI',
            },
            'recommendation': [
                {
                    'type': 'Battery',
                    'name': 'DJI Phantom 4000 Lipo',
                    'benefit': '62% increase in battery life',
                    'link': 'http://www.bhphotovideo.com/bnh/controller/home?O=&sku=964487&Q=&is=REG&A=details&referrer_partner=%s' % application.config.get('REFERRER_PARTER_NAME')
                }
            ]
        },
        {
            'drone': 'TurboAce X830',
            'current_spec': {
                'battery': 'X830 Lipo',
                'propeller': 'X830 Polyurethane Propeller',
                'motor': 'X830 Brushless Motor',
            },
            'recommendation': [
            ]
        }
    ]
    return render_template('fleet.html', recommendations=recommendations)

# Authentication ###########################
@application.route('/login/')
def login(methods=['GET']):
    """
    'Authenticate' the user coming back from the fake
    DroneDeploy site with a mock oauth token and redirect
    them to the analytics view.
    """
    # We are faking oAuth for the sake of the demo
    if request.args.get('token', None):
        # Always load the default 'mock' user
        user = load_user(application.config.get('MOCK_USERNAME'))
        login_user(user)
        return redirect(request.args.get('next', url_for('analytics')))
    return abort(404)

@application.route('/logout/')
@login_required
def logout():
    " De-authenticate (is that a word?) the user. "
    logout_user()
    return redirect(url_for('home'))
