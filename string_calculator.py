def parse_input(input_string):
  number_list = []
  if input_string == "":
    number_list.append(0)
  return number_list

def sum(input_string):
  integer_list = parse_input(input_string)
  sum = 0
  for int in integer_list:
    sum = sum + int
  return sum
