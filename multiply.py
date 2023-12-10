"""
Creating a test code to print sum of 2 integer inputs
"""
def multiply(a, b):
  return (a * b)

def test_multiply():
  result = multiply(3,5)
  assert result == 15
