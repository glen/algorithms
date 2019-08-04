import sys
from termcolor import colored
import read_data

INPUT_FILE = 'input.json'

class LinearSearch:
  def __init__(self, search_array):
    self.search_array = search_array

  def search(self, target):
    for index, element in enumerate(self.search_array):
      if target == element:
        return index
    
    return -1

target = int(sys.argv[1])

input_data = read_data.read_json_file(INPUT_FILE)
x = LinearSearch(input_data['input'])
located_position = x.search(target)

print( colored(' Linear Search Implementation '.center(60, '#'), 'grey', 'on_white') )
print( colored('Input:'.ljust(10), 'blue'), colored(input_data['input'], 'yellow') )
print( colored('Target:'.ljust(10), 'blue'), colored(target, 'yellow') )
print( colored('Located:'.ljust(10), 'blue'), colored('Yes', 'green') if located_position >=0 else colored('No', 'red') )
if located_position >= 0:
  print( colored('Position:'.ljust(10), 'blue'), colored(located_position, 'yellow') )
