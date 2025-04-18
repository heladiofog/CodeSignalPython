# You are provided with a string of alphanumeric characters in which each number, regardless of the number of digits, is always followed by at least one alphabetic character before the next number appears. The task requires you to return a transformed version of the string wherein the first alphabetic character following each number is moved to a new position within the string and characters in between are removed.

# Specifically, for each number in the original string, identify the next letter that follows it, and then reposition that character to directly precede the number. All spaces and punctuation marks between the number and the letter are removed.

# The length of the string s ranges from 3 to 
# 1
# 0
# 6
# 10 
# 6
#   (inclusive), and the string contains at least one number. The numbers in the string are all integers and are non-negative.

# Here is an example for better understanding:

# Given the string:

# "I have 2 apples and 5! oranges and 3 grapefruits."

# The function should return:

# "I have a2pples and o5ranges and g3rapefruits."

# In this instance, the character 'a' following the number 2 is moved to come before the 2, the 'o' succeeding the 5 is placed before the 5, and the 'g' subsequent to the 3 is repositioned to precede the 3. Punctuation marks and spaces in between are removed.

# Please note that the operation should maintain the sequential order of the numbers and the rest of the text. Considering this, the task is not solely about dividing a string into substrings but also about modifying them. This will test your expertise in Python string operations and type conversions.

def solution(input_string):
  # TODO: implement your solution here
  pass

# Solution:
def solution(input_string):
  # TODO: implement your solution here
  #word[0]
  #number
  #word[1::]
  shifted_string = ""
  current_number = ""
  word_to_be_mixed = ""
  words = input_string.split()
  
  for word in words:
    if word.isdigit():
      current_number = word
    elif current_number:    # there is a number
      # append to the shifted string
      word_to_be_mixed = word
      shifted_string += word[0] + current_number + word[1::] + " "
      current_number = ""
    else: # just append next word
      shifted_string += word + " "
  
  if current_number:
    shifted_string += word_to_be_mixed[0] + current_number + word_to_be_mixed[1::]
  
  print(f"Resulting shifted string {shifted_string.strip()}")
  return shifted_string.strip()
  pass