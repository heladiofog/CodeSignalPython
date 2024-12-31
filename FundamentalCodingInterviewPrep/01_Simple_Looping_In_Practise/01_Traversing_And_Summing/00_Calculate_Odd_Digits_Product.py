# # You are given an integer n where n ranges from 
# 1 to 10^8, inclusive. Your task is to write a function that calculates and returns the product of the odd digits of n, without converting n into a string.

# For example, if n equals 43172, the output should be 21, because the product of the odd digits 3, 1, and 7 is 21.

# Please note that if n has no odd digits, your function should return 0.

# You are expected to solve this task by using a while loop. Good luck!
def solution(n):
    odd_digits_product = 1  # start at 1 just in the case
    odd_digits_count = 0
    while n > 0:
        last_digit = n % 10
        if last_digit % 2 == 1:  # Check if the digit is odd
            odd_digits_product *= last_digit
            odd_digits_count += 1
        n = n // 10  # Remove the last digit
    # checkif there was at least one odd digit
    odd_digits_product = 0 if odd_digits_count == 0 else odd_digits_product
    
    print(f"Total odd digits product is {odd_digits_product}")
    return odd_digits_product