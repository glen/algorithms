class LinearSearch:
    def __init__(self, search_array):
        self.search_array = search_array
        self.iteration = 0
        self.located = -1

    def search(self, target):
        for index, element in enumerate(self.search_array):
            self.iteration = index + 1
            if target == element:
                return self.iteration
        return self.located
