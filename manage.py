import inspect
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask.ext.script import Manager, Server
from ddanalytics import app, db, utils, models, tests

app.debug=True
manager = Manager(app)

# Turn on debugger by default and reloader
manager.add_command("runserver", Server(
    use_debugger = True,
    use_reloader = True,
    host = '0.0.0.0')
)

@manager.command
def bootstrap():
    " Flush the data store and install fixtures; return the site to 'bootstrapped' state. "
    # Only flush dev/staging envs
    if app.debug != True:
        return 'You can only bootstrap staging/dev sites (not production).'

    # Prompt user
    if raw_input('Are you sure you want to flush your local data? [y/n]') not in ['y', 'yes']:
        return

    # Flush the database
    # db.dropDatabase() -- there isnt' a flush database command???
    print 'Flushing database....'
    for name, cls in inspect.getmembers(models, inspect.isclass):
        if issubclass(cls, db.Document):
            cls.objects.all().delete()

    # Load data
    utils.generate_dev_data()

if __name__ == "__main__":
    manager.run()
