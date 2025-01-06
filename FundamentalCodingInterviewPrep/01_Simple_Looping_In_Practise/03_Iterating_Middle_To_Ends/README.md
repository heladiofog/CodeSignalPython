# Unit 2 - Lesson 4 - Iterating Through an Array from Middle to Ends
You've been doing stellar work navigating through these concepts! It's an astronomical feat! 🌟 Keep up the fantastic effort as we venture through arrays in this new lesson.

## Introduction
Greetings! Welcome to our lesson today, where we'll be taking a deep dive into an intriguing aspect of array manipulation. Have you ever considered the idea of traversing an array not from start to end or from end to start, but from the middle, extending towards both ends simultaneously? Today's lesson is all about this concept. Trust me, it's going to be fascinating! Let's jump right in.

## Task Statement
Our task is as follows: Given an array of integers, we aim to return a new array that emerges from the center of the original array and alternates direction towards both ends. In other words, the first element of our new array will be the middle element of the original one. After establishing the starting point, we will alternate between the elements to the left and to the right of the initial center until we have incorporated every element. If the length of the initial array is even, we first take the the element to the left of the center, then the one to the right of the center, then do the alternation as described above.

For example, for `numbers = [1, 2, 3, 4, 5]`, the output should be `[3, 2, 4, 1, 5]`.

This task might initially seem complex. However, don't worry. We're going to break it down and construct our solution step by step. Keep in mind an additional condition: the length of the array—represented as `n`—can vary from `1` to `100,000`, inclusive.

## Solution Building: Step 1
To start, we need to establish the middle point of our array. Why the middle, you ask? Well, our task necessitates that we traverse the array from the center to the ends. Python's integer division operator, `//`, allows us to determine the middle. If the array has an odd length, we add the middle element to the `new_order` array (as it's not paired with any other element), otherwise we keep it empty for now.

Here's a look at its application in the code:
```Python
def iterateMiddleToEnd(numbers):
    mid = len(numbers) // 2 # The index of the left middle element
    if len(numbers) % 2 == 1:
        new_order = [numbers[mid]] # Adding the middle element to the resulting array
    else:
        new_order = [] # No elements in the resulting array for now
```
## Solution Building: Step 2
The resolution of our task requires two pointers: `left` and `right`. These pointers will originate from just before and just after the middle element, respectively.

Here's an illustration of how we can implement this in our Python function:

```Python
def iterateMiddleToEnd(numbers):
    mid = len(numbers) // 2 # The index of the left middle element
    if len(numbers) % 2 == 1:
        left = mid - 1 # The left to the middle element
        right = mid + 1 # The right to the middle element
        new_order = [numbers[mid]] # Adding the middle element to the resulting array
    else:
        left = mid - 1 # Left middle element
        right = mid # Right middle element
        new_order = [] # No elements in the resulting array for now
```

## Solution Building: Step 3
Now that our pointers are initialized, it's time to traverse the array and construct our new order. For this, we can effectively utilize a while loop in Python, which continues looping until the `left` pointer is less than zero and the `right` pointer is not yet at the end of the list. In each iteration, we add the element at index `left` to the new_order list, decrease the left pointer by one, add the element at index `right`, and increase the right pointer by one.

This is what the code looks like:

```Python
def iterateMiddleToEnd(numbers):
    mid = len(numbers) // 2 # The index of the left middle element
    if len(numbers) % 2 == 1:
        left = mid - 1 # The left to the middle element
        right = mid + 1 # The right to the middle element
        new_order = [numbers[mid]] # Adding the middle element to the resulting array
    else:
        left = mid - 1 # Left middle element
        right = mid # Right middle element
        new_order = [] # No elements in the resulting array for now

    while left >= 0 and right < len(numbers):
        new_order.append(numbers[left])
        new_order.append(numbers[right])
        left -= 1
        right += 1
            
    return new_order
```
This way, we have created a new ordered array, starting from the middle and alternating between left and right elements all the way to the end of the original array. This approach capably satisfies the requirements of our task!

## Lesson Summary
Congratulations on reaching the end of this lesson! You've just uncovered a fascinating method of traversing and manipulating arrays! Be proud of yourself for comprehending this concept and implementing it in the code. As is always the case, practice makes perfect. Therefore, I encourage you to apply this concept to similar problems. Your journey in mastering Python and algorithms has just begun. Take the next step, and code away!

```
``
`