# Unit 2 - Lesson 2 - Traversing and Summing Even Digits in an Integer
How stellar of you to keep expanding your skills! 🚀 Keep up the great work as we dive into the intricacies of numbers today!

## Introduction
Welcome! In today's lesson, we'll delve into a unique coding challenge that centers around traversing the digits of a number using a `while` loop under a specific condition. You'll have the opportunity to practice and enhance your skills in working with Python's loops and conditional statements - fundamental concepts in programming. Are you as excited as I am? Let's dive in!

## Task Statement
Today, our objective is to create a function that operates on an integer input. The task might seem simple, but it requires some ingenuity. Here's the mission: given an integer, `n`, we need to calculate and return **the sum of its even digits** — and here's the clincher(punto clave) — without converting `n` into a string. For instance, if `n` equals `4625`, the output should be `12` because the sum of the even digits `4`, `6`, and `2` equals `12`.

Keep in mind that `n` will always be a positive integer between 
`1` and `10^8`. Ready to give it a shot? Great! Let's get started!

## Solution Building: Step 1
To start, we need the basic structure of our function, where we begin by defining a variable `digit_sum` to keep track of the sum of even digits.

Below is the initial platform for our function:

```Python
def solution(n):
    digit_sum = 0
    # Our code will evolve from here
```
## Step 2: Setting up the Loop
The tool we've chosen to traverse through the digits of the input integer `n` is the `while` loop, which is set to run as long as `n` is greater than zero. Let's incorporate this into our function:

```Python
def solution(n):
    digit_sum = 0
    while n > 0:
        # We'll develop our function from here
```

## Step 3: Extracting and Processing Each Digit
Inside our loop, we'll first extract the last digit of `n` using the **modulo operation** (`n % 10`). If the digit is even, we'll increase our `digit_sum` by this digit.

After processing a digit, we'll then chop off the last digit of `n` using integer division (`n // 10`), which allows the while loop to proceed to the next digit. Here's how this appears in the code:

```Python
def solution(n):
    digit_sum = 0
    while n > 0:
        digit = n % 10
        if digit % 2 == 0:  # Check if the digit is even
            digit_sum += digit
        n = n // 10  # Remove the last digit
```

## Step 4: Returning the Result
After summing up all the even digits, the final step is to return our `digit_sum`.

Our complete function now looks like this:

```Python
def solution(n):
    digit_sum = 0
    while n > 0:
        digit = n % 10
        if digit % 2 == 0:  # Check if the digit is even
            digit_sum += digit
        n = n // 10  # Remove the last digit
    return digit_sum
```   
## Lesson Summary
Well done on completing this lesson! You've successfully navigated the foundational concepts of using a `while` loop to traverse the digits of a number and have gained an understanding of how to apply conditions within it. Now, it's your turn to apply what you've learned. I invite you to explore additional challenges to solidify and build upon your new skill set. Remember, the only limit to your growth is the boundary of your dedication. Keep practicing; your Python prowess is growing with each challenge you conquer!
``