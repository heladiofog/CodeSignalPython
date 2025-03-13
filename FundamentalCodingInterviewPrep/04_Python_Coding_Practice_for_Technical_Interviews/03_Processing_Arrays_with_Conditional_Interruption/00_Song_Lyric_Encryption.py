# As an aspiring musician, you are given a chance to create a unique encrypted song. The song's lyrics will be encoded based on specific rules applied to an array of integers and a string.

# You are provided with an array of n integers, where n is between 
# 1
# 1 to 
# 500
# 500, inclusive. Each integer in the array ranges from 
# −
# 100
# −100 to 
# 100
# 100, inclusive. Accompanying this, you are presented with a string comprising n lowercase alphabetical characters.

# Here are your tasks:

# For the array, calculate the absolute value of each number and multiply it by 
# 2
# 2. Accumulate these results until the total exceeds 
# 100
# 100.

# For the string, your task is to replace each letter with the preceding alphabetical character and then concatenate these characters in the order they were processed. However, if the current character in the string is a vowel (i.e., 'a', 'e', 'i', 'o', 'u'), it should not be processed, and you should stop the process immediately.

# When the accumulated total exceeds 
# 100
# 100, or if the next character is a vowel, halt the process and return the transformed string and the remainder of the array in their original order.

# Your main challenge here is to process the given string and integer array according to the stated rules but stopping when a certain condition is met. The final output should be a tuple with the transformed string as the first element and the remaining, unprocessed part of the array as the second element.


def solution(strings, numbers):
  # TODO: implement the solution according to the task
  pass

# Solving the problem Song Lyrics Encryption and Number Processing Challenge.

def solution(strings, numbers):
  # TODO: implement the solution according to the task
  result_string = ''
  sum_so_far = 0
  i = 0
  
  while i < len(strings) and strings[i] not in ['a', 'e', 'i', 'o', 'u'] and sum_so_far <= 100:
    result_string += chr(ord(strings[i]) - 1)
    duplicated_number = abs(numbers[i] * 2)
    sum_so_far += duplicated_number
    i += 1
  
  print(f"Resulting string: {result_string}, remainder numbers {numbers[i:]}")
  return result_string, numbers[i:]
  pass