# You are required to create a function that, given two parameters — an array of integers and a string — will return a modified text message based on these elements.

# You will be provided with an array of n integers, where n is between 1 and 
# 100, inclusive, and a string with m characters, where m ranges from 1 to 
# 500, inclusive. Each element in the array will range from # −100 to 100, inclusive.

# Your initial task is to process the array by subtracting 3 from each number and then accumulating the absolute values of each number until their total exceeds 30. If the total exceeds 30, you must stop processing the array immediately.

# Concurrently, you must process the given string. In this part, replace each lowercase character in your string with the succeeding alphabetical character in a cyclic manner; for instance, 'a' should be replaced by 'b', 'b' should be replaced by 'c', and so on, until 'z', which should be replaced by 'a'. If a character is not a lowercase letter, it should be left as is.

# Similar to the array, if the total absolute value from the array operations crosses the threshold of 30, you should cease the string modification immediately.

# At the conclusion, return both an updated string with all processed characters and the remaining, unprocessed portion of the initial array, respectively.

# Can you create a function that accomplishes all this?

def solution(arr, text):
  # TODO: implement
  pass

# Solving the Processing Strings and Arrays with a Threshold Condition problem.

def solution(arr, text):
  # TODO: implement
  arr_accumulation = 0
  modified_text = ""
  i = 0
  
  while i < len(text) and i < len(arr):
    arr_accumulation += abs(arr[i] - 3)
    if arr_accumulation > 30:
      break
    if text[i].islower():
      modified_text += 'a' if text[i] == 'z' else chr(ord(text[i]) + 1)
    else:
      modified_text += text[i]
    i += 1
  
  print(f"Accumulated was {arr_accumulation}")
  print(f"Modified text: {modified_text}, remainder numbers {arr[i:]}")
  return modified_text, arr[i:]
  pass