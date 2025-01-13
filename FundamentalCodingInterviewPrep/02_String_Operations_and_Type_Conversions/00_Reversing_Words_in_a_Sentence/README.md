# Unit 3 - Lesson 1 - Manipulating Strings: Reversing Words in a Sentence
Astounding work diving into string manipulation techniques! As we explore the intricacies of reversing words today, your coding skills are shining brighter than a supernova! 🌟 Keep it up, and don't hesitate to ask if you need assistance navigating these concepts.

## Introduction
Hello, and welcome! Are you ready to take your string manipulation skills in Python to the next level? Today, we'll explore a task that not only enhances your understanding of strings but also trains your ability to think creatively. The task at hand involves splitting a string into words, then reversing each word as if reflected in a mirror. Intrigued? Let's dive right in!

## Task Statement and Description
Consider a string filled with words. Your task is to write a Python function that accepts such a string. It then takes each of those words, reverses their character order, and, finally, stitches them all together to form a new string with reversed words.

Here's what you need to keep in mind:

- The input string will contain between 1 and 100 words.
- Each word is a sequence of characters separated by white space.
- A word is composed of characters ranging from `a` to `z`, `A` to `Z`, `0` to `9`, or even an underscore `_`.
- The given string will not start or end with a space - double spaces will not appear either.
- After reversing the words, your program should return a single string with the words preserving their original order.

### Example

Suppose that the input string is `"Hello neat pythonistas_123"`.

The function will work on this in the following fashion:

- `'Hello'` becomes `'olleH'`
- `'neat'` becomes `'taen'`
- `'pythonistas_123'` becomes `'321_satsinohtyp'`
- 
The function now combines the obtained strings into one string, resulting in `"olleH taen 321_satsinohtyp"`.

Therefore, if `solution("Hello neat pythonistas_123")` is called, the returned value should be `"olleH taen 321_satsinohtyp"`.

Let's start breaking this down!

## Step-by-Step Solution Building: Step 1
Our very first step requires us to separate the words in the sentence. Python provides us with a built-in `split()` function, which breaks a given string at a specified separator and outputs a list of words. If no argument is provided to the `split()` function, it defaults to using space as the separator. Here is a sample code to illustrate this:

```Python
# an initial example string
input_str = "Hello neat pythonistas_123"

# split the string into words
words = input_str.split()

print(words)
```
You will see `['Hello', 'neat', 'pythonistas_123']` printed out.

## Step-by-Step Solution Building: Step 2
We've successfully extracted the words from the sentence, but they're not reversed yet. Python's `reversed()` function comes to the rescue here. However, it returns something called an iterable and **not a string directly**. To convert this back to a string format, you can use the `join()` function. Let's add these lines to our existing code:

```Python
# an example string
input_str = "Hello neat pythonistas_123"

# split the string into words
words = input_str.split()

# reverse each word 
reversed_words = [''.join(reversed(word)) for word in words]

print(reversed_words)
```
Aha! Now you can see the reversed words: `['olleH', 'taen', '321_satsinohtyp']`.

## Step-by-Step Solution Building: Step 3
Finally, we need to bring these reversed words back together again into a string format, using space as a separator. We get to use `join()` again for this. We call `join()` on the string `' '`, which acts as a spacer between the words. Resultantly, our words are not squashed together when we form them into one string. Here's the code to complete our task:

```Python
def solution(input_str):
    # split the string into words
    words = input_str.split()
    
    # reverse each word 
    reversed_words = [''.join(reversed(word)) for word in words]
    
    # join the words back together with space as a separator
    result = ' '.join(reversed_words)
    
    return result

# Now we call the function and print the returned result outside of the function
print(solution("Hello neat pythonistas_123"))  # this will print: 'olleH taen 321_satsinohtyp'
```
## Lesson Summary
Well done! By completing this lesson, you've gained proficiency in manipulating strings in Python, especially when it comes to reversing the order of characters in a word. I hope you're feeling more confident and enthusiastic about your Python skills. Remember, the key to mastery is regular practice. Therefore, take a moment to explore related problems and practice what you’ve learned. It's all part of the joy of learning!

```
``
`