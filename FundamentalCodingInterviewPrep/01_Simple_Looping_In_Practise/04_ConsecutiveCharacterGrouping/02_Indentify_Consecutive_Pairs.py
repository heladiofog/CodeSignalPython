# In this task, you need to write a Python function that finds repeating two-character patterns in a string. The function should identify when the same pair of characters appear next to each other in the string and count how many times each pair repeats consecutively.

# The function should return a new string that lists each pair followed by the number of times it repeats consecutively. For example, let's break down the input string "aaabbabbababacab":

# Divide the string into pairs:

# "aa"
# "ab"
# "ba"
# "bb"
# "ab"
# "ab"
# "ac"
# "ab"
# Note the consecutive pairs:

# "ab" appears twice consecutively in the middle.
# Therefore, the output string will be: "aa1ab1ba1bb1ab2ac1ab1".


def solution(s):
  # TODO: Implement the function here
  pass

def solution(s):
  # TODO: Implement the function here
  consecutive_pairs_count_string = ''
  s_length = len(s)
  current_pair_position = 0
  next_pair_position = 2
  current_consecutive_count = 1
  # base case: length is 2
  current_pair = s[0] + s[1]
  
  while next_pair_position + 1 < s_length:
    next_pair = s[next_pair_position] + s[next_pair_position + 1]
    # there is a consecutive pair
    if current_pair == next_pair:
      current_consecutive_count += 1
      next_pair_position += 2
        
    else:
      # add current pair and its count
      consecutive_pairs_count_string += current_pair + str(current_consecutive_count)
      # restart count and update positions
      current_pair_position = next_pair_position
      next_pair_position += 2
      current_consecutive_count = 1
      current_pair = next_pair # s[current_pair_position] + s[current_pair_position + 1]

  # chech if currenr pair position is < len(s)
  if current_pair_position < s_length:
    consecutive_pairs_count_string += current_pair + str(current_consecutive_count)
      
  print(f"Resulting pairs count string: {consecutive_pairs_count_string}")
  return consecutive_pairs_count_string
  pass
