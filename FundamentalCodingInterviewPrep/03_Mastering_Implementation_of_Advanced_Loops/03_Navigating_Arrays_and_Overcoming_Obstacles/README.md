# Unit 4 - Lesson 3 - Navigating Arrays and Overcoming Obstacles in Python

Blast off on another coding adventure! You've come so far and conquered many challenges along the way. Keep it up, your skills are shooting for the stars! 🚀

## Introduction
Welcome! In today's lesson, we're tackling a thrilling task that combines basic operations with numbers and array manipulation. We will implement a "Move Until Obstacle" game using a linear integer array. Picture yourself as a game developer and get ready to dive into the fun world of creatively solving problems!

## Task Statement
In this "Move Until Obstacle" game, the player begins at the start of a linear array of integers. The number at each position indicates the number of steps a player can move rightward, while an obstacle number is one upon which you can't land. The aim is to move as far right as possible until an obstacle stops you or you reach the array's end.

Your function, `solution(numbers, obstacle)`, needs to tally and return the number of moves needed to reach the array's end without encountering an obstacle. If the player encounters an obstacle, then the function should return the index at which the obstacle lies.

For example, if the function is given the input: `numbers = [2, 3, 3, 4, 2, 4]` and `obstacle = 4`, it should return `5`. This is because the player starts on the 0th index, takes 2 steps as indicated by the number at the 0th index (landing on the 2nd index), and then takes 3 more steps as indicated by the number at the 2nd index to land on the 5th index, which is the obstacle `4`.

If the function is given the input: `numbers = [4, 1, 2, 2, 4, 2, 2]` and `obstacle = 2`, the output should be `2`. The player starts on the 0th index, takes 4 steps, lands on the 4th index, then takes 4 more steps, which brings the player outside the array, so in total the player makes `2` moves.

## Solution Building: Step 1
Our first step is to ensure that we have variables to track the player, i.e., their current position and the moves they've taken so far. We'll call them `position` and `moves`, with both being initialized to `0`:

```Python
def solution(numbers, obstacle):
    position = 0
    moves = 0
```

## Solution Building: Step 2 - Main Loop
Next, we'll use a while loop to iterate over the array. It continues as long as `position` is less than the size of the `numbers` array:

```Python
    while position < len(numbers):
```

## Solution Building: Step 3 - Obstacle Check
Within each iteration, we need to check if the player has met an obstacle. If so, return the `position` at which this obstacle resides:

```Python
  if numbers[position] == obstacle:
      return position
```

## Solution Building: Step 4 - Move Player and Increment Steps
If the current number is not an obstacle, the player proceeds. The number of steps taken is the value at the current `position`. We add this to `position` and increment `moves`:

```Python
  moves += 1
  position += numbers[position]
```

## Final Solution: Outside the Loop
Once the loop ends, either the player has reached the array's end or encountered an obstacle. If the player has navigated the entirety of the array without encountering an obstacle, we want the total `moves` to be returned:

```Python
  return moves
```

The complete function looks like this:

```Python
def solution(numbers, obstacle):
  position = 0
  moves = 0
  while position < len(numbers):
    if numbers[position] == obstacle:
      return position
    moves += 1
    position += numbers[position]
  return moves
```

## Lesson Summary
Congratulations on successfully implementing the "Move Until Obstacle" game using Python! You've navigated task challenges by applying concepts of basic array manipulation and operations with numbers. Celebrate your achievements, but don't stop there! Up next, we have practice sessions filled with similar exercises to reinforce your understanding and skill. So, gear up and let's keep going!


****


```
``
`
```
