import requests
import unittest
from unittest.mock import patch

def get_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

class TestDataFetching(unittest.TestCase):

    @patch('requests.get')
    def test_get_data_success(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = {'message': 'Success'}

        url = 'https://google.com'
        result = get_data(url)

        mock_get.assert_called_once_with(url)
        self.assertEqual(result, {'message': 'Success'})

    @patch('requests.get')
    def test_get_data_failure(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.status_code = 404
        mock_response.json.return_value = {'message': 'Not Found'}

        url = 'https://google.com'
        result = get_data(url)

        mock_get.assert_called_once_with(url)
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
