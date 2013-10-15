import datetime
import random
from ddanalytics import login_manager
from ddanalytics.models import User, Drone
from ddanalytics.conf import MOCK_USERNAME


@login_manager.user_loader
def load_user(username):
    " Callback used to reload the user object from the user ID stored in the session. "
    try:
        return User.objects.get(username=username)
    except User.DoesNotExist:
        pass
    return None

def generate_dev_data():
    " Generates a handful of dev data to bootstrap the site. "
    print 'Creating User: %s' % MOCK_USERNAME
    user = User.objects.create(
        username = MOCK_USERNAME,
        avg_flight_time = _trim_float(random.uniform(1.3, 4.7)),
        longest_flight_time = _trim_float(random.uniform(4.1, 5.2)),
        cumulative_flight_time = random.randint(354, 544),
        highest_flight = random.randint(1235, 2231),
        avg_flights_per_month = random.randint(44, 54),
        cumulative_flights = random.randint(254, 400),
        last_flight_date = datetime.datetime.now() - datetime.timedelta(days=5),
    )
    print user

    MODEL_AND_MANFACTURERS = [
        ('Parrot', 'AR 2.0', 'Default AR Lipo', 'Default AR Props', 'Brushless Parrot Motor'),
        ('MicroDrone', 'MD4-1000', 'MD4-5500 Lipo', 'MD4 Prop', 'Brushless MD4 Motor'),
        ('DJI', 'Phantom', 'DJI Flight Battery', 'DJI Carbon Props', 'Brushless DJI'),
        ('TurboAce', 'X830', 'X830 Lipo', 'X830 Polyurethane Propeller', 'X830 Brushless Motor'),
    ]
    print 'Creating Drone Army....'
    for i in range(random.randint(3, 7)):
        mm_tup = MODEL_AND_MANFACTURERS[random.randint(0, len(MODEL_AND_MANFACTURERS) - 1)]
        drone = Drone.objects.create(
            user = user,
            model = mm_tup[0],
            manufacturer = mm_tup[1],
            battery = mm_tup[2],
            propeller = mm_tup[3],
            motor = mm_tup[4],
        )
        print drone

def _trim_float(decimal, precision=2):
    " Utility method to trim a floated "
    slen = len('%.*f' % (precision, decimal))
    return float(str(decimal)[:slen])
