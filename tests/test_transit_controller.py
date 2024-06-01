import unittest
from flask import Flask
from controller.transit_controller import transit_schedule_bp

class TransitControllerTestCase(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(transit_schedule_bp, url_prefix='/transit')
        self.client = self.app.test_client()

    def test_get_transit_schedule_success(self):
        """Test getting transit schedule with valid parameters"""
        response = self.client.get('/transit/schedule?origin_station_id=1&destination_station_id=2')
        self.assertEqual(response.status_code, 200)
        self.assertIn('next_schedules', response.json)

    def test_get_transit_schedule_missing_origin(self):
        """Test missing origin_station_id parameter"""
        response = self.client.get('/transit/schedule?destination_station_id=2')
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.json)
        self.assertEqual(response.json['error'], 'origin_station_id is required')

    def test_get_transit_schedule_missing_destination(self):
        """Test missing destination_station_id parameter"""
        response = self.client.get('/transit/schedule?origin_station_id=1')
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.json)
        self.assertEqual(response.json['error'], 'destination_station_id is required')

    def test_get_transit_schedule_invalid_page(self):
        """Test invalid page parameter"""
        response = self.client.get('/transit/schedule?origin_station_id=1&destination_station_id=2&page=invalid')
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.json)
        self.assertEqual(response.json['error'], 'Invalid value for page')

    def test_get_transit_schedule_invalid_per_page(self):
        """Test invalid per_page parameter"""
        response = self.client.get('/transit/schedule?origin_station_id=1&destination_station_id=2&per_page=invalid')
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.json)
        self.assertEqual(response.json['error'], 'Invalid value for per_page')

    def test_get_transit_schedule_large_page(self):
        """Test large page number"""
        response = self.client.get('/transit/schedule?origin_station_id=1&destination_station_id=2&page=1000000')
        self.assertEqual(response.status_code, 200)
        self.assertIn('next_schedules', response.json)
        self.assertEqual(response.json['next_schedules'], [])

if __name__ == '__main__':
    unittest.main()
