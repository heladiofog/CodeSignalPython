# Unit 4 - Lesson 1 - Nested Loop Pair Discovery: Comparing Elements Across Two Arrays

Astounding work navigating through these programming challenges! I can see you're mastering the art of looping and comparison—keep up the excellent progress! 🚀

## Introduction
Hello and welcome to today's programming practice session! Are you prepared to delve into an exciting task involving nested loops and arrays? Our focus today will be on mastering the use of nested loops to search two arrays. You're about to embark on a fascinating journey of hands-on learning. Let's get started!

## Task Statement
Imagine you've received two lists of integers. Should you choose to accept this mission, you'll need to write a function that locates and returns pairs of integers. The first element of the pair will come from the first list, with the second coming from the second list. Important to note is that the first element must be less than the second.

The order of pairs in your result should follow the order in which they appear in the input lists. For instance, given the lists `[1, 3, 7]` and `[2, 8, 9]`, the function should return `[(1, 2), (1, 8), (1, 9), (3, 8), (3, 9), (7, 8), (7, 9)]`. It's a challenge if no pairs exist, or if any input list is empty. Let's dissect this task to unravel the solution together!

## Solution Building: Step 1
Before we dive into writing code, let's break down the problem. It appears to be an ideal candidate for nested looping.

Begin by initializing an empty list called `result`, which will store our pairs.

```Python
def solution(list1, list2):
  result = []
```
It's always prudent to set up your function and data storage first!

## Solution Building: Step 2
In this step, our focus shifts to the creation of nested loops. We'll need to iterate over both lists simultaneously. To do this efficiently, we'll use nested loops. One outer loop will pick an element from the first list, and an inner loop will skim through each element of the second list.

```Python
def solution(list1, list2):
  result = []
  for i in list1:
    for j in list2:
      # We'll fill this in next
  return result
```
In this context, `i` represents each element in `list1`, and for each `i`, `j` represents each element in `list2`.

## Solution Building: Step 3
Now that we have our loops established, let's introduce the logic inside. Here's where we make a crucial check: Is the element `i` from `list1` lesser than the element `j` from `list2`? If it is, we append the pair `(i, j)` to our result list.

```Python
def solution(list1, list2):
  result = []
  for i in list1:
    for j in list2:
      if i < j:
        result.append((i, j))
  return result
```
During each iteration of our inner loop, we make this check and store the pairs that meet our condition.

## Lesson Summary
Excellent job! You've successfully implemented a complex task using nested loops to search two arrays. You now know how to traverse and manipulate two lists effectively to achieve your desired objective. Keep practicing and continually challenge yourself with more tasks to consolidate your knowledge. In your subsequent practice sessions, you will encounter similar challenges that will further enhance your understanding of this concept. Remember, practice is the key to mastering any concept. Happy coding!

****

```
``
`
```
