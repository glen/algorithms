import sys
import pdb
from termcolor import colored
sys.path.append('../')
from python.lib import read_data
from python.lib import helper


class RunAlgorithm:
    AVAILABLE_ALGORITHMS = ('linear_search')
    INPUT_FILE = 'data/input.json'
    LOG = sys.stdout

    def __init__(self):
        self.parse_args(sys.argv)
        self.load_algorithm(self.algorithm_to_run)

    def parse_args(self, args=[]):
        if len(args) < 3:
            self.LOG.write('Invalid input!\nRun code like this "python run_algorithm [algorithm_name] [number_to_search]"')
            sys.exit(0)

        self.algorithm_to_run = sys.argv[1]

        if self.algorithm_to_run not in self.AVAILABLE_ALGORITHMS:
            print('Available algorithms are ', self.AVAILABLE_ALGORITHMS)
            sys.exit(0)

        self.target = int(sys.argv[2])

    def load_algorithm(self, algorithm_to_load):
        package = 'python.algorithms'
        self.imported = getattr(__import__(package, fromlist=[algorithm_to_load]), algorithm_to_load)

    def locate(self, target=None):
        if target is None:
            target = self.target
        self.input_data = read_data.read_json_file(self.INPUT_FILE)
        x = eval(f"self.imported.{helper.class_name(self.algorithm_to_run)}(self.input_data['input'])")
        self.located_position = x.search(target)
        return self.located_position

    def print_result(self):
        algorithm_name = helper.class_name(self.algorithm_to_run)
        print(colored(f" {algorithm_name} ".center(60, '#'), 'grey', 'on_white'))
        print(helper.print_label('Input', 10, 'blue'), helper.print_value(self.input_data['input'], 'yellow'))
        print(helper.print_label('Target', 10, 'blue'), helper.print_value(self.target, 'yellow'))
        print(helper.print_label('Located', 10, 'blue'), helper.print_value('Yes', 'green') if self.located_position >=0 else helper.print_value('No', 'red') )
        if self.located_position >= 0:
            print(helper.print_label('Position', 10, 'blue'), helper.print_value(self.located_position, 'yellow') )

if __name__ == '__main__':
    app = RunAlgorithm()
    app.locate()
    app.print_result()
