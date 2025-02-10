# Unit 4 - Lesson 2 - Processing Words in Sentences with Nested Loops

Blasting through nested loops like a coding astronaut! Your journey in manipulating sentences has reached an impressive level. Keep soaring through the challenges! 🚀

## Introduction
Hello and welcome to today's Python lesson! We are going to dive into a delightful challenge that will test our abilities in string manipulation, more specifically in a concept known as nested loops. Prepare yourself for an interesting journey as we explore how to extract odd-indexed characters from each word in a sentence, but only if the word has an even number of characters. Doesn't it sound exciting? Let's get started!

## Task Statement
Here is a detailed look at our task: We will work with a string that represents a sentence in which words are separated by spaces. Your task is to create a Python function that identifies the odd-indexed characters of words that have an even number of characters. Then, combine these characters into a single string, maintaining the order in which they appear in the sentence.

Let's consider an example to foster a deep understanding: "Python is a high-level programming language." Here, the word 'Python' has 6 characters (an even number), and we will select the odd-indexed characters from this word, specifically, 'y', 'h', and 'n'. Similarly, we select 's' from 'is', and 'i', 'h', 'l', 'v', 'l' from 'high-level'. The words 'a', 'programming', and 'language.' have odd lengths, so they are skipped.

So, if our function is working correctly, it should return "yhnsihlvl". This task highlights the versatility of loops and conditionals in solving all kinds of string challenges!

Let's get started!

## Solution Building: Step 1
We initiate our solution-building process by splitting the sentence into words. Python provides us with a built-in split() function that makes this task easy. The function separates the sentence into words at each space, providing us with a list containing all the words in the sentence.

```Python
def solution(sentence):
  words = sentence.split(' ')
  # we will proceed progressively
```

## Solution Building: Step 2
Now we delve into nested loops: an outer loop that iterates over every single word, and an inner loop that checks every character within each word. Firstly, we'll use an if condition that verifies whether a word has an even length. How do we do this, you ask? By finding the modulus of the length of the word with 2. If this modulus is zero, our word has an even length!

```Python
def solution(sentence):
    words = sentence.split(' ')
    for word in words:
        if len(word) % 2 == 0:  # confirms whether the length of the word is even
            # we are building up our solution progressively
```
## Solution Building: Step 3
With our outer loop set, it's time to complete our inner loop. We intend to iterate over only the odd-indexed characters in each word of even length. To accomplish this, we start from an index of 1 and increment by 2 each time. This strategy ensures our loop only selects the characters at odd indexes.

We then append these characters to our result string, which will be returned as our final output.

```Python
def solution(sentence):
  words = sentence.split(' ')
  result = ''
  for word in words:
    if len(word) % 2 == 0:  # check if the length of word is even
    for i in range(1, len(word), 2):  # loop over odd characters
      result += word[i]
  return result
```
## Lesson Summary
Bravo! You've just successfully navigated through the maze of `nested loops` to extract specific information from words within a sentence. You've learned how to analyze a sentence by breaking it down into its constituent words and then studying each word at an even deeper level.

Now, use this knowledge as a foundation in your exploration of nested loops. Practicing more is key, as the more you apply what you've learned, the more you will reinforce this knowledge. Are you ready to dive deeper into the world of nested loops and string manipulations? Let's dive right in!



****

```
``
`
```
