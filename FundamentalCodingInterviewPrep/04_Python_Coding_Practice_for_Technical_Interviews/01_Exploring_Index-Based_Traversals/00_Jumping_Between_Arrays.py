# You're assisting in the creation of an algorithm for a novel game where a character hops between two arrays following certain rules. The game starts at the first index (1-based) of an array, arrayA.

# The value at the character's current position in arrayA determines the index it jumps to on the second array, arrayB. Upon landing on arrayB, it does the same thing: the value at the current position specifies the index it jumps to in arrayA. This iteration continues until the character lands on an index in arrayA that it has already visited, at which point the game concludes.

# Your task is to develop a Python function simulating this gameplay. The function receives two equal-length arrays of integers, arrayA and arrayB, each containing n elements (1 ≤ n ≤ 100). It should return an array consisting of the 1-based indices on arrayB that the character visited before a position on arrayA was repeated.

# Each element in the input arrays ranges from 1 to n, indicating the next 1-based index that the character will jump to in the other array. The function guarantees that each jump always results in a valid position within the same-length arrays, and a position in arrayA will inevitably be revisited.

# Can you devise a function that proficiently simulates this gameplay?

# Example

# For arrayA = [1, 3, 2, 5, 4] and arrayB = [5, 4, 3, 2, 1] the output should be [1, 4, 3, 2, 5] since it first lands at the first position in arrayB (the resulting array is [1]), then goes to the fifth position in arrayA, then returns to the fourth position in arrayB (the resulting array becomes [1, 4]), etc.

def solution(arrayA, arrayB):
  # TODO: Implement the function
  pass

# 'Course5-CodingInterview-Python_Coding_Practice_for_Technical_Interviews-Lesson01-ArrayHoppingAdventure:ExploringIndex-BasedTraversals-01-Solving Array Hopping Adventure: Exploring Index-Based Traversals problem.'

def solution(arrayA, arrayB):
  # TODO: Implement the function
  indexA = 1
  indexB = None
  in_arrayA = True
  output = []
  
  while True:
    if in_arrayA:
      if arrayA[indexA - 1] == 0:  # visited
        return output
      indexB = arrayA[indexA - 1]
      arrayA[indexA - 1] = 0  # visited
    else:
      output.append(indexB)
      indexA = arrayB[indexB - 1]
    
    in_arrayA = not in_arrayA
  pass