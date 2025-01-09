# Unit 2 - Lesson 5 - Consecutive Character Grouping in Strings
Blasting through string manipulation like a coding comet! 🌠 Keep up the great momentum as you unlock the patterns in this lesson!

## Introduction
Hello there! Today, we’re going to delve into handling and manipulating strings in Python, a skill that is invaluable in many areas of programming. Specifically, we'll learn how to identify consecutive groups of equal characters in a string. Are you curious to know more and enhance your skills? Then let's get started!

## Task Statement
In this lesson, our goal is to write a Python function that accepts a string as input and identifies all consecutive groups of identical characters within it. A group can be defined as a segment of the text where the same character is repeated consecutively.

Your function should return a list of tuples. Each tuple will consist of the repeating character and the length of its repetition. For instance, if the input string is `"aaabbcccaae"`, your function should output: `[('a', 3), ('b', 2), ('c', 3), ('a', 2), ('e', 1)]`.

It's important to note that while processing the input string, we are interested only in alphanumeric characters (i.e., alphabets and digits), whether they are upper or lower case. Any other characters present won't factor into the formation of these groups.

Are you ready to unravel how to accomplish this task? Let's dive in!

## Solution Building, Step 1: Initialization
As is always the case when attempting to solve a problem, it's a good idea to take preliminary steps to establish our scope. First, we will initialize an empty list `groups` to store our results. We will also declare two variables, `current_group_char` and `current_group_length`, which will help us keep track of the current group's character and the length of its consecutive sequence.

```Python
def solution(s):
    groups = []
    current_group_char = None
    current_group_length = 0
```

## Step 2: Loop Through the String
With the setup in place, we now arrive at the main event: processing the input string. For this, we loop through the string to examine each character. At each step, we also need to verify whether the character is alphanumeric, as that's all we're interested in.

```Python
def solution(s):
    groups = []
    current_group_char = None
    current_group_length = 0

    for char in s:
        if char.isdigit() or char.isalpha():
```

## Step 3: Identify the Groups
During our loop, if a character is the same as `current_group_char`, it means that the group is continued, and we merely increment `current_group_length`. However, if the character is different from `current_group_char`, it signifies the start of a new group.

At the start of a new group, we append the tuple `(current_group_char, current_group_length)` to groups, and then update current_group_char and current_group_length with the new character and 1, respectively.

```Python
def solution(s):
    groups = []
    current_group_char = None
    current_group_length = 0

    for char in s:
        if char.isdigit() or char.isalpha():
            if char == current_group_char:
                current_group_length += 1
            else:
                if current_group_char is not None:
                    groups.append((current_group_char, current_group_length))
                current_group_char = char
                current_group_length = 1
```
## Step 4: Wrap Up
After ending the loop, we need to be aware of the potential for a leftover group that has not yet been added to `groups`. This can happen because we only add a group to `groups` when we identify a new group. To ensure we don't miss any groups, we make a final check on `current_group` and, if necessary, add it to `groups`.

```Python
def solution(s):
    groups = []
    current_group_char = None
    current_group_length = 0

    for char in s:
        if char.isdigit() or char.isalpha():
            if char == current_group_char:
                current_group_length += 1
            else:
                if current_group_char is not None:
                    groups.append((current_group_char, current_group_length))
                current_group_char = char
                current_group_length = 1
    if current_group_char is not None:
        groups.append((current_group_char, current_group_length))
    
    return groups
```

## Lesson Summary
Congratulations! You have now learned how to identify consecutive groups of characters in a string using Python. This ability is very helpful, particularly when it comes to analyzing text-related problems, or even when preprocessing data for machine learning. Your next task is to work on similar problems to reinforce what you've learned and gain practice. Remember, mastery comes through persistence and continuous effort. Now get cracking on those strings!

```
``
`