# Unit 2 - Lesson 1 - Manipulating Arrays to Find Opposite Element Pairs
Astounding work reaching this point in your learning journey! Your grasp of array manipulation is impressive. Keep up the fantastic momentum! 🌟

## Lesson Overview
Welcome! Today, I am excited to guide you through an intriguing task involving arrays: pairing up 'opposite' elements. We're going to learn about accessing and manipulating elements in Python arrays. This task provides an excellent opportunity to refine your array-handling skills in Python. Are you ready to start? Let's dive right in!

## Task Statement and Description
Our task is to form pairs of 'opposite' elements in a given array of integers. In an array of `n` elements, we view the first and last elements as 'opposite', the second and second last elements as 'opposite', and so on. If the array length is odd, the middle element is its own 'opposite'.

You are provided with an array of `n` integers, with `n` ranging from 1 to 100, inclusive. The task necessitates that you return an array of tuples, where each tuple comprises a pair of an element and its 'opposite' element.

For example, for `numbers = [1, 2, 3, 4, 5, 6, 7]`, the output should be `solution(numbers) = [(1, 7), (2, 6), (3, 5), (4, 4), (5, 3), (6, 2), (7, 1)]`.

## Solution Building: Step 1
Before we start writing code, let's familiarize ourselves with how to access the elements of an array in Python.

In Python, the `i`-th element of an array `numbers` can be accessed as `numbers[i]`, with the index starting from `0`. Consequently, the first element can be accessed using `numbers[0]`, the second using `numbers[1]`, and so forth, up to `numbers[numbers.length - 1]` for the last element.

Already dressed to the nines? Brilliant! Now, let's figure out how to access each element's 'opposite'.

## Solution Building: Step 2
The 'opposite' of the `i`-th element of the array is the `numbers.length - i - 1`-th element. To visualize this, imagine that you are standing at the start of a line and your friend is at the end of the line, with both of you being 'opposites'. So, the opposite element for `numbers[0]` is `numbers[numbers.length - 0 - 1]`, the opposite to `numbers[1]` is `numbers[numbers.length - 1 - 1]`, and so on.

Now, let's start coding our solution. We initiate by initializing an empty list in which we will store our 'opposite' pairs and by calculating the array's length for later use.

```Python
def solution(numbers):
    result = []
    n = len(numbers)
```
Next, we loop over all elements in our array.

```Python
def solution(numbers):
    result = []
    n = len(numbers)
    for i in range(n):
        # next step comes here
```

## Solution Building: Step 3
Within our loop, we create a tuple for each pair of 'opposite' elements. This pair includes the `i`-th element and the `n - i - 1`-th element. We then append this tuple to our result list. Here's the final version of our function:

```Python
def solution(numbers):
    result = []
    n = len(numbers)
    for i in range(n):
        result.append((numbers[i], numbers[n - i - 1]))
    return result
```
This function iterates over all elements of the array and, for each element, forms a pair with its 'opposite' and stores the pair as a tuple in the result list.

## Lesson Summary
Brilliant work! You've just navigated through the concept of 'opposite' pairs and array indexing in Python. By now, you should be comfortable with the idea of accessing and pairing elements in an array based on their positions. This is a fundamental step towards achieving proficiency in array manipulation in Python. Up next, we've prepared some hands-on exercises for you to apply and practice what you've learned today. Remember, the more you practice, the better you improve. Keep going, and happy coding!