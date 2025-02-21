# Your mission is to write a Python function that compares these two "string-numbers" without converting the entire strings into integers. Your function should determine whether num1 is greater than, less than, or equal to num2.

# Your function can only use comparison operators (such as >, <, or ==) on strings. So “1” < “2” is allowed, but 1 < 2 is not. The task requires that you manually compare the two strings from the most significant digit to the least significant. You should implement your own logic to compare two string numbers.

# The function should return the following results:

# If num1 is greater than num2, your function should return 1.
# If num2 is greater than num1, your function should return -1.
# If num1 and num2 are equal, your function should return 0.
# Let's look at the following examples:

# Copy to clipboard
# For `num1` = '12345' and `num2` = '1234', your function should return `1`.
# For `num1` = '1234' and `num2` = '12345', your function should return `-1`.
# For `num1` = '12345' and `num2` = '12345', your function should return `0`.
# This exercise is a great test of your understanding of how numbers and strings work and interact in a programming language. We hope you find it challenging and enjoyable!

def solution(num1, num2):
  # TODO: implement the function
  pass

# Solving the problem of comparing large numbers represented as strings.
def solution(num1, num2):
  # TODO: implement the function
  num1_length, num2_length, result = len(num1), len(num2), 0

  if num1_length != num2_length:
    result = 1 if num1_length > num2_length else -1
  else:
    for position in range(num1_length):
      if num1[position] != num2[position]:
        result = 1 if num1[position] > num2[position] else -1
              
  print(f"Result: {result}")
  return result
  pass