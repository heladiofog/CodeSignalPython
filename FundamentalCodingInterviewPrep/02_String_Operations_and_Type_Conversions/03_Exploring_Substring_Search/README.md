# Unit 3 - Lesson 4 - Exploring Substring Search in Python Strings

Rocketing through these lessons, aren't you? 🚀 Your grasp on substring searches is about to get stellar! Keep it up, and remember, I'm here to help answer any cosmic queries you might have!

## Introduction
Hello, and welcome to our analysis lesson. Today, we will be exploring a classic problem in the realm of string manipulations. We'll learn how to locate all occurrences of a substring within a larger string using Python. The techniques you will learn can be used in scenarios such as text processing and data analysis. Are you ready to dive in? Let's get started!

## Task Statement and Description
Here's our challenge: we have two lists of strings of the same length, one containing the "original" strings and the other, the "substrings". We're to identify all occurrences of each substring within its corresponding original string and return a list of the starting indices of these occurrences. Remember, index counting should start from 0.

### Example

If we take the following lists: Original List: `["HelloWorld", "LearningPython", "GoForBroke", "BackToBasics"] Substring List: ["loW", "ear", "o", "Ba"]`.

This will produce the following outputs: In `"HelloWorld"`, `"loW"` starts at index `3`. In `"LearningPython"`, `"ear"` starts at index `1`. In `"GoForBroke"`, `"o"` appears at indices `1`, `3`, and `7`. In `"BackToBasics"`, "Ba" starts at indices `0 and `6.

So, if `findSubString(["HelloWorld", "LearningPython", "GoForBroke", "BackToBasics"], ["loW", "ear", "o", "Ba"])` is called, the function should return

```Python
[
    "The substring 'loW' was found in the original string 'HelloWorld' at position(s) 3.",
    "The substring 'ear' was found in the original string 'LearningPython' at position(s) 1.",
    "The substring 'o' was found in the original string 'GoForBroke' at position(s) 1, 3, 7.",
    "The substring 'Ba' was found in the original string 'BackToBasics' at position(s) 0, 6."
]
```
Although this task seems reasonably straightforward, it may still feel daunting. Fear not! We will dissect it piece by piece.

## Step-by-Step Solution: Initializing the Output
First, we need to create a place to store the result of our findings. Can you think of a Python data type that we could use for that? That's correct—a list would be perfect for this task!

```Python
def solution(orig_strs, substrs):
    result_arr = []
```
## Pairing Strings and Finding First Occurrence
We use the built-in `zip()` function to create pairs of original strings and substrings. We then use the `find()` method to find the first occurrence of each substring in its related original string. Python string objects have a built-in method called `str.find(substring, starting_index=0)`, which comes in handy here. It returns the lowest index of the substring in `str` that is greater than or equal to `starting_index` if found. Otherwise, it returns `-1`.

```Python
for original, substring in zip(orig_strs, substrs):
    start_pos = original.find(substring)
```
In `original.find(substring)`, we pass the `'substring'` that we want to locate. The function begins the search from the beginning as we have not specified a starting position.

## Finding Subsequent Occurrences
The following step is to locate the rest of the instances of the `'substring'` in the `'original'`.

We use a while loop to accomplish this. But, how will we know when to stop seeking more occurrences? Good question! The moment our `.find()` function begins returning `-1`, it signifies that there are no more matches to be found.

Each time we find a match, we append its starting index to the `match_indices` list and adjust the `start_pos` to search after the end of this match:

```Python
match_indices = []
while start_pos != -1:
    match_indices.append(str(start_pos))
    start_pos = original.find(substring, start_pos + 1)
```
Formatting and Storing the Results
Finally, we format the result for readability and append it to the `result_arr`:

```Python
result_arr.append(f"The substring '{substring}' was found in the original string '{original}' at position(s) {', '.join(match_indices)}.")
```
With this, we've come to the end of our function design.

## The Final Solution
Here is the comprehensive solution, which incorporates all the steps above:

```Python
def solution(orig_strs, substrs):
    result_arr = []

    for original, substring in zip(orig_strs, substrs):
        start_pos = original.find(substring)
        match_indices = []
        while start_pos != -1:
            match_indices.append(str(start_pos))
            start_pos = original.find(substring, start_pos + 1)
        result_arr.append(f"The substring '{substring}' was found in the original string '{original}' at position(s) {', '.join(match_indices)}.")

    return result_arr
```
## Lesson Summary
Congratulations! You've mastered a vital operation in string manipulations—finding all occurrences of a 'substring' in another string. Remember, this algorithm has numerous applications in real-world scenarios. Now that we have thoroughly dissected and examined a systematic way to handle it, I encourage you to practice further. Upcoming exercises will provide an opportunity for you to refine your skills better. Keep on coding and learning!
****

```
``
`
```
