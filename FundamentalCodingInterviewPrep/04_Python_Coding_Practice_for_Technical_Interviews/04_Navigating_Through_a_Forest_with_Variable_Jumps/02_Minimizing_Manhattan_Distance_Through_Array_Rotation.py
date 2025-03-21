# Prepare to challenge your array manipulation skills! Consider two arrays, array1 and array2, each consisting of n non-negative integers. The values of n range from 1 to 500, inclusive. Each integer in the arrays is at most 10^3.

# Your task is to discover a rotation of array1 that minimizes the Manhattan distance with `array2`. The Manhattan distance between two arrays, `a` and `b`, of size `n`, is defined by:

#  D(a,b) =  i=1 ∑ n ∣a[i] −b[i]∣

# where a[i] and b[i] denote the `i`-th elements of arrays `a` and `b`, respectively, and `n` represents the size of the arrays.

# A rotation of an array refers to taking one or more elements from the end and moving these elements to the beginning, maintaining their original order in the process.

# You need to return the smallest possible Manhattan distance obtained through this operation.

# Let's say that you find multiple rotations of array1 that yield the same smallest Manhattan distance with array2. In this case, you should return the rotated array that, when converted into an integer number by concatenating all of its digits (from left to right), would be the smallest.

# Consider the array as periodic; that is, after the last element, the first one follows.

# Keep in mind that the size of the two arrays is always the same, and the arrays are not necessarily sorted at the beginning.

# If array1 is exactly the same as array2 from the beginning, output the original array1 and the Manhattan distance 
# 0
# 0.

# Remember, the ultimate goal is to minimize the Manhattan distance between array1 and array2 through the least alterations possible to array1. Let's see how small you can get!

def largest_step(garden, start, direction):
  # TODO: implement the function
  pass

# Solving the 02_Minimizing_Manhattan_Distance_Through_Array_Rotation problem.

def solution(array1, array2):
  # TODO: Your implementation goes here
  iteration = 0
  
  if array1 == array2:
    return (array1, 0)
  
  current_array1 = array1[::1]
  min_distance = float('inf')
  min_rotation_number = int(''.join([str(n) for n in array1]))
  min_rotation = array1[::1]
  
  while iteration <= len(array1):
    manhattan_distance = 0
    pos = 0
    
    while pos < len(array1):
      manhattan_distance += abs(current_array1[pos] - array2[pos])
      pos += 1
    
    if current_array1 == array2:
      return (current_array1, 0)
    
    # compare min
    manhattan_distance_number = int(''.join([str(n) for n in current_array1]))
    # print(f"{manhattan_distance} <= {min_distance}")
    # print(f"min_rotation_number: {min_rotation_number}, manh number: { manhattan_distance_number}")
    if manhattan_distance < min_distance:
      min_distance = manhattan_distance
      min_rotation_number = manhattan_distance_number
      min_rotation = current_array1[::1]
    elif manhattan_distance == min_distance:
      if min_rotation_number > manhattan_distance_number:
        min_distance = manhattan_distance
        min_rotation_number = manhattan_distance_number
        min_rotation = current_array1[::1]
        
    iteration += 1
    current_array1 = current_array1[1::1] + [current_array1[0]]
  print(f"Itetation {min_rotation}, min distance {min_distance}")
  return (min_rotation, min_distance)
  pass

from collections import deque

def simpler_solution(array1, array2):
  if array1 == array2:
    return (array1, 0)
  
  n = len(array1)
  min_distance = float('inf')
  min_rotation = array1[:]
  
  for i in range(n):
    rotated_array = array1[i:] + array1[:i]
    manhattan_distance = sum(abs(a - b) for a, b in zip(rotated_array, array2))
      
    if manhattan_distance < min_distance or (manhattan_distance == min_distance and rotated_array < min_rotation):
      min_distance = manhattan_distance
      min_rotation = rotated_array
  
  return (min_rotation, min_distance)

print(simpler_solution([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]))
# Sol ([3, 4, 5, 1, 2], 6)