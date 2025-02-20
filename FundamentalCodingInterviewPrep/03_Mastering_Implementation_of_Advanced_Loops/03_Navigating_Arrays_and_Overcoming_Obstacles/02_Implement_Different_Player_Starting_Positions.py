# You are the developer of a unique board game and you need to calculate how many moves a player has to make, assuming different starting positions.

# The game is played on a linear board represented by an array of positive integers. The length of the board can range from 
# 1 to 500 inclusive. Each position on the board represents the number of steps a player can make from that position. The player can only move towards the end of the board. The board can contain obstacles on which the player cannot land, defined by a specific integer value. The game ends when the player exits the board or lands on an obstacle.

# Your task is to implement the `solution(board, obstacle)` function, which returns an array moves. For every `i` in moves, the algorithm should calculate the number of moves required for a player to exit the board, while starting from the i-th position, without landing on an obstacle. If the player encounters an obstacle, `moves[i]` should be set to -1.

# The value of obstacle as well as each value in the board array ranges from 
# 1 to 10 inclusive.

# For example, `solution([5, 3, 2, 6, 2, 1, 7], 3)` should `return [3, -1, 3, 1, 2, 2, 1]`. The moves array is calculated as follows:

# moves[0] should be 3 because:

# - The player starts on board[0] = 5
# - The player then moves 5 places on to board[5] = 1
# - Then the player moves 1 place to board[6] = 7
# - And, finally, the player moves to exit the board, making it a total of 3 moves

# moves[1] should be -1 because:

# - The player starts on the board[1] = 3 which is equal to obstacle
# And so on...

def solution(board, obstacle):
  # TODO: implement function
  pass

# Solving the Implement Different Payer Starting Point Positions in a Boardgame problem.
def solution(board, obstacle):
  # TODO: implement function
  solution_moves = []
    
  for starting_position in range(len(board)):
    position = starting_position
    moves = 0
    there_was_obstacle = False
    
    while position < len(board):
      if board[position] == obstacle:
        solution_moves.append(-1)
        there_was_obstacle = True
        break
      moves += 1
      position += board[position]
    
    if not there_was_obstacle:
        solution_moves.append(moves)
    
  print(f"Solution moves: {solution_moves}")
  return solution_moves
  pass