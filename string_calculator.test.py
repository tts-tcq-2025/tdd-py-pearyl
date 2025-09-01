from string_calculator import sum

def test_input(input):
  if input == "":
    assert sum(input) == 0

if __name__ == '__main__':
  test_input("")
