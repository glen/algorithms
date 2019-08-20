import sys
sys.path.append('../')
from python.algorithms import bubble_sort
import unittest

class TestBubbleSort(unittest.TestCase):
    def setUp(self):
        self.bubble_sort = bubble_sort.BubbleSort([5, 1, 4, 2, 8])
        self.bubble_sort.sort()
    
    def test_sort(self):
        self.assertEqual(self.bubble_sort.iteration, 3)

