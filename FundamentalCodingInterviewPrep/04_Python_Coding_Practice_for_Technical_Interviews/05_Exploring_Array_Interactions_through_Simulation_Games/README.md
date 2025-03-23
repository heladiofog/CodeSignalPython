# Unit 5 - Python Coding Practice for Technical Interviews
## Lesson 5 - Exploring Array Interactions through Simulation Games

Thrilled to see you engaging with array interactions and simulation games! You're about to enhance your skills in a fun and practical way, and I'm here to guide you through every step. Keep up the great work, we're going to have a stellar time! 🚀

### Introduction
Welcome! Are you ready to embark on a captivating journey into the world of array manipulations? Today, we're going to explore a fascinating scenario involving a wonderful small town, its houses, and a fun balloon game. Without further ado, let's dive right in!

## Task Statement
Picture a quaint, small town where every house is numbered sequentially from `1` to `n`. One day, a festive town event is held, and balloons are tied to each house. The festivities do not end there. At the conclusion of the event, a fun game is played: at each step of the game, each house sends half of its balloons to the neighboring house simultaneously (the neighbor on the right side, and for the last house, the neighbor is the first house). The game goes on until at some step there are no changes in the amount of balloons compared to the previous step.

The task is to create a Python function, `solution(balloons)`, where `balloons` is a list representing the number of balloons at each house. The function should simulate this game and return the number of steps in the game.

For example, if `balloons = [4, 1, 2]`, the output should be `solution(balloons) = 3`. After the first step, the list becomes `[3, 3, 1]`. This is because the first house sends 2 balloons and gets 1, the second house sends nothing but gets 2, and the third house sends 1 but receives nothing. Note that when the number of balloons `x` is odd, than the house sends `(x - 1) / 2` balloons. After the second step, the list becomes `[2, 3, 2]` and never changes after that. So after the third step, the process finishes.

## Solution Building: Step 1 - Understanding the Problem
Firstly, it's essential to note that we're dealing with a cyclical event. In other words, when iterating over our balloons array, we need to perceive the array as *circular*, meaning `balloons[n - 1]` should refer back to `balloons[0]`. This concept of cyclicity becomes crucial when we consider the last house passing balloons to the first.

## Solution Building: Step 2 - Setting Up The Loop
Confident in our understanding of the problem, we move on to programming our solution. First, we need to set up a loop to iterate the rounds of the balloon sharing. This loop should continue as long as the list changes.

```Python
def solution(balloons):
  steps = 0
  while True:
    steps += 1
    new_balloons = balloons.copy()  # Store updated balloon counts
    # TODO: Share the balloons
    if new_balloons == balloons:
      break
    balloons = new_balloons # Update balloons with new counts.
  return steps
```

## Solution Building: Step 3 - Sharing Balloons
Our next step delves into the core game mechanics: sharing the balloons. Throughout each cycle, each house must share half of its balloons with the next house.

We must also ensure that the last house shares balloons with the first house at the end of each cycle — for this, we'll use the handy modulo `%` operator.

Here's the updated solution, complete with the mechanics of balloon sharing:

```Python
def solution(balloons):
  n = len(balloons)
  steps = 0
  while True:
    steps += 1
    new_balloons = balloons.copy()
    for i in range(n):
      share = balloons[i] // 2  # Balloons to share
      new_balloons[i] -= share  # Decrease balloons of current house.
      new_balloons[(i + 1) % n] += share  # Increase balloons of next house.
    if new_balloons == balloons:
      break
    balloons = new_balloons
  return steps
Bravo! We've navigated through the maze of array manipulation and successfully simulated an intriguing game event.
```

## Lesson Summary
Congratulations on mastering this crucial programming scenario! You've successfully navigated a task involving the simulation of real-world events using array manipulation.

What's next? Now is the time to put into practice everything we've learned today. Try designing different versions of this balloon sharing game. As always, happy coding!

****
```
``
`
```
