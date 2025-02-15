# Your task is to design a 1-dimensional game where a player moves along a path determined by an array of integers.

# The path is an array of integers, each ranging from -100 to 100, inclusive. The size of the array n, i.e., the total number of steps on the path, can range from 1 to 500, inclusive. Each integer a_i in the array signifies how many steps the player can move and in which initial direction:

# A positive integer allows the player to move that many steps to the right.
# A negative integer directs the player to move that many steps to the left.
# Zero signifies a blockade that prevents further movement.
# The game proceeds along the following rules:

# The player starts at the first position of the array (0-indexed) and moves according to the value at the player's current position in the array.

# If the value in the current position is zero, then the game ends. If the player's current position leads them outside of the array's boundaries, then their ability to move in the current direction ceases.

# If the latter happens, then the player reverses their direction and continues to move according to similar rules, but now the directions are inverted: positive integers lead the player to the left, and negative integers point to the right.

# The game ends when the player encounters a blockade or the array boundaries for the second time and so can no longer move.

# You are to implement a function titled evaluatePath(numbers). This function should take an array of integers as input, representing the path and its rules, and return a tuple (position, moves), where:

# position: This is the player's final position (0-indexed) when the game ends.
# moves: This is the total number of moves made by the player until the game ends.
# It's guaranteed that the game will not lead to an infinite loop, i.e. the path to the next blockade or the array boundaries would not require the player to visit the same position more than once.

# For instance, given an array [3, 4, 1, 1, -3, 1]. The output would be (4, 5). Here's how it works:

# - The player starts at position 0, where the value is 3. They move 3 steps to the right and land on the 3rd position. Total moves till now: 1.

# - At position 3, the value is 1. They move 1 step to the right, landing on the 4th position. Total moves till now: 2.

# - At position 4, the value is -3. They move 3 steps to the left, landing back on position 1. Total moves meanwhile: 3.

# - At position 1, the value is 4. They move 4 steps to the right, landing on position 5. Total moves thus far: 4.

# - At position 5, the value is 1, which would lead them out of the array's right boundary. So, they reverse their direction.

# - After reversing direction at position 5, they move 1 step to the left and land on position 4. Total moves till now: 5.

# - Now, with the reversed direction, the player is at position 4 where the value is -3. In the reversed direction, -3 indicates 3 steps to the right. But this would again lead to the right boundary of the array. Since they have already reversed direction once, they cannot move further in any direction and the game ends.

# - At the end of the game, the player is at position 4 having made a total of 5 moves, thereby, the function returns (4, 5).

## Additional explanation:
# HAF> explain the sequence of steps for this case [2, 1, -3, 4]
# Cosmo> • 5:22 PM
# Cosmo> Read message out loud
# Let's break down the sequence of steps for the array [2, 1, -3, 4]:

# - Start at position 0: The value is 2, so the player moves 2 steps to the right, landing on position 2. Total moves: 1.

# - At position 2: The value is -3, which means the player should move 3 steps to the left. This would take the player to position -1, which is outside the array's left boundary. The player reverses direction.

# - Reverse direction at position 2: Now, the player moves 3 steps to the right (since the direction is reversed), landing on position 5, which is outside the array's right boundary. The player reverses direction again.

# - Second reversal: Since the player has already reversed direction once, they cannot move further in any direction, and the game ends.

# The final position is 2, and the total number of moves made is 1. The function returns (2, 1).


def evaluatePath(numbers):
  # TODO: implement the function
  pass

# Solving Design and Implement a 1D Board Game using Arrays problem:
def evaluatePath(numbers):
  # TODO: implement the function
  # if true, the direction is to the left
  boundary_was_reached_once = False
  moves_count = 0
  position = 0
  length = len(numbers)
  
  while numbers[position] != 0:
    current_value = numbers[position]
    # update position if possible
    if boundary_was_reached_once:   # positive direction to the left
      next_position = position - current_value
      # if next position is OFF the board (again) => end of game
      if next_position < 0 or next_position >= length:    # off the board
          break
      # if next position is ON the board
      position = next_position
    else:
      next_position = position + current_value
      # array boundary reached (only once allowed)
      if next_position < 0 or next_position >= length:    # off the board
        boundary_was_reached_once = True
        continue    # check towards the opposite direction on the same position
      # if next position is ON the board
      position = next_position
    # a valid move was performed
    moves_count += 1
  final_ouput = (position, moves_count)
  print(f"Final position: {final_ouput}")
  return final_ouput
  pass

