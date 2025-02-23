def sum(num1, num2):
  i, j, carry, res = len(num1) - 1, len(num2) - 1, 0, []
  
  while i >= 0 or j >= 0 or carry > 0:
    n1 = int(num1[i]) if i >= 0 else 0
    n2 = int(num2[j]) if j >= 0 else 0
    total = n1 + n2 + carry
    if total > 9:
      carry = 1
    else:
      carry = 0
    curr = total%10
    res.append(str(curr))
    i, j = i - 1, j - 1

  return ''.join(res[::-1])  # reverse the list and join into a single string

print(sum("", "12"))
print(sum("9", "9"))