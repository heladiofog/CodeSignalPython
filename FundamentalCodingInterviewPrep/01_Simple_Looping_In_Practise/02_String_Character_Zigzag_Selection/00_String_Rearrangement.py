# In this task, you are given a string composed of lowercase English alphabet letters ('a' to 'z'). The length of the string will range from 1 to 100 characters. Your challenge is to create a new string resulting from a unique order of character selection from the original string.

# You need to develop a Python function, `special_order(inputString)`, which takes `inputString` as an argument. The resulting string begins with the last character of the `inputString`, then selects the second-to-last character, continuing in reverse order until you reach the middle character of the string. Then, start with the first character of the inputString, proceed to the second character, and continue in this manner until you reach the middle character.

# For example, if the inputString is "abcdefg", the function should return "gfedabc".

# Keep in mind the following constraints while creating your function:

# The input string contains only lowercase English letters ('a' to 'z').
# The length of the input string is between 1 and 100, inclusive

def special_order(inputString):
  # TODO: Implement function
  pass

# Solution:
def special_order(inputString):
  # TODO: Implement function
  first_half = ''
  second_half = ''
  length = len(inputString)
  special_arranged_string = ''
  
  for i in range(length // 2):
    first_half += inputString[length - 1 - i]
    second_half += inputString[i]
      
  special_arranged_string = first_half + second_half if length % 2 == 0 else first_half + inputString[length//2] + second_half
  print(f"Special arranged string: {special_arranged_string}, its length is {length}.")
  return special_arranged_string
  
  pass