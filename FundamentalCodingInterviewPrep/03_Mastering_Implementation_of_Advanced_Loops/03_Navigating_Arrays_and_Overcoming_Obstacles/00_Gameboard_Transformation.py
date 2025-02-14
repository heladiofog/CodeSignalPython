# You are given an array of `n` integers, ranging from `1` to `100` inclusive. Each integer represents a player's progress on a linear gameboard, indicating how many steps they can move to the right. However, the course is fraught(tenso) with challenges; there exist several obstacles, represented by negative integers.

# Your task is to return a transformed array structuring the gameboard in a new way: if an integer can lead the player to an obstacle on its right (within the range of its value), replace the number with the index of the obstacle. If the number represents an obstacle (a negative integer), replace it with `-1`. If none of these conditions are met, retain the original integer.

# Keep in mind, this task is an innovative take on our previous analysis lesson, implementing a "**Move Until Obstacle**" game. Remember, your array will have no more than 500 elements, and the elements in the array range from -100 to 100, inclusive. Good luck with your coding journey!

# For instance, given an array `[3, 2, -3, 1, 2]`, the output would be `[2, 2, -1, 1, 2]`.

# Here's how it works:

# - Replace the first position with 2 because a player at the first position can move 3 steps but will hit the obstacle at the 2nd index.
# - Replace the second position with 2 because a player at the second position can move 2 steps but will hit the obstacle at the 2nd index.
# - Replace the negative number -3 at the third position with -1 because it represents an obstacle.
# - Keep the number 1 at the fourth position as there are no obstacles in its range.
# - Keep the number 2 at the fifth position as there are no further positions or obstacles to impact it.

def solution(numbers):
  # TODO: implement the function according to the task description
  pass

# Solving Gameboard Transformation:
def solution(numbers):
  # TODO: implement the function according to the task description
  transformed_gameboard = []
  position = 0
  moves_forward = 0
  
  while position < len(numbers):
    if numbers[position] < 0:   # it's an obstacle
      transformed_gameboard.append(-1)
      position += 1
      continue
    
    moves_forward = numbers[position]
    there_was_obstacle = False
    
    for increment in range(1, moves_forward + 1):
      checked_position = position + increment
      
      if checked_position < len(numbers) and numbers[checked_position] < 0:   # is an obstacle
        # save the position of the obstacle
        transformed_gameboard.append(checked_position)
        there_was_obstacle = True
        break   # stps checking
    
    if not there_was_obstacle:  # the number remains
      transformed_gameboard.append(numbers[position])
    
    position += 1
  
  print(f"Transformed gameboard {transformed_gameboard}")
  return transformed_gameboard
  pass