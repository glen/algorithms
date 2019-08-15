from termcolor import colored

def class_name(underscore_name):
  return ''.join(x.capitalize() or '_' for x in underscore_name.split('_'))

def print_label(text, col_width, color):
  return colored(f"{text}:".ljust(col_width), color)

def print_value(text, color):
  return colored(f"{text}", color)