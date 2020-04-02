from python import run_algorithm
#import run_algorithm
import unittest
import sys
import json
from unittest.mock import patch
from python.lib import read_data
from contextlib import contextmanager
from io import StringIO
import algorithms
import pdb

@contextmanager
def captured_output():
    new_out, new_err = StringIO(), StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err


class runAlgorithmTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def test_no_command_line_arguments(self):
        with patch.object(sys, 'argv', []):
            with self.assertRaises(SystemExit):
                run_algorithm.RunAlgorithm()

    def test_no_command_line_arguments_stdout(self):
        with patch.object(run_algorithm.RunAlgorithm, 'AVAILABLE_ALGORITHMS', ('linear_search')):
            with patch.object(sys, 'argv', []):
                expected_ouput = "Invalid input!\nRun code like this \"python run_algorithm.py [algorithm_name] [number_to_search]\""
                with self.assertRaises(SystemExit):
                    with captured_output() as (out, err):
                        run_algorithm.RunAlgorithm()
                output = out.getvalue().strip()
                self.assertEqual(expected_ouput, output)

    def test_single_command_line_argument(self):
        with patch.object(sys, 'argv', ['python', 'run_algorithm.py']):
            with self.assertRaises(SystemExit):
                run_algorithm.RunAlgorithm()

    def test_two_command_line_arguments_with_incorrect_algorithm_provided(self):
        algos = ('linear_search', 'bubble_sort')
        with patch.object(run_algorithm.RunAlgorithm, 'AVAILABLE_ALGORITHMS', algos):
            with patch.object(sys, 'argv', ['python', 'run_algorithm.py', 'linear_search1']):
                expected_ouput = "Available Algorithms are " + str(algos)
                with self.assertRaises(SystemExit):
                    with captured_output() as (out, err):
                        run_algorithm.RunAlgorithm()
                output = out.getvalue().strip()
                self.assertEqual(expected_ouput, output)

    def test_two_command_line_arguments_with_correct_algorithm_provided_but_no_search_input(self):
        algos = ('linear_search')
        with patch.object(run_algorithm.RunAlgorithm, 'AVAILABLE_ALGORITHMS', algos):
            with patch.object(sys, 'argv', ['python', 'linear_search']):
                expected_ouput = "Invalid input!\nRun code like this \"python run_algorithm.py [algorithm_name] [number_to_search]\""
                with self.assertRaises(SystemExit):
                    with captured_output() as (out, err):
                        run_algorithm.RunAlgorithm()
                output = out.getvalue().strip()
                self.assertEqual(expected_ouput, output)

    def test_three_command_line_arguments_with_correct_search_alogrithm_and_input_present(self):
        with patch.object(run_algorithm.RunAlgorithm, 'AVAILABLE_ALGORITHMS', ('linear_search')):
            with patch.object(sys, 'argv', ['run_algorithm.py', 'linear_search', 7]):
                with patch.object(json, 'load', return_value={'input': [5, 7, 2, 3]}):
                    expected_output = "Yes"
                    with captured_output() as (out, err):
                        x = run_algorithm.RunAlgorithm()
                        self.assertEqual(x.locate(), 2)
                        x.print_search_result()
                    output = out.getvalue().strip()
                    self.assertIn(expected_output, output)


    def test_three_command_line_arguments_with_correct_search_alogrithm_and_input_absent(self):
        with patch.object(run_algorithm.RunAlgorithm, 'AVAILABLE_ALGORITHMS', ('linear_search')):
            with patch.object(json, 'load', return_value={'input': [5, 7, 2, 3]}):
                with patch.object(sys, 'argv', ['python', 'linear_search', 12]):
                    self.assertEqual(run_algorithm.RunAlgorithm().locate(12), -1)

    def test_three_command_line_arguments_with_correct_sort_alogrithm(self):
        with patch.object(run_algorithm.RunAlgorithm, 'AVAILABLE_ALGORITHMS', ('bubble_sort')):
            with patch.object(sys, 'argv', ['run_algorithm.py', 'bubble_sort']):
                with patch.object(json, 'load', return_value={'input': [5, 7, 2, 3]}):
                    expected_output = "3"
                    with captured_output() as (out, err):
                        x = run_algorithm.RunAlgorithm()
                        x.sort()
                        x.print_sort_steps()
                    output = out.getvalue().strip()
                    self.assertIn(expected_output, output)


if __name__ == '__main__':
    unittest.main()
