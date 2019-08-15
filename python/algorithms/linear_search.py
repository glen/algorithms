class LinearSearch:
    def __init__(self, search_array):
        self.search_array = search_array
        self.iteration = -1

    def search(self, target):
        for index, element in enumerate(self.search_array):
            if target == element:
                self.iteration = index
                break
        return self.iteration
