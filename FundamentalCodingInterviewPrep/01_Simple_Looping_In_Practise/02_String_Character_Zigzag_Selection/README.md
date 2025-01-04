# Unit 2 - Lesson 3 - String Character Zigzag Selection
Blast off on another coding challenge! 🚀 You're about halfway through - keep up the fantastic work and let's master these string manipulations together!

## Introduction
Hello and welcome to our exciting exploration of Python strings! For today's lesson, we've prepared something quite unique: you will learn how to select characters from a string in an order that might initially seem a bit strange but is certainly interesting. We will explain it in such a comprehensive and concise way that you'll master it in no time. Let's get started!

## Task Statement
Imagine this: You are given a string, and you need to go through it and pick its characters, but the order in which you pick them is unusual. You start with the first character, then jump to the last character, move to the second character, then to the second-to-last character, and carry on in this pattern until you run out of characters. Sounds interesting, isn't it?

Here's what we mean:

You are tasked with writing a Python function, `solution(inputString)`. This function will take `inputString` as a parameter, a string composed of lowercase English alphabet letters ('a' to 'z') with a length anywhere between `1` to `100` characters. The function will then return a new string, which is derived from the input string but with characters selected in the order we just discussed.

For example, if the `inputString` is `"abcdefg"`, the function should return `"agbfced"`.

## Solution Building: Step 1 - Initialization
Before we begin problem-solving, let's set up our result store. We initialize a variable, result, as an empty string to store the output.

```Python
def solution(inputString):
    result = ''
```

## Step 2 - Looping over the string
After initialization, we need to iterate over the `inputString`. Python provides the `range` function with which we can define the number of times the loop should run.

The question here is, how many iterations are required for our loop? Given that we are taking two characters per iteration — one from the beginning and one from the end — we need the loop to run for half the length of the list if the length is even and half the length plus one if the length is odd so that we include the middle character.

How do we achieve this? We use `length // 2 + length % 2`. This will ensure that the loop iterates for half the length if it is even and half the length plus one if it is odd.

Here's what our function looks like so far:

```Python
def solution(inputString):
    result = ''
    length = len(inputString)
    for i in range(length // 2 + length % 2):
        # Loop implementation in next step
        pass
```

## Step 3: Adding Characters to Result
Now that we are inside our loop, we can start taking characters and adding them to our `result`.

First, we take a character from the beginning of the input string, i.e., `inputString[i]`, and add it to our `result`.

Next, we take a character from the end of the input string. The index for the last character is `length - 1 - i`. However, we don't want to add this character if it is the same as the one we just added from the beginning. This could happen when the length of the string is odd and we are at the middle character. Hence, we only add it if `length - 1 - i` is not equal to `i`.

After adding the code for these steps, our function becomes:

```Python
def solution(inputString):
    result = ''
    length = len(inputString)
    for i in range(length // 2 + length % 2):
        result += inputString[i]
        if length - 1 - i != i:
            result += inputString[length - 1 - i]
    return result
```

And there you have it, our function is complete!

## Lesson Summary
Congratulations! In this lesson, you managed to master a rather unique aspect of string manipulation. It was not easy, but you did it. Now, selecting characters from a string following such an unusual pattern should feel a lot more intuitive.

It's now time for you to put what you've learned into practice. As with any concept, the best way to truly understand what you've learned is to apply it. I encourage you to tackle other problems that require similar techniques. This exercise will ensure these concepts are ingrained in your mind. Enjoy coding, and remember, persistence is key!

```
``
`