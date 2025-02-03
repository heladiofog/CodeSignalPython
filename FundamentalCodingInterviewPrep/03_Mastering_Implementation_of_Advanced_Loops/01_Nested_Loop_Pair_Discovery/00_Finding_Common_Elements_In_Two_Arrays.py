# You are provided with two arrays of unique integers, with the lengths of arrays ranging from `1` to `100`, inclusive. The task requires you to identify elements that appear in both arrays and return them in an array, maintaining the order from the first provided array.

# Each array's element ranges from `-100` to `100`, inclusive.

# In your function `common_elements(listA, listB)`, `listA` and `listB` represent the two input arrays. The function should return an array that includes the common elements found in both `listA` and `listB`, while preserving the order of elements as they appear in `listA`.

# For example, if `listA = [7, 2, 3, 9, 1]` and `listB = [2, 3, 7, 6]`, the output should be `[7, 2, 3]`.

def common_elements(listA, listB):
  # TODO: Implement the function to find the common elements in the two arrays
  pass

# Solution:
def common_elements(listA, listB):
  # TODO: Implement the function to find the common elements in the two arrays
  common_numbers = []
    
  for numberA in listA:
    for numberB in listB:
      if numberA == numberB:
        common_numbers.append(numberA)
        listB.remove(numberB) # not necessary
        break
          
  print(f"Common numbers are {common_numbers}")
  return common_numbers
  pass