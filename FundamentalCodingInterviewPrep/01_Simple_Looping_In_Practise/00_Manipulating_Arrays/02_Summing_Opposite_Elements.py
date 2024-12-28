# You are given an array of `n` integers, where `n` ranges from `2` to `200`, inclusive. The elements in the array range from `-200` to `200`, inclusive. Your task is to return an array in which each element is the sum of a pair composed of an element and its 'opposite' element.

# By 'opposite', we mean that in an array of `n` elements, the first and last elements are paired, the second and second-to-last elements are paired, and so on. If the array is of odd length, the middle element pairs with itself.

# The function should handle both positive and negative integers and be capable of dealing with an odd number of elements in the list.

# For example, given an input array [1, 2, 3, 4, 5], your function should return [6, 6, 6]. This is because the first element 1 plus the last element 5 equals 6, the second element 2 plus the second-to-last element 4 equals 6, and the middle element 3 plus itself equals 6.

def solution(numbers):
  # TODO: Implement solution here
  pass

# Solution:
def solution(numbers):
  # Implement solution here:
  oposite_pair_sums = []
  numbers_length = len(numbers)
  n = numbers_length // 2 if numbers_length % 2 == 0 else (numbers_length + 1) // 2 
  print(n)
  for i in range(n):
    oposite_pair_sums.append(sum(numbers[i], numbers[numbers_length -i - 1]))
  
  print(oposite_pair_sums)
  return oposite_pair_sums
  pass

def sum(a, b):
  return a + b