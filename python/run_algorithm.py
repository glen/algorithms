import sys
import pdb
from termcolor import colored

AVAILABLE_ALGORITHMS = ('linear_search')

algorithm_to_run = sys.argv[1]

if algorithm_to_run not in AVAILABLE_ALGORITHMS:
  print( 'Available algorithms are ', AVAILABLE_ALGORITHMS )
  sys.exit(0)

package = 'python.algorithms'
sys.path.append('../')
from python.lib import read_data
from python.lib import helper
imported = getattr(__import__(package, fromlist=[algorithm_to_run]), algorithm_to_run)

INPUT_FILE = 'data/input.json'
target = int(sys.argv[2])

input_data = read_data.read_json_file(INPUT_FILE)
x = eval(f"imported.{helper.class_name(algorithm_to_run)}(input_data['input'])")
located_position = x.search(target)

print(colored(' Linear Search Implementation '.center(60, '#'), 'grey', 'on_white'))
print(helper.print_label('Input', 10, 'blue'), helper.print_value(input_data['input'], 'yellow'))
print(helper.print_label('Target', 10, 'blue'), helper.print_value(target, 'yellow'))
print(helper.print_label('Located', 10, 'blue'), helper.print_value('Yes', 'green') if located_position >=0 else helper.print_value('No', 'red') )
if located_position >= 0:
  print( helper.print_label('Position', 10, 'blue'), helper.print_value(located_position, 'yellow') )

