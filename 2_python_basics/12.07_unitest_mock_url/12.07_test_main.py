import unittest 
from unittest.mock import patch

class TestJoke(unittest.TestCase):
    @patch("main.request")
    def test_get_joke(self, mock_request):
        mock_request.get.return_value.status_code = 200
        mock_request.get.return_value.json.return_value = {"value"}
        self.assertEqual(get_joke(), "test")
        
    @patch("main.get_joke")
    def test_len_joke(self, mock_get_joke):
        mock_get_joke.return_value = "test"
        self.assertEqual(get_joke(),4)
        
        