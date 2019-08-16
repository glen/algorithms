import sys
import os
sys.path.append('../')
from python.lib import read_data
import unittest
from unittest.mock import patch, mock_open, Mock

class TestReadData(unittest.TestCase):

    def test_read_json_data_file_present(self):
        os.path.isfile = Mock(return_value=True)
        with patch("builtins.open", mock_open(read_data='{"input": [5, 4, 6, 7]}')) as mock_file:
            assert read_data.read_json_file('some_file') == {"input": [5, 4, 6, 7]}

    def test_read_json_data_file_not_present(self):
        # os.path.isfile = Mock(return_value=False)
        not_present_file = 'some_file'
        with self.assertRaises( read_data.FileNotFoundError ):
            read_data.read_json_file(not_present_file)

if __name__ == '__main__':
  unittest.main()
