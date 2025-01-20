# Unit 3 - Lesson 2 - Parsing and Multiplying Numeric Values in Strings

Blasting through the fundamentals of string parsing and arithmetic - you're doing stellar work! Keep this momentum going! 🚀

## Introduction

Hello there! Today, we have an engaging and practical task on our plate that will flex your Python programming muscles. We will be working on a problem that centers around **parsing strings and making type conversions**. So, buckle up, and let's dive right into it!

## Task Statement and Description

The task du jour involves creating a Python function named `parse_and_multiply_numbers()`. The function will take a string as input. This input string is quite special — it will have numbers and words jumbled together in a free-spirited manner.

The function's job is to parse this input string, find all the numbers, convert these numbers (which are currently strings) into integer data types, subsequently multiply all these numbers together. The output? It’s the product of all those numbers!

For you to get an idea, let's illustrate with an example. For the input string `"I have 2 apples and 5 oranges,"` our function should return the product of 2 and 5, which is 10.

## Step-by-Step Solution Building: Step 1

The first course of action is to parse the string and capture the numbers. But how do we do this? We can sequentialize our search.

Let's create an empty string num where we will gather digits and an empty list numbers to collect all the numbers found:

```Python
input_string = "I have2apples and5oranges"
num = ""
numbers = []
```

## Step-by-Step Solution Building: Step 2

The next move is to iterate through the input string character by character. If we come across a digit, we add it to our `num` string. If the character is not a digit, and `num` is not empty, it means we've reached the end of a number.

We can then convert `num` to an integer, add it to the `numbers` list, and then reset `num` back to an empty string. If the character is not a digit and `num` is empty, we can skip it and proceed.

```Python
for char in input_string:
    if char.isdigit():
        num += char
    elif num:
        numbers.append(int(num))
        num = ""
print(numbers)
```

After running this code, the output on the console will be `[2, 5]`.

## Step-by-Step Solution Building: Step 3

Lastly, we multiply all the numbers in the list numbers together. This multiplication is saved in the variable result.

```Python
result = 1
for number in numbers:
    result *= number
print(result)
```

After running the above piece of code, the output on the console will be `10`.

## Full Solution

Combining all the steps, we arrive at our final solution:

```Python
def parse_and_multiply_numbers(input_string):
    num = ""
    numbers = []
    for char in input_string:
        if char.isdigit():
            num += char
        elif num:
            numbers.append(int(num))
            num = ""
    if num:
        numbers.append(int(num))
    result = 1
    for number in numbers:
        result *= number
    return result
```

This new solution also handles `numbers` ending in the final character of the input string.

## Lesson Summary

Kudos to you! You've just developed a Python function that expertly navigates through strings to identify numbers, performs a data type conversion, and then carries out an arithmetic operation on those numbers. It's as if you've just conducted a symphony orchestra, getting the varied elements to work in harmony!

But remember, in coding, practice makes progress. Try tweaking this solution to perform different operations on the numbers, change the condition for a valid number, or even adapt this concept to solve other problems. Every challenge you tackle helps strengthen your core Python concepts. All the best, and keep coding!

```
``
`
```
