import os
import sys
import unittest
from flask.ext.script import Manager, Server
from ddanalytics import create_application

application = create_application('DEVELOPMENT')
manager = Manager(application)

from ddanalytics.utils import flush_database, generate_dev_data
from ddanalytics.tests import TestModels


# Turn on debugger by default and reloader
manager.add_command("runserver", Server(
    use_debugger = True,
    use_reloader = True,
    host = '0.0.0.0')
)

@manager.command
def bootstrap():
    " Flush the data store and install fixtures; return the site to 'bootstrapped' state. "
    # Prompt user
    if raw_input('Are you sure you want to flush your local data? [y/n]') not in ['y', 'yes']:
        return

    # Flush the database
    # db.dropDatabase() -- there isnt' a mongoengine flush db command???
    utils.flush_database()

    # Load data
    utils.generate_dev_data()

@manager.command
def run_tests():
    " Run unit tests for the project. "
    suite = unittest.TestLoader().loadTestsFromTestCase(TestModels)
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == "__main__":
    manager.run()
