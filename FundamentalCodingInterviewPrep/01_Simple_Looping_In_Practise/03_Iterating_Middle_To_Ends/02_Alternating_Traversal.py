#You are provided with an array of n integers, where n ranges from `1` to `501` and is always an odd number. The elements of the array span values from `−10^6` to `10^6`, inclusive. The goal is to return a new array constructed by traversing the initial array in a specific order, outlined as follows:

# - Begin with the middle element of the array.
# - For each subsequent pair of elements, alternate between taking two elements from the left and two elements from the right, relative to the middle.
# - If fewer than two elements remain on either side, include all the remaining elements from that side.
# - Continue this process until all elements of the array have been traversed.

# For example, for `array = [1, 2, 3, 4, 5, 6, 7]`, your function should return `[4, 2, 3, 5, 6, 1, 7]`. And for array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], your function should return [6, 4, 5, 7, 8, 2, 3, 9, 10, 1, 11].

def unusual_traversal(array):
    # TODO: implement this function
    pass

# Solution:
def unusual_traversal(array):
  # TODO: implement this function
  length = len(array)
  mid_position = length // 2
  traversal_array = [array[mid_position]]
  
  ## Base cases
  if length == 1:
    return traversal_array
  
  left_position = mid_position -1
  right_position = mid_position + 1 
  
  while left_position - 1 >= 0 and right_position + 1 < length:
    # traversal_array.extend(array[left_position - 1: left_position + 1])
    traversal_array.append(array[left_position - 1])
    traversal_array.append(array[left_position])
    # traversal_array.extend(array[right_position: right_position + 2])
    traversal_array.append(array[right_position])
    traversal_array.append(array[right_position + 1])
      
    # if left_position - 2 == 0 and right_position + 2 == length:
    left_position -= 2
    right_position += 2
  
  if (length - 1) % 4 == 2:
    traversal_array.append(array[0])
    traversal_array.append(array[length - 1])
  
  print(f"Travelsal array {traversal_array}, left is {left_position}, right is {right_position}")
  return traversal_array
  pass