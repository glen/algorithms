import math
import pdb


class BinarySearch:
    def __init__(self, search_array):
        search_array.sort()
        self.search_array = search_array
        self.iteration = 0
        # print(self.search_array)
    
    def search(self, target, low_index = 0, high_index = None):
        high_index = high_index or len(self.search_array) - 1
        self.iteration += 1
        # print("Iteation ", self.iteration)
        # print(f"Target: {target}, low_index: {low_index}, high_index: {high_index}")
        if high_index >= low_index:
            mid_index = low_index + math.ceil((high_index - low_index)/2)
            # print(f"Mid Target: {mid_index}")
            if self.search_array[mid_index] == target:
                # print("Got it: ", mid_index)
                return mid_index
            elif self.search_array[mid_index] < target:
                return self.search(target, mid_index + 1, high_index)
            elif self.search_array[mid_index] > target:
                return self.search(target, low_index, mid_index - 1)
        else:
            return -1
