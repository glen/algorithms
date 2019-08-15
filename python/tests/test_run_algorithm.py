from python import run_algorithm
import unittest
import sys
import json
from unittest.mock import patch
from python.lib import read_data
from io import StringIO
from contextlib import contextmanager


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

    # def test_no_command_line_arguments_stdout(self):
    #     with patch.object(sys, 'argv', []):
    #         with captured_output() as (out, err):
    #             with self.assertRaises(SystemExit):
    #                 run_algorithm.RunAlgorithm()
    #             self.assertEqual(out.getvalue().strip(), 'Hello World')

    def test_single_command_line_argument(self):
        with patch.object(sys, 'argv', ['python', 'linear_search']):
            with self.assertRaises(SystemExit):
                run_algorithm.RunAlgorithm()

    def test_two_command_line_argument_but_incorrect_first_one(self):
        with patch.object(run_algorithm.RunAlgorithm, 'AVAILABLE_ALGORITHMS', ('linear_search')):
            with patch.object(sys, 'argv', ['python', 'linear_search1', 12]):
                with self.assertRaises(SystemExit):
                    run_algorithm.RunAlgorithm()

    def test_two_command_line_argument_with_target_present(self):
        with patch.object(run_algorithm.RunAlgorithm, 'AVAILABLE_ALGORITHMS', ('linear_search')):
            with patch.object(json, 'load', return_value={'input': [5, 7, 2, 3]}):
                with patch.object(sys, 'argv', ['python', 'linear_search', 7]):
                    self.assertEqual(run_algorithm.RunAlgorithm().locate(7), 1)

    def test_two_command_line_argument_with_a_different_target_present(self):
        with patch.object(run_algorithm.RunAlgorithm, 'AVAILABLE_ALGORITHMS', ('linear_search')):
            with patch.object(json, 'load', return_value={'input': [5, 7, 2, 3]}):
                with patch.object(sys, 'argv', ['python', 'linear_search', 3]):
                    self.assertEqual(run_algorithm.RunAlgorithm().locate(3), 3)

    def test_two_command_line_argument_with_target_absent(self):
        with patch.object(run_algorithm.RunAlgorithm, 'AVAILABLE_ALGORITHMS', ('linear_search')):
            with patch.object(json, 'load', return_value={'input': [5, 7, 2, 3]}):
                with patch.object(sys, 'argv', ['python', 'linear_search', 12]):
                    self.assertEqual(run_algorithm.RunAlgorithm().locate(12), -1)



if __name__ == '__main__':
    unittest.main()