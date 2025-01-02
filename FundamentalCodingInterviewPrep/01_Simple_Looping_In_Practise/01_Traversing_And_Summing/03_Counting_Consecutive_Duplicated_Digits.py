# You are tasked with writing a function that takes a positive integer, n, as an input and returns the number of consecutive equal digits in the number. Specifically, your function should identify pairs of digits in n that are equal and consecutive and return the count of these pairs.

# For instance, if n = 113224, it contains two groups of consecutive equal digits: 11 and 22. Therefore, the output should be 2. For n = 444, the output should also be 2, as there are two groups of 44 in this number.

# Keep in mind that n will be a positive integer ranging from 
# 1 to 10^8, inclusive.

# Note: You are not permitted to convert the number into a string or any other iterable structure for this task. You should work directly with the number.

def solution(n):
  # TODO: implement
  pass
# Solution:
def solution(n):
    # TODO: implement
    original_n = n
    consecutive_count = 0
    while n > 0:
        last_digit = n % 10
        n //= 10
        prev_last_digit = n % 10
        if last_digit == prev_last_digit:
            consecutive_count += 1
    print(f"for {original_n} there are {consecutive_count} consecutive equal digits")
    return consecutive_count
    pass