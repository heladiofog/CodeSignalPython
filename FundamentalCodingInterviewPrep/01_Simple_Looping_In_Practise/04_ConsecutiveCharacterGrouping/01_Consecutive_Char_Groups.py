# Your task is to write a Python function that takes in a string and identifies all the consecutive groups of identical characters within it, with the analysis starting from the end of the string rather than from its beginning. A group is defined as a segment of the text where the same character is repeated consecutively.

# Your function should return a list of tuples. Each tuple will consist of the repeating character and the number of its repetitions. For instance, if the input string is "aaabbcccdde", the function should output: [('e', 1), ('d', 2), ('c', 3), ('b', 2), ('a', 3)].

# Note that the input string cannot be empty; in other words, it must contain at least one character, and its length must not exceed 500 characters. The return should also be in reverse order, starting from the group of repeated characters at the end of the string and moving backward.

# Put your knowledge and skills into action to solve this reverse pattern identification puzzle!

def solution(s):
  # TODO: implement the algorithm to find consecutive groups of characters in the reverse order
  pass

# Solution:
def solution(s):
  # TODO: implement the algorithm to find consecutive groups of characters in the reverse order
  consecutive_groups = []
  current_group_char = None
  current_group_length = 0
  reversed_string = s[::-1]
  
  for char in reversed_string:
  #if char.isdigit() or char.isalpha():   # this problem is not only for aplhanumeric chars
      if char == current_group_char:
          current_group_length += 1
      else:
          if current_group_char is not None:
              consecutive_groups.append((current_group_char, current_group_length))
          current_group_char = char
          current_group_length = 1
  
  if current_group_char is not None:
      consecutive_groups.append((current_group_char, current_group_length))
  
  print(f"reversed consecutive groups for {s} are: {consecutive_groups}")
  return consecutive_groups
  pass