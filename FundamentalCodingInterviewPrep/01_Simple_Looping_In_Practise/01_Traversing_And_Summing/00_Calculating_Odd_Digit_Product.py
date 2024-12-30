# You are given an integer n where n ranges from `1 to 10^8``, inclusive. Your task is to write a function that calculates and returns the product of the odd digits of `n`, without converting `n` into a string.

# For example, if `n` equals `43172`, the output should be `21`, because the product of the odd digits `3`, `1`, and `7` is `21`.

# Please note that if `n` has no odd digits, your function should return `0`.

# You are expected to solve this task by using a while loop. Good luck!

def solution(n):
    # TODO: implement
    pass

# # Solution:
# def solution(n):
#     # TODO: implement
#     odd_digits_product = 1
#     odd_digits_count = 0
    
#     while n > 0:
#         last_digit = n % 10
#         if last_digit % 2 == 1:  # Check if the digit is odd
#             odd_digits_product *= last_digit
#             odd_digits_count += 1
#         print(f"n is {n} the product do far ({odd_digits_count}) is {odd_digits_product}")
#         n = n // 10  # Remove the last digit
#     return odd_digits_product if odd_digits_count > 0 else 0
#     pass