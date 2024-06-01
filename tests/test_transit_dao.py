import unittest
from unittest.mock import patch, Mock
from dao.transit_dao import get_transit_schedule_dao


class TransitDAOTestCase(unittest.TestCase):

    @patch('dao.transit_dao.create_db_connection')
    def test_get_transit_schedule_dao(self, mock_create_db_connection):
        # Create a mock database connection and cursor
        mock_connection = Mock()
        mock_cursor = Mock()

        # Set the mock connection to return the mock cursor
        mock_create_db_connection.return_value = mock_connection
        mock_connection.cursor.return_value = mock_cursor

        # Mock cursor's fetchall method to return mock data
        mock_cursor.fetchall.return_value = [
            {
                'transit_mode': 'train',
                'estimated_arrival_origin': '2024-06-01 10:00:00',
                'estimated_arrival_destination': '2024-06-01 12:00:00'
            }
        ]

        schedules = get_transit_schedule_dao('1', '2', 1, 10)

        self.assertIsInstance(schedules, list)
        self.assertEqual(len(schedules), 1)
        self.assertEqual(schedules[0]['transit_mode'], 'train')

        # Ensure the query was executed with the correct parameters
        mock_cursor.execute.assert_called_once_with(
            """
    SELECT transit_mode, estimated_arrival_origin, estimated_arrival_destination
    FROM train_schedule
    WHERE origin_station_id = %s AND destination_station_id = %s
    ORDER BY estimated_arrival_origin
    LIMIT %s OFFSET %s
    """,
            ('1', '2', 10, 0)
        )

        # Ensure cursor and connection are properly closed
        mock_cursor.close.assert_called_once()
        mock_connection.close.assert_called_once()


if __name__ == '__main__':
    unittest.main()
