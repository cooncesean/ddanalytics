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

    def test_most_used_drone(self):
        " Assert the `User.most_used_drone()` method returns the most used Drone based on flight history of the user. "
        raise

    def test_flight_history_by_month_and_drone(self):
        " Assert the `User.flight_history_by_month_and_drone()` returns the expected data based on the user's flight history. "
        raise

if __name__ == '__main__':
    unittest.main()
