import datetime
from ddanalytics import db
from flask import url_for
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
    flights = db.ListField(db.EmbeddedDocumentField('Drone'))
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
        document.user.drones.remove(document)
        document.user.save()

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
        document.user.flights.remove(document)
        document.user.save()

post_save.connect(FlightHistory.post_save, sender=FlightHistory)
post_delete.connect(FlightHistory.post_delete, sender=FlightHistory)
