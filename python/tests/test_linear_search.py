import sys
sys.path.append('../')
from python.algorithms import linear_search
import unittest

class TestLinearSearch(unittest.TestCase):
    def setUp(self):
        self.linear_search = linear_search.LinearSearch([5, 7, 4, 9, 2, 6, 3])

    def test_search_present(self):
        self.assertEqual(self.linear_search.search(5), 0)
  
    def test_search_absent(self):
        self.assertEqual(self.linear_search.search(11), -1)

if __name__ == '__main__':
  unittest.main()
