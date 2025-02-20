# Unit 4 - Lesson 4 - Adding Extremely Large Numbers Represented as Strings

You're truly mastering these concepts, astronaut! Your coding skills are soaring high among the stars. Keep up the awesome work! 🚀

## Introduction
Hello and welcome! Today, we'll delve deep into a captivating problem that involves large numbers -- specifically, adding extraordinarily large numbers. As you may have noticed, traditional calculators and even some programming languages struggle when numbers get exceedingly large. To handle such scenarios efficiently, we'll simulate this process manually using strings. By the end of this discussion, you'll be able to add together numbers that have thousands or even tens of thousands of digits. Intriguing, right? Let's get started.

## Task Statement
In today's task, we'll step into the world of large numbers, where, specifically, we are given two exceedingly large positive integers. However, these aren't your average, everyday large numbers. They are so vast they're represented as strings that can be up to 10,000 digits long!

Accepting our mission means writing a Python function that binds these two "string-numbers" together. The challenge is to perform the addition without converting the entire strings into integers.

Finally, our function should return the resulting sum, represented as a string. While it might seem daunting at first, don't worry -- we'll break it down step by step, mimicking how we manually add numbers.

## Solution Building: Step 1
Before we start coding, let's consider the strategy we're going to adopt. You may recall that each digit in a number has a value, and the position of the digit determines its influence on the total value of the number. This system is called place-value notation.

The first step requires initialization of our variables. We'll use two indices, `i` and `j`, to point to the current digit in `num1` and `num2`, respectively. We'll also need a variable `carry` to hold carryovers from each addition operation. Lastly, we'll employ a list named `res` to hold our result, where each digit from the addition is appended at the front.

```Python
def solution(num1, num2):
    i, j, carry, res = len(num1) - 1, len(num2) - 1, 0, []
```

## Solution Building: Step 2
Having initialized our variables, we can advance to the next step, which involves scanning through `num1` and `num2` from right to left. This scanning goes from the least significant digit to the most significant one.

For each iteration, we extract the digits `n1` from `num1` and `n2` from `num2`. If `i` or `j` is less than `0`, we've processed all the digits in one of the numbers. Consequently, we consider these additional digits as `0`.

```Python
def solution(num1, num2):
  i, j, carry, res = len(num1) - 1, len(num2) - 1, 0, []
  
  while i >= 0 or j >= 0 or carry > 0:
    n1 = int(num1[i]) if i >= 0 else 0
    n2 = int(num2[j]) if j >= 0 else 0
```

## Solution Building: Step 3
After obtaining the digits `n1` and `n2`, our immediate step is to add them. However, the `carry`, which accumulates any overflow from the addition of previous column digits, must also be added. This sum results in a two-digit number, in which the `tens` place becomes a new `carry` and the `units` place is the resultant digit.

Subsequently, we append `curr` to `res` and decrement both `i` and `j` before embarking on the next iteration. Finally, we reverse `res` and join the digits into a single string to acquire our result.

```Python
def solution(num1, num2):
  i, j, carry, res = len(num1) - 1, len(num2) - 1, 0, []
  
  while i >= 0 or j >= 0 or carry > 0:
    n1 = int(num1[i]) if i >= 0 else 0
    n2 = int(num2[j]) if j >= 0 else 0
    total = n1 + n2 + carry
    if total > 9:
      carry = 1
    else:
      carry = 0
    curr = total%10
    res.append(str(curr))
    i, j = i - 1, j - 1

  return ''.join(res[::-1])  # reverse the list and join into a single string
```

## Lesson Summary
Bravo! You've successfully implemented a method to add very large numbers, mimicking the way we traditionally perform addition operations. Achieving this not only requires a sound understanding of place-value notation but also the ability to manipulate strings and arrays effectively. This task may have been challenging, but remember, the greater the struggle, the more glorious the triumph. Now, with this powerful tool in your arsenal, you can confidently tackle problems involving large numbers. In the upcoming practice session, test your new skills with a range of similar challenges. Enjoy coding, and remember, learning is a journey, so take pleasure in the ride!

```
``
`
```
