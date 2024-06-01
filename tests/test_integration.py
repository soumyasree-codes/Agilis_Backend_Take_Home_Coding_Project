import unittest
from flask_testing import TestCase
from app import app
from config.db_config import create_db_connection

class TransitIntegrationTestCase(TestCase):
    SQL_CREATE_TABLE = """
    CREATE TABLE IF NOT EXISTS train_schedule (
        transit_mode VARCHAR(50),
        estimated_arrival_origin DATETIME,
        estimated_arrival_destination DATETIME,
        origin_station_id VARCHAR(50),
        destination_station_id VARCHAR(50)
    );
    """
    SQL_INSERT_DATA = """
    INSERT INTO train_schedule (transit_mode, estimated_arrival_origin,
     estimated_arrival_destination, origin_station_id, destination_station_id)
    VALUES ('train', '2024-06-01 10:00:00', '2024-06-01 12:00:00', '1', '2');
    """
    SQL_DELETE_DATA = "DELETE FROM train_schedule WHERE origin_station_id = '1' AND destination_station_id = '2';"

    def create_app(self):
        app.config['TESTING'] = True
        return app

    def setUp(self):
        self.connection = create_db_connection()
        cursor = self.connection.cursor()
        cursor.execute(self.SQL_CREATE_TABLE)
        cursor.execute(self.SQL_INSERT_DATA)
        self.connection.commit()
        cursor.close()

    def tearDown(self):
        cursor = self.connection.cursor()
        cursor.execute(self.SQL_DELETE_DATA)
        self.connection.commit()
        cursor.close()
        self.connection.close()

    def test_get_transit_schedule(self):
        response = self.client.get('/transit/schedule?origin_station_id=1&destination_station_id=2')
        self.assertEqual(response.status_code, 200)
        self.assertIn('next_schedules', response.json)
        self.assertEqual(len(response.json['next_schedules']), 1)

if __name__ == '__main__':
    unittest.main()
