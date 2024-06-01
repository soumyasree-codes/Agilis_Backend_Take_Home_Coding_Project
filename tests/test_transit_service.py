import unittest
from unittest.mock import patch, Mock
from service.transit_service import get_transit_schedule_service


class TransitServiceTestCase(unittest.TestCase):

    @patch('service.transit_service.get_transit_schedule_dao')
    def test_get_transit_schedule_service(self, mock_get_transit_schedule_dao):
        # Mock the DAO function to return mock data
        mock_get_transit_schedule_dao.return_value = [
            {
                'transit_mode': 'train',
                'estimated_arrival_origin': '2024-06-01 10:00:00',
                'estimated_arrival_destination': '2024-06-01 12:00:00'
            }
        ]

        result = get_transit_schedule_service('1', '2',
                                              None, None, 1, 10)

        self.assertIsInstance(result, dict)
        self.assertIn('next_schedules', result)
        self.assertEqual(len(result['next_schedules']), 1)
        self.assertEqual(result['next_schedules'][0]['transit_mode'], 'train')


if __name__ == '__main__':
    unittest.main()
