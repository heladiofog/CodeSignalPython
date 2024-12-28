# You are given an input array consisting of n integers ranging from 0 to 100, inclusive, where n represents the length of the array. Your task is to return a new array of tuples. Each tuple should consist of an element from the input array paired with its geometrical mean with the 'opposite' element. The 'opposite' element of any element in the array is defined as the element at the corresponding position from the end of the array.

# Assume that the geometrical mean of two numbers, a and b, is calculated as: 
# `sqrt(a×b)`, where `sqrt` stands for square root.

# A few notes:

# - If the length of the array, n, is odd, the middle element is considered to be its own 'opposite'.
# - The elements of the input array will be in the range from 0 to 100, inclusive.
# - Calculate the geometrical mean to two decimal places. For example, the geometrical mean of 2 and 8 is 4.00 (since `sqrt(2×8)=4`).
# - Round down to two decimal places. For instance, the geometrical mean of 2 and 8 is 4.00, not 4.472.
# - For example, for `numbers = [1, 2, 3, 4, 5]`, the output should be `solution(numbers) = [(1, 2.24), (2, 2.83), (3, 3.0), (4, 2.83), (5, 2.24)]`.


def solution(numbers):
  # TODO: implement this function
  pass

# Solution:
from math import sqrt

# def solution(numbers):
#     # TODO: implement this function
#     oposite_mean_pairs = []
#     n = len(numbers)
#     for i in range(n):
#         # next step comes here
#         print(numbers[i], numbers[n - i - 1])
#         oposite_mean_pairs.append((numbers[i], geometrical_mean(numbers[i], numbers[n - i - 1])))
#     print(oposite_mean_pairs)
#     return oposite_mean_pairs
#     pass

# def geometrical_mean(a, b):
#     return round(sqrt(a * b), 2)

