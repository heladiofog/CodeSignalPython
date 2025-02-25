# Unit 5 - Lesson 1 - Array Hopping Adventure: Exploring Index-Based Traversals

Look at you, jumping through coding challenges like a pro! Keep up the fantastic work, we're getting closer to mastering these skills! 🚀


## Introduction
Welcome to a delightful lesson on array traversal! Today, we invite you to join an endearing bunny named Gloria on an intricate quest. Gloria has a soft spot for number games, especially when they involve hopping between arrays. Our goal, on this exciting journey, is to assist Gloria through her escapade and identify the maximum value she encounters along the way. Are you ready to embark on this adventure?

## Task Statement
Gloria's quest unravels with two arrays, both brimming with non-negative integers. Starting at the first element of `arrayA`, she leaps to `arrayB` based on the index she discovers in `arrayA`. She then bounces back to `arrayA` according to the index she stumbles upon in `arrayB`. Gloria repeats these hops until she returns to where she started in `arrayA`. What an adventure!

Your challenge is to craft a Python function that aids Gloria on her trip. The function will take two lists of integers as inputs, representing `arrayA` and `arrayB`. The objective is **to find the highest value** from `arrayB` that Gloria jumps to during her voyage.

It is guaranteed that at some point Gloria returns at the starting position.

### Example

If a`rrayA = [2, 4, 3, 1, 6]` and `arrayB = [4, 0, 3, 2, 0]`, the output should be `3`.

In this scenario, Gloria starts from the first element of `arrayA`, which is `2`. Then, she jumps to `arrayB` at index `2`, where she discovers `3`. She then bounces back to `arrayA` at index `3`, where she arrives at `1`. From there, she leaps back to `arrayB` at index `1`, stumbling upon a `0`. Finally, she bounces back to `arrayA` at index `0`, a location where she started her adventure. Hence she stops here and during this journey, she came across the highest value `3` from `arrayB`.

## Solution Building: Step 1 - Initialization
Before we make headway with our code, let's kickstart with the initialization of variables. Let `indexA` and `indexB` denote the last positions of Gloria in `arrayA` and `arrayB` respectively. We will also use `max_value` for tracking the highest value encountered in `arrayB`. Her quest starts from `arrayA`, so we also maintain a Boolean flag `in_arrayA`.

```Python
indexA = 0
indexB = None
in_arrayA = True
max_value = float('-inf')
```

## Solution Building: Step 2 - Array Hopping
Our assistant for Gloria’s hopping challenge will be a while loop! This _keeps iterating until Gloria returns to her starting position in `arrayA`_.

If Gloria is in `arrayA`, we check if the value in `arrayB` where she is going to land is greater than `max_value`, and update `max_value` if it is. We also switch Gloria's position to the other array in each iteration.

```Python
while True:
  if in_arrayA:
    indexB = arrayA[indexA]
    if arrayB[indexB] > max_value:
      max_value = arrayB[indexB]
  else:
    indexA = arrayB[indexB]
    if indexA == 0:
      return max_value
  in_arrayA = not in_arrayA
```

## Final Function
Collecting all the pieces together, here's our ultimate function:

```Python
def solution(arrayA, arrayB):
  indexA = 0
  indexB = None
  in_arrayA = True
  max_value = float('-inf')
  while True:
    if in_arrayA:
      indexB = arrayA[indexA]
      if arrayB[indexB] > max_value:
        max_value = arrayB[indexB]
    else:
      indexA = arrayB[indexB]
      if indexA == 0:
        return max_value
    in_arrayA = not in_arrayA
```

## Lesson Summary
Heartiest congratulations on guiding Gloria through her array hopping adventure. Not only have you heightened Gloria's joy, but you've also skillfully solved a complex task. You've deftly handled arrays, tracked indices, and made careful use of conditional statements.

This experience should empower you to take on more complex coding challenges. Keep practicing, keep exploring, and keep growing. Happy coding!


****
```
``
`
```
