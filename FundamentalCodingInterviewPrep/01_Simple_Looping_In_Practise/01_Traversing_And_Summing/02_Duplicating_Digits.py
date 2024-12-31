# Your task is to implement a function that duplicates every digit in a given non-negative integer number, n. For example, if n equals 1234, the function should return 11223344.

# To prevent possible integer overflow, it is guaranteed that n will be a non-negative integer that does not exceed 10^4. Solve this task without converting n into a string or performing any other type of casting. Your job is to work strictly with integer operations.

# Keynote:
# Focus on the essence of the problem, which is processing each digit of the number independently while maintaining the digit order. There is no need to look for mathematical patterns or clever simplifications; plain and straightforward processing will suffice. Utilize the toolbox of basic programming skills: loops, conditions, and mathematical operations. Good luck!

def solution(n):
    # TODO: Implement the solution
    pass

def solution(n):
  # TODO: Implement the solution
  if n == 0: return 0
  duplicated_number = 0
  # TODO: Implement the solution
  # positions start at -1 to avoid another conditional
  relative_position = -1
  while n > 0:
    last_digit = n % 10 # get last digit to work with
    relative_position += 2  # update positin before calculation
    duplicated_number += (10 ** (relative_position) * last_digit) + (10 ** (relative_position - 1) * last_digit)
    n //= 10 # reducing n
    print(f"calculated number is {duplicated_number}, n is now {n}")
  return duplicated_number
  pass