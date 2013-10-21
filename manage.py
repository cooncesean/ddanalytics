"""
Flask-Script management file. Allows devs to write/run
app specific commands from the command line.

Note the `env` option which allows the user to specify the
appropriate config class when running a command. If no
`-e` option is specified, the default environment will be
`ddanalytics.config.Development`.

Usage:
    # Run the `bootstrap` command using the `Test` config
    > python manage.py bootstrap -e TEST
"""
import os
import sys
import unittest
from flask.ext.script import Manager, Server, Command
from ddanalytics import create_application

# Create the application w/ the specified environment
manager = Manager(create_application)
manager.add_option('-e', '--env', dest='default_env', required=False)

# Turn on debugger by default and reloader
manager.add_command("runserver", Server(
    use_debugger = True,
    use_reloader = True,
    host = '0.0.0.0')
)

@manager.command
def bootstrap():
    " Flush the data store and install fixtures; return the site to 'bootstrapped' state. "
    from ddanalytics.utils import flush_database, generate_dev_data

    # Prompt user
    if raw_input('Are you sure you want to flush your local data? [y/n]') not in ['y', 'yes']:
        return

    # Flush the database
    # db.dropDatabase() -- there isnt' a mongoengine flush db command???
    utils.flush_database()

    # Load data
    utils.generate_dev_data()

class RunTestCommand(Command):
    " Run unit tests for the project. "

    def __init__(self, default_env='TEST'):
        self.default_env = default_env
        super(RunTestCommand, self).__init__()

    def run(self):
        from ddanalytics.tests import TestModels
        suite = unittest.TestLoader().loadTestsFromTestCase(TestModels)
        unittest.TextTestRunner(verbosity=2).run(suite)

    # def get_options(self):
    #     option_list = super(RunTestCommand, self).get_options()
    #     return option_list

manager.add_command('run_tests', RunTestCommand())

if __name__ == "__main__":
    manager.run()
