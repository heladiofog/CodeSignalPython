# Unit 5 - Python Coding Practice for Technical Interviews
## Lesson 4 - Navigating Through a Forest with Variable Jumps

Ready to leap over hurdles and calculate your moves? You're doing great navigating this course, and I'm here to boost your momentum! 🚀

### Introduction
Welcome to a captivating session on array manipulation in programming! Today, we'll take you on a journey through a virtual forest represented as an array. Your mission? To find the smallest possible jump size that allows safe passage through the forest without running into any trees. This exercise will help you strengthen your array traversal techniques and problem-solving skills. Let the adventure begin!

## Task Statement
Consider an array which symbolizes a dense forest; each index is either `1`, indicating a tree, or `0`, signifying a clear position. Starting from a fixed initial index and given a specific direction, your objective is to ascertain the smallest possible jump size that enables traversal from the initial position to one of the ends of the array without hitting a tree. Each move you make will be exactly the determined jump size in the given direction.

Keep these pointers in mind:

- The array of binary integers (`0` and `1`) depicts the forest.
- The journey will always commence from a `0` index.
- The direction is an integer. `1` implies jumping toward larger indices, while `-1` denotes jumping toward smaller ones.
- In situations where there is no jump size that can avoid all trees, return `-1` to indicate the impossibility of traversal under these conditions.

The ultimate objective? Identify the minimal jump size that ensures a smooth navigation through the entire forest without hitting a single tree.

**Example**

For the input values `forest = [0, 1, 0, 0, 0, 0, 1, 1]`, `start = 0`, and `direction = 1`, the output should be `4`.

- If you take the jump size equal to `1`, you immediately step on a tree.
- If you choose `2`, you step on a tree after three jumps at `forest[6]`.
- If you choose `3`, you again step on a tree at `forest[6]`.
- For the jump size equal to `4`, you first jump to the 4th position which is a valid position, then jump outside of the array, thereby traversing the forest without hitting a tree.

## Step 1: Start the Function
The first step involves initializing your function which takes as input the forest array, the start position, and the direction. We begin with a jump size of 1:

```Python
def calculate_jump(forest, start, direction):
  jump = 1
  # Other steps will be added here...
```

## Step 2 - Implement the Jumping Mechanism
Now, we'll explore each potential jump size beginning from 1. At each jump size, implement a while loop to execute jumps of that designated size in the identified direction:

```Python
def calculate_jump(forest, start, direction):
  jump = 1

  while (direction * jump) + start >= 0 and (direction * jump) + start < len(forest):
    pos = start
    while 0 <= pos < len(forest):
        
        # Subsequent steps follow...
        
    jump += 1
```
The condition on line 5 (46) ensures the jumps stay within the boundary of the forest array. The expression `(direction * jump) + start` calculates the position index after executing a jump. When direction is `1`, you are jumping towards larger indices, and when it's `-1`, you are jumping towards smaller indices.

The condition checks that this new position remains within the bounds of the forest (array). `>=0` ensures you don't jump too far to the left to negative indices, and `< len(forest)` checks that you don't jump beyond the array's length on the right.

## Step 3 - Check for Trees
Within the nested loop, inspect whether the current position has a tree. If it does, break the loop and examine the next jump size. If it doesn't, carry on jumping:

```Python
def calculate_jump(forest, start, direction):

  jump = 1

  while (direction * jump) + start >= 0 and (direction * jump) + start < len(forest):
    pos = start
    while 0 <= pos < len(forest):
      if forest[pos] == 1:
        break
      pos += jump * direction
    else:
      return jump

    jump += 1
  return -1
```
Here, the function iterates over positive integers as potential jump sizes, starting from 1. For each size, it starts from the initial position and carries out jumps of that magnitude. If a tree is encountered, it halts, adds 1 to the jump size and tests again. If it doesn't encounter a tree and successfully jumps one end of the forest, it promptly returns the jump size. If no viable jump size is found after checking numbers up to the length of the forest, it returns -1.

## Lesson Summary
Congratulations! You've mapped out a path to traverse through the forest and have created a function that identifies the its minimal safe jump size. This exercise has helped you sharpen your problem-solving skills, and become adept at Python, particularly array manipulation and control structures. Continue practicing and exploring different challenges to solidify these skills! We look forward to seeing you take on next challenge!


****
```
``
`
```
