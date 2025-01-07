# You are provided with an array of `n` integers, where `n` can range from `1` to `200`, inclusive. Your task is to create a new array that takes two pairs of 'opposite' elements from the original array at each iteration, starting from the center and moving towards both ends, to calculate the resulting multiplication of each pair.

# By 'opposite' elements, we mean pairs of elements symmetrically located relative to the array's center. If the array's length is odd, the center element doesn't have an opposite and should be included in the result array as is.

# Each element in the array can range from `-100` to `100`, inclusive.

# For example, if the input array is `[1, 2, 3, 4, 5]`, the returned array should be `[3, 8, 5]`. This is because the center element `3` remains as it is, the multiplication of `2` and `4` is `8`, and the multiplication of `1 and `5` is `5`.

def solution(numbers):
  # TODO: Implement the solution here
  pass

# Solution:
def solution(numbers):
  # TODO: Implement the solution here
  mid_position = len(numbers) // 2
    # initialization
  if len(numbers) % 2 == 1:   # odd array starts with a product
    # first element is the number in the middle position
    product_array = [numbers[mid_position]]
    left = mid_position - 1
    right = mid_position + 1
  else:
    # first element remains empty at first
    product_array = []
    left = mid_position - 1
    right = mid_position
  
  while left >= 0 and right < len(numbers):
    product_array.append(numbers[left] * numbers[right])
    left -= 1
    right += 1
      
  print(f"Result product array: {product_array}")
  return product_array
  pass