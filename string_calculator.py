import re

def split_numbers(input_string):
  if not input_string:
    return []
  return re.split(r'[,\n]', input_string)

def sum(input_string):
  numbers = split_numbers(input_string)
  total = sum(int(x) for x in numbers if x.strip())
  return total
