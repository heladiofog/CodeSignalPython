
# You are given two exceedingly large positive decimal numbers, `num1` and `num2`, both represented as strings. The length of these strings can range anywhere from 1 to 500 characters. The challenge here is to subtract `num2` from `num1 without directly converting the strings into integers.

# Create a Python function that performs this operation and returns the resultant string, referred to as `num3`.

# Please note that the subtraction will not result in a negative number, as `num1 will always be greater than or equal to `num2`.

def solution(num1, num2):
  # TODO: Implement the solution
  pass

# Solving Subtracting Large Numbers Represented as Strings problem.
def solution(num1, num2):
  # TODO: Implement the solution
  i, j, carryless, res = len(num1) - 1, len(num2) - 1, 0, []
  
  while i >= 0:
    n1 = int(num1[i]) if i >= 0 else 0
    n2 = int(num2[j]) if j >= 0 else 0
    
    if n1 >= n2 + carryless:
      total = n1 - n2 - carryless
      carryless = 0
    else:
      total = 10 + n1 - n2 - carryless
      carryless = 1
    
    res.append(str(total))
    i, j = i - 1, j - 1
  
  # remove trailing 0
  pos = len(res) - 1
  while pos > 0 and res[pos] == '0':
    res.pop()
    pos -= 1

  return ''.join(res[::-1])  # reverse the list and join into a single string
  pass