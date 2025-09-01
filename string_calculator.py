import re

def split_numbers(input_string):
  if not input_string:
    return []
  delimiters = [',','\n']
  if input_string.startswith("//"):
    parts = input_string.split("\n", 1)
    custom_delim, input_string = parts[0], parts[1]
    delimiters.append(custom_delim)
  pattern = "|".join(map(re.escape, delimiters))
  print(pattern)
  return re.split(pattern, input_string)

def sum(input_string):
  numbers = split_numbers(input_string)
  total = sum(int(x) for x in numbers if x.strip())
  return total
