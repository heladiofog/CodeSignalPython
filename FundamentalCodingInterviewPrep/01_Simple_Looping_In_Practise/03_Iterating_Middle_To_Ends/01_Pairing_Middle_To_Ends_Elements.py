# You are given an array of `n` integers, where `n` can range from `1` to `500`, inclusive. Your task is to create a new array in which each element is a tuple, determined by pairing elements from the middle to both ends of the original array.

# If the original array has an odd length, pair the middle element with `0`. If the original array has an even length, start pairing from the two middle elements. Continue the pairing by alternating elements from the left and the right until all elements have been paired.

# After creating the paired elements, return the new array of tuples. Ultimately, your result should be an array of tuples, each of size two. Each element within a tuple, as well as within the array, can range from `-1000` to `1000`, inclusive.

# For example, if the input is `numbers = [1, 2, 3, 4, 5]`, the output should be `[(3, 0), (2, 4), (1, 5)]`. Similarly, if the input is `numbers = [1, 2, 3, 4]`, the output should be `[(2, 3), (1, 4)]`.

def solution(numbers):
    # TODO: Implement the function to pair the elements from the middle to ends of the list
    pass

# Solution:
def solution(numbers):
  # TODO: Implement the function to pair the elements from the middle to ends of the list
  length = len(numbers)
  middle_position = length // 2
  # initialization
  if length % 2 == 1:
    tuples_array = [(numbers[middle_position], 0)]
    left_position = middle_position - 1
    right_position = middle_position + 1
  else:
    tuples_array = []
    left_position = middle_position - 1
    right_position = middle_position
      
  while left_position >= 0 and right_position < length:
    tuples_array.append((numbers[left_position], numbers[right_position]))
    left_position -= 1
    right_position += 1
      
  print(f"Tuples array is {tuples_array}")
  return tuples_array
  pass