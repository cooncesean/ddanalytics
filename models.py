from ddanalytics import db
from flask import url_for


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

class DroneType(db.Document):
    " A specific brand/model of drone. "
    model_name = db.StringField(max_length=255, required=True)
    manufacturer = db.StringField(max_length=255, required=True)

    def get_absolute_url(self):
        return url_for('post', kwargs={"slug": self.slug})

    def __unicode__(self):
        return self.title
