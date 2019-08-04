import sys
import pdb
from termcolor import colored

def class_name(underscore_name):
  return ''.join(x.capitalize() or '_' for x in underscore_name.split('_'))

AVAILABLE_ALGORITHMS = ('linear_search')

INPUT_FILE = 'data/input.json'
algorithm_to_run = sys.argv[1]

if algorithm_to_run not in AVAILABLE_ALGORITHMS:
  print( 'Available algorithms are ', AVAILABLE_ALGORITHMS )
  sys.exit(0)

package = 'python.algorithms'
sys.path.append('../')
from python.lib import read_data
imported = getattr(__import__(package, fromlist=[algorithm_to_run]), algorithm_to_run)

target = int(sys.argv[2])

input_data = read_data.read_json_file(INPUT_FILE)
x = eval(f"imported.{class_name(algorithm_to_run)}(input_data['input'])")
located_position = x.search(target)

print( colored(' Linear Search Implementation '.center(60, '#'), 'grey', 'on_white') )
print( colored('Input:'.ljust(10), 'blue'), colored(input_data['input'], 'yellow') )
print( colored('Target:'.ljust(10), 'blue'), colored(target, 'yellow') )
print( colored('Located:'.ljust(10), 'blue'), colored('Yes', 'green') if located_position >=0 else colored('No', 'red') )
if located_position >= 0:
  print( colored('Position:'.ljust(10), 'blue'), colored(located_position, 'yellow') )
