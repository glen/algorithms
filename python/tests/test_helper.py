import sys
sys.path.append('../')
from python.lib import helper
from termcolor import colored
import unittest

class TestHelper(unittest.TestCase):
  def test_class_name(self):
    self.assertEqual(helper.class_name('hello_world'), 'HelloWorld')

  def test_print_label(self):
    self.assertEqual(helper.print_label('Hello', 10, 'red'), colored('Hello:'.ljust(10), 'red'))

  def test_print_value(self):
    self.assertEqual(helper.print_value('Yes', 'blue'), colored('Yes', 'blue'))

if __name__ == '__main__':
  unittest.main()
