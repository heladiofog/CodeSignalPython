# Gloria the bunny finds herself once again amidst an array game. This time, however, the game has slightly intensified with a third array coming into play. Your task is to develop a Python function to maneuver Gloria through her quest, yielding the summation of the maximum values she encounters from arrayB and arrayC together.

# Gloria's movement pattern oscillates between the arrays in the following order: arrayA -> arrayB -> arrayA -> arrayC -> arrayA -> arrayB -> arrayA -> arrayC, and so on.

# The rule to decide Gloria's move is: She uses the current element's value in the array as an index for her next array. For example, if Gloria is at arrayA[1]=2, she would move to arrayB[2].

# The pattern repeats itself until one of the following occurs:

# Gloria's path repeats by visiting a position in arrayB or arrayC that was already visited, indicating that she is stuck in a loop and cannot progress further, OR
# Gloria tries to access an index that exceeds the length of an array (for example, attempting to access arrayA[4] when arrayA only contains 4 items indexed from 0 to 3), in which case Gloria's journey should also stop.
# Your task is to calculate the sum of the maximum values that Gloria encounters in arrayB and arrayC during her journey.

# Each input array consists of n items, where n ranges from 
# 1
# 1 to 
# 100
# 100, inclusive. Every item in the arrays is a non-negative integer and falls within the range of 
# 0
# 0 to 
# 99
# 99, inclusive.

# EXAMPLE

# Consider arrayA = [2, 1, 3, 0], arrayB = [1, 3, 2, 4], and arrayC = [4, 2, 5, 1]. Gloria's journey would look like:

# She begins at arrayA[0] = 2 which leads her to arrayB[2] = 2.
# She then goes back to arrayA[2] = 3, and then to arrayC[3] = 1.
# She returns to arrayA[1] = 1, then makes a hop to arrayB[1] = 3.
# She goes back to arrayA[3] = 0 and then proceeds to arrayC[0] = 4.
# Now Gloria would go to arrayA[4], however, since arrayA[4] doesn't exist because arrayA only contains 4 elements indexed from 0 to 3, Gloria's journey stops here.
# During her journey, Gloria encounters the maximum value 3 in arrayB and 4 in arrayC. The function should return 7, the sum of these two maximum values.
def solution(roadA, roadB):
  # TODO: implement the function according to the description above
  pass

# Solving Alice Jumping Game Adventure problem.

def solution(roadA, roadB):
  # TODO: implement the function according to the description above
  roads_distances = []
  
  for n in range(len(roadA)):
    indexA = n
    indexB = None
    temp_roadA = roadA[:]
    temp_roadB = roadB[:]
    in_roadA = True
    current_road_length = 0
    next_value = None
    
    while True:
      if in_roadA:
        indexB = temp_roadA[indexA]
        temp_roadA[indexA] = -1  # mark as visited
        next_value = temp_roadB[indexB] # next position's value
      else:
        indexA = temp_roadB[indexB]
        temp_roadB[indexB] = -1  # mark as visited
        next_value = temp_roadA[indexA] # next position's value
          
      current_road_length += 1
      if next_value == -1:  # visited, end of the road
        break
          
      in_roadA = not in_roadA
    
    roads_distances.append(current_road_length)
  print(f"Roads distances: {roads_distances}")
  return roads_distances
  pass