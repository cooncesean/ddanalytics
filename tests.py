import unittest
from ddanalytics.application import application
from ddanalytics.models import User
from ddanalytics.utils import flushDatabase


class DDAnalyticsTestCase(unittest.TestCase):
    " Unit tests for the `ddanalytics` project. "
    def setUp(self):
        # Configure test settings
        application.config['MONGODB_SETTINGS'] = {'DB': 'test-ddanalytics'}
        application.config['TESTING'] = True
        self.app = application.test_client()

        # Create default user object
        self.user = User.objects.create(username='test-user')

    def tearDown(self):
        # Flush the db
        flushDatabase()

class TestModels(DDAnalyticsTestCase):
    " Model unit tests. "

    def test_drone_post_save(self):
        " Assert the `Drone.post_save()` correctly appends the drone to the `User.drones` list. "
        raise

    def test_drone_post_delete(self):
        " Assert the `Drone.post_delete()` correctly removes the drone to the `User.drones` list. "
        raise

    def test_flight_post_save(self):
        " Assert the `Flight.post_save()` correctly appends the drone to the `User.flights` list. "
        raise

    def test_flight_post_delete(self):
        " Assert the `Flight.post_delete()` correctly removes the drone to the `User.flights` list. "
        raise

    def test_most_used_drone(self):
        " Assert the `User.most_used_drone()` method returns the most used Drone based on flight history of the user. "
        raise

    def test_flight_history_by_month_and_drone(self):
        " Assert the `User.flight_history_by_month_and_drone()` returns the expected data based on the user's flight history. "
        raise

if __name__ == '__main__':
    unittest.main()
