# Unit 3 - Lesson 3 - Parsing and Calculating Seconds from Time Strings in Python

Bravo on reaching this point in your journey through the cosmos of coding! Your dedication is as bright as the stars we're sailing past! 🌟

## Introduction

Welcome! In today's lesson, we will explore the practical application of string operations and type conversions in Python. These concepts are crucial and are deployed in many programming spheres. We'll examine a real-world example: time parsing. Have you ever pondered how to add a certain number of seconds to some specific time? By the end of today's session, you'll be equipped to calculate this using Python. Let's get started!

## Task Statement and Description
Imagine this: You receive a time formatted as a string in `HH:MM:SS` where `HH`, `MM`, and `SS` denote the hour, minute, and second, respectively. You are also given an integer representing a number of seconds. Your task is to calculate the new time after adding the provided seconds and output the result in the `HH:MM:SS` format.

For example, if the input time is 05:10:30 and the number of seconds to add is 123, the output should be 05:12:33 since 123 seconds translate to 2 minutes and 3 seconds.

Take note of these points when resolving this task:

- The input time is invariably a valid time string in the `HH:MM:SS` format, with `HH` ranging from `00` to `23`, `MM`, and `SS` ranging from `00` to `59`.
- The output ought to be a time in the same format.
Let's go ahead and break down how to achieve this in our step-by-step solution guide.

## Step-by-Step Solution Building: Step 1
Our initial step should involve parsing the input time string. From this string, we'll extract the hours, minutes, and seconds as integer values for further calculations. In Python, we can utilize the `split()` method combined with a list comprehension to divide the string at `":"` and convert each substring into an integer:

```Python
time = '12:34:56'
time_parts = [int(part) for part in time.split(":")]
```

By executing this operation, we've successfully parsed the time string and converted the hours, minutes, and seconds into integers.

## Step-by-Step Solution Building: Step 2
Now that we have the hours, minutes, and seconds in integer format, we can effortlessly calculate the total number of seconds elapsed since the day's start. Here's the logic behind it:

- 1 hour comprises 3600 seconds, so we multiply the number of hours by 3600.
- 1 minute comprises 60 seconds, so we multiply the number of minutes by 60.
- The count of seconds remains unaltered.
Given this, we can write the following code:

```Python
seconds_since_start = time_parts[0] * 3600 + time_parts[1] * 60 + time_parts[2]
```
Your function should now compute the cumulative number of seconds from the start of the day.

## Step-by-Step Solution Building: Step 3
Now, we need to add the integer representing a number of seconds to our computed `seconds_since_start`, and also consider cases where the added seconds roll over to the next day:

```Python
total_seconds = (seconds_since_start + seconds) % (24 * 3600)
```
The modulus operator (`%`) ensures that our `total_seconds` value doesn't exceed the total number of seconds in a day (`86400` seconds or `24*3600` seconds).

## Step-by-Step Solution Building: Step 4
In this part of the task, we reverse the previous operation. We're given an integer number of seconds, and we have to convert this into a time string in the `HH:MM:SS` format.

We will use Python's `divmod()` function, which **takes two numbers and returns a pair** - a tuple consisting of their quotient and remainder. We'll perform two `divmod` operations: one with 3600 to get the hours and the rest of the seconds, and one with 60 to get the minutes and the final seconds:

```Python
hours, remainder = divmod(total_seconds, 3600)
minutes, seconds = divmod(remainder, 60)
```

## Step-by-Step Solution Building: Step 5
The final step is to assemble these values into our `HH:MM:SS` format string:

```Python
return f"{hours:02d}:{minutes:02d}:{seconds:02d}"
```
This might look a bit complex, but it's actually very efficient. Inside the f-string, `:02d` ensures that **each time value is a 2-digit number, padding with a `0` if needed**.

## Final Solution
Let's collate all the individual steps and formulate the final function:

```Python
def solution(time, seconds):
    time_parts = [int(part) for part in time.split(":")]
    seconds_since_start = time_parts[0] * 3600 + time_parts[1] * 60 + time_parts[2]
    total_seconds = (seconds_since_start + seconds) % (24 * 3600)
    hours, remainder = divmod(total_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"
```
And voila! You've crafted a function that accurately calculates the new time based on the provided time and number of seconds elapsed since then.

## Lesson Summary
Congratulations! You've adeptly learned how to parse a time string and utilize type conversions to calculate the number of seconds that have passed since the day began. Then you learned how to do the reverse operation: calculate the time based on the number of seconds passed since the beginning of the day. In this lesson, we've practiced essential Python skills, including string operations, list comprehension, and rudimentary arithmetic operations on integers. Continue practicing with similar problems to reinforce your learning, and you will soon find these tasks becoming second nature. In our upcoming sessions, more practical exercises related to this topic await. See you there, and happy coding!


```
``
`
```
