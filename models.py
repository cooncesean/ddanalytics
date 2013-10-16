import datetime
from ddanalytics import db
from flask import url_for
from itertools import groupby
from mongoengine.signals import post_save, post_delete


class User(db.Document):
    """
    A user of the system.
    Notes:
        - The oAuth logic/fields are all mocked for the sake of the demo.
        - The `is_anonymous`, `is_authenticated`, etc. methods required
          by `flask_login` are all mocked for the time being.
    """
    username = db.StringField(unique=True, max_length=255, required=True)
    drones = db.ListField(db.EmbeddedDocumentField('Drone'))
    flights = db.ListField(db.EmbeddedDocumentField('FlightHistory'))
    avg_flight_time = db.DecimalField()
    longest_flight_time = db.DecimalField()
    cumulative_flight_time = db.IntField()
    highest_flight = db.IntField()
    avg_flights_per_month = db.IntField()
    cumulative_flights = db.IntField()
    most_efficient_drone = db.StringField(max_length=255)
    most_used_drone = db.StringField(max_length=255)
    last_flight_date = db.DateTimeField(default=datetime.datetime.now)

    meta = {
        'indexes': ['username'],
    }

    def __unicode__(self):
        return self.username

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def get_id(self):
        return self.username

    def flight_history_by_month_and_drone(self):
        """
        Return a list of flight history objects grouped by drone model and by month.
        This data is used in the `flights_over_time` graph.

        TODO: The returned data is cached for 30 minutes.
        Sample:
        {
            'months': ['May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct'],
            'graph_data': [
                {
                    'name': 'Some Drone Model Name',
                    'data': [1, 2, 4, 6, 12, 5]
                },
                {
                    'name': 'Another Drone Model Name',
                    'data': [21, 5, 4, 6, 12, 7]
                },
            ]
        }
        """
        final_flight_history = {'months': []}
        grouped_flights = []

        # Get a set of drone models for the user
        drone_models = set([drone.model for drone in self.drones])

        # Get a filtered (sub)list of flights for each specific drone model
        for dm in drone_models:
            _data = {'name': dm, 'data': []}

            # Filter and sort the flight history by current model
            filtered_flights = [flight for flight in self.flights if flight.drone.model == dm]
            filtered_flights.sort(key=lambda x:x.flight_date)

            # Group and sum the month counts
            for k, v in groupby(filtered_flights, key=lambda x:x.flight_date.strftime('%b')):
                _data['data'].append(len([d for d in v]))
                final_flight_history['months'].append(k)

            grouped_flights.append(_data)

        final_flight_history['graph_data'] = grouped_flights
        return final_flight_history

class Drone(db.Document):
    " A drone object that belongs to a specific user. "
    user = db.ReferenceField(User)
    model = db.StringField(max_length=255, required=True)
    manufacturer = db.StringField(max_length=255, required=True)
    battery = db.StringField(max_length=255)
    propeller = db.StringField(max_length=255)
    motor = db.StringField(max_length=255)

    def __unicode__(self):
        return '%s: %s[%s]' % (self.user.username, self.model, self.manufacturer)

    @classmethod
    def post_save(cls, sender, document, **kwargs):
        " Update the `User.drones` ListField. "
        if kwargs.get('created', False):
            document.user.drones.append(document)
            document.user.save()

    @classmethod
    def post_delete(cls, sender, document, **kwargs):
        " Update the `User.drones` ListField. "
        try:
            document.user.drones.remove(document)
            document.user.save()
        except ValueError:
            pass

post_save.connect(Drone.post_save, sender=Drone)
post_delete.connect(Drone.post_delete, sender=Drone)

class FlightHistory(db.Document):
    " A flight log for a specific user and drone. "
    user = db.ReferenceField(User)
    drone = db.ReferenceField(Drone)
    flight_date = db.DateTimeField(default=datetime.datetime.now)

    @classmethod
    def post_save(cls, sender, document, **kwargs):
        " Update the `User.flights` ListField. "
        if kwargs.get('created', False):
            document.user.flights.append(document)
            document.user.save()

    @classmethod
    def post_delete(cls, sender, document, **kwargs):
        " Update the `User.flights` ListField. "
        try:
            document.user.flights.remove(document)
            document.user.save()
        except ValueError:
            pass

post_save.connect(FlightHistory.post_save, sender=FlightHistory)
post_delete.connect(FlightHistory.post_delete, sender=FlightHistory)
