import unittest


class DDAnalyticsTestCase(unittest.TestCase):
    " Unit tests for the `ddanalytics` project. "
    pass

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

if __name__ == '__main__':
    unittest.main()