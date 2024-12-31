def solution(n):
  # TODO: implement the solution here
  reversed_digits = []  # start with an empty array
  positions_count = 0
  reversed_number = 0
  #print(n)
  
  # get the digits and count positions
  while n > 0:
    last_digit = n % 10
    reversed_digits.append(last_digit)
    n = n // 10  # Remove the last digit
    positions_count += 1 # count positions(this might be obtained with len() function call)
  print(reversed_digits, positions_count)
  
  # Calculate reversed number
  while positions_count > 0:
    first_reversed_digit = reversed_digits.pop(0)
    reversed_number += 10 ** (positions_count - 1) * first_reversed_digit
    positions_count -= 1
  
  print(f"Reversed number is {reversed_number}")
  return reversed_number
  pass
# Sample inpout/output
#12345
# [5, 4, 3, 2, 1] 5
# Reversed number is 0
# 23456789
# [9, 8, 7, 6, 5, 4, 3, 2] 8
# Reversed number is 0