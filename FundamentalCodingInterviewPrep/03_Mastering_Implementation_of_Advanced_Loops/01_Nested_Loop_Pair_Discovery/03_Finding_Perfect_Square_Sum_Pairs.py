# You will be given two arrays of integers. The first array has n elements, and the second array has k elements. Sizes n and k both range from 1 to 100, inclusive. The elements of both arrays can fall within a range of -100 to 100, inclusive.

# Your task is to write a Python function that will locate and return an array of all pairs of integers with the property that the first element of each pair comes from the first array and the second element of each pair comes from the second array, such that the sum of the two elements of the pair is a perfect square. A perfect square, as you know, is an integer that is the square of another integer.

# The order of pairs in your output should correspond to the order of the elements in the input arrays. For example, if the two arrays are [2, 3, 16] and [1, 9, 10], the function should return [(3, 1), (16, 9)] because 3+1=4 (which is the square of 2) and 16+9=25 (which is the square of 5).

# If no such pairs exist, or if either input array is empty, your function should return an empty list.

def solution(arr1, arr2):
  # TODO: Implement this function
  pass

# Solution:
def solution(arr1, arr2):
  # TODO: Implement this function
  resulting_pairs = []
  
  for n in arr1:
    for k in arr2:
      if n + k >= 0:  # to avoid complex numbers
        sum_square_root = (n + k) ** (1 / 2)
        # print(f"{sum_square_root} is square root of {n + k}")
        if sum_square_root.is_integer():
          resulting_pairs.append((n, k))

  print(f"Resulting pairs {resulting_pairs}")
  return resulting_pairs
  pass