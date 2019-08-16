import math
import pdb


class BinarySearch:
    def __init__(self, search_array):
        search_array.sort()
        self.search_array = search_array
        self.iteration = 0

    def search(self, target, low_index=0, high_index=None):
        if high_index is None:
            high_index = high_index or len(self.search_array) - 1
        self.iteration += 1
        if high_index >= low_index:
            mid_index = low_index + math.ceil((high_index - low_index)/2.0)
            if self.search_array[mid_index] == target:
                return mid_index
            elif self.search_array[mid_index] < target:
                return self.search(target, mid_index + 1, high_index)
            elif self.search_array[mid_index] > target:
                return self.search(target, low_index, mid_index - 1)
        else:
            return -1
