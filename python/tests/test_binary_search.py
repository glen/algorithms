import sys
sys.path.append('../')
from python.algorithms import binary_search
import unittest

class TestBinarySearch(unittest.TestCase):
    def setUp(self):
        self.binary_search = binary_search.BinarySearch([5, 7, 4, 9, 2, 6, 3])

    def test_search_present(self):
        self.assertEqual(self.binary_search.search(5), 3)
        self.assertEqual(self.binary_search.search(2), 0)

    def test_search_absent(self):
        self.assertEqual(self.binary_search.search(11), -1)

if __name__ == '__main__':
  unittest.main()
