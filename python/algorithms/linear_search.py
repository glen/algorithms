class LinearSearch:
  def __init__(self, search_array):
    self.search_array = search_array

  def search(self, target):
    for index, element in enumerate(self.search_array):
      if target == element:
        return index
    return -1
