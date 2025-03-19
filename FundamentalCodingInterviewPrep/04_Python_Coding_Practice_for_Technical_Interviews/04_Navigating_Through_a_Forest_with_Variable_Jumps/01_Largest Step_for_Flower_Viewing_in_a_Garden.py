# Assume you have a community garden composed of `n` different types of flowers, with `n` ranging from `1` to `100`. Each type is represented by a distinct number (`1`, `2`, `3`, ..., `n`). The garden is depicted as a 1D array, wherein each element indicates the type of flower planted in that specific location.

# Your task involves visiting each type of flower at least once, traversing the garden in a specific direction (either from left to right with smaller to larger indices, or from right to left). You can take exactly `k` number of steps in the chosen direction, visiting a new location.

# Write a Python function, `largest_step(garden, start, direction)`, that accepts as input the garden as an array, your starting position, and the direction in which you want to travel. This function is expected to compute and return the largest-sized step `step` that you can take so that you can visit each type of flower existing in the garden at least once.

# If no such value of `step` enables you to visit all types of flowers at least once, the function should return `-1`. The direction is given as an integer — `1` indicates moving towards larger indices (right), while `-1` suggests moving towards smaller ones (left).

def largest_step(garden, start, direction):
  # TODO: implement the function
  pass

# Solving the Largest Step for Flower Viewing in a Garden problem.

def largest_step(garden, start, direction):
  # TODO: implement the function
  step = 1
  unique_flowers = set(garden)
  max_step = -1
  
  while step <= len(garden):
    pos = start
    visited_flowers = []
    while 0 <= pos < len(garden):
      visited_flowers.append(garden[pos])
      pos += step * direction
    else:   # update max step if all flowers wer visited
      if set(visited_flowers) == unique_flowers:
        max_step = step if step > max_step else max_step
    step += 1
  print(f"Max step that allows to visit every flower is {max_step}")
  return max_step
  pass