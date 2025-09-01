from string_calculator import sum

def test_empty_string_returns_zero():
  assert sum("") == 0

def test_addition():
  assert sum(1,2,3,4,5) == 15


