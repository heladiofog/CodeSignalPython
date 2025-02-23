# You are tasked with writing a Python function to multiply two extremely large positive integers. These are not your regular-sized large numbers; they are represented as strings potentially up to 500 digits long.

# Your function should take two string parameters, representing the two large integers to be multiplied, and return the product as a string. The challenging part is that you should perform the multiplication without converting the entire strings into integers.

# Keep in mind that the elements of the string are digits in the range from 0 to 9, inclusive.

# Furthermore, bear in mind that when multiplying numbers manually, we align the numbers vertically and multiply each digit of the first number with each digit of the second number, starting from the rightmost digits, and add the results after shifting appropriately.

# Please solve this problem using similar, decision-based string manipulations instead of merely converting strings into integers, multiplying them, and converting the result back to a string. This approach is imperative as direct multiplication would not be feasible for very large numbers.

# Challenge yourself, and Happy Coding!

def solution(num1, num2):
  # TODO: Implement Function
  pass

# Solving Multiplying Extremely Large Numbers Represented as Strings problem.
def solution(num1, num2):
  # TODO: Implement Function
  i, length_num2, res = len(num1) - 1, len(num2) - 1, ''
  shifts = []
  
  while i >= 0:
    sub_total = [] + shifts   # shift for each position
    n1 = int(num1[i])
    carry = 0
    j = length_num2

    while j >= 0 or carry > 0:
      n2 = int(num2[j]) if j >= 0 else 0
      ij_mult = n1 * n2 + carry
      # carry is different from sum's carry
      carry = ij_mult // 10
      current_digit = ij_mult % 10
      sub_total.append(str(current_digit))
      j -= 1
      # remove trailing 0
      pos = len(sub_total) - 1
      while pos > 0 and sub_total[pos] == '0':
        sub_total.pop()
        pos -= 1
      # finally subtotal result
      sub_total = ''.join(sub_total[::-1])
      res = sum_large_numbers(res, sub_total)
      shifts.append('0')
      i -= 1
  
  print(f"Mult result: {res}")
  return res
  pass


def sum_large_numbers(num1, num2):
  i, j, carry, res = len(num1) - 1, len(num2) - 1, 0, []

  while i >= 0 or j >= 0 or carry > 0:
    n1 = int(num1[i]) if i >= 0 else 0
    n2 = int(num2[j]) if j >= 0 else 0
    total = n1 + n2 + carry
    if total > 9:
      carry = 1
    else:
      carry = 0
    curr = total % 10
    res.append(str(curr))
    i, j = i - 1, j - 1

  return ''.join(res[::-1])  # reverse the list and join into a single string
  pass