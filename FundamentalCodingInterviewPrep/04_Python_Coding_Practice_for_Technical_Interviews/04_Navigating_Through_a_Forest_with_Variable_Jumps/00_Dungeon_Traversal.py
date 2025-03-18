# You are given an array of `n` integer values, with `n` ranging from `1` to `500`, inclusive. The array represents a path through a virtual dungeon, with certain positions marked as traps.

# Each element in the array ranges from −10 ^10 to 10 ^10, inclusive, and represents the trap power. A value of `0` signifies a safe position, whereas positive integers indicate trap power — the higher the value, the harder it is to avoid and, hence, the more dangerous it is. Negative integers are traps that are easier to avoid, with negative values implying that the trap could potentially aid you rather than hinder.

# Your task is to move from the start position to the end position. For each step, you can move by `x` elements in the right direction only, where `x` ranges from `1` to `n`. Each time you step on a trap, you lose health points equal to the trap's power. You originally have `h` health points, where `h` is a positive integer ranging from `1` to 10^ 100.

# Find the `x` that you must choose such that you lose the least amount of `health` points upon reaching the end of the array. Also, determine if there is no possible `x` that allows you to reach the end of the array with any remaining health points. In the latter case, return `-1` to indicate that it's impossible to traverse the dungeon without succumbing to a fatal trap. If at any point your health points reach `0` or less, you are considered out of the game.

# Missing information: "...However, **the goal is to find the smallest jump size that achieves this.**...". So I have to look for the smallest jump size that achieves the desired goal.

def solution(dungeon, health):
  # TODO: Implement the solution
  pass

# Solving the Dungeon Traversal: Survive the Traps! problem.

def solution(dungeon, health):
  # TODO: Implement the solution
  jump_size = 1
  max_health = 1
  min_jump_size = 0    # x
  
  while jump_size <= len(dungeon):
    pos = 0     # retry on the start position
    current_health = health
    while pos < len(dungeon):
      current_health -= dungeon[pos]
      if current_health <= 0:     # out of the game
        break
      pos += jump_size    # just advance
    else:   # susccesfully traversed the dungeon
      if max_health < current_health:  # the first (min) will remain
        max_health = current_health
        min_jump_size = jump_size
        
    jump_size += 1
      
  print(f"Max health: {max_health} with min jump size: {min_jump_size} ")
  if min_jump_size == 0:
    return -1
  else:
    return min_jump_size
  pass