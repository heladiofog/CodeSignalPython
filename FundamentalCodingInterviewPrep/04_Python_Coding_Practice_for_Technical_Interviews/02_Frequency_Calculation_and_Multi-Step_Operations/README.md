# Unit 5 - Python Coding Practice for Technical Interviews
## Lesson 2 - Frequency Calculation and Multi-Step Operations

Astounding effort on reaching this stage in your coding journey! The skills you're building are out of this world! 🚀 Keep up the fantastic work as we continue with more string manipulation and value reuse strategies.

## Introduction
Hello! Are you ready for an exciting voyage into the wonderful realm of strings and data structures? Today, we will be assisting Alice, an aspiring cryptographer, with an intriguing string manipulation task. She loves playing with strings and has come up with a unique string encoding scheme. I assure you, this will be an enlightening journey that will stretch your programming muscles. Let's get started!

## Task Statement
Alice has devised a unique way of encoding words. She takes a word and replaces each character with the next character in the alphabetical order. In other words, given a string word, for each character, if it's not z, she replaces it with the character that comes next alphabetically. For the character z, she replaces it with a.

Another element of Alice's algorithm involves frequency analysis. After shifting the characters, she counts the frequency of each character in the new string. Then, she creates an association of each character with its frequency and ASCII value. Each character maps to a number, which is a product of the ASCII value of the character and its frequency. The aim of our task is to construct a list that contains these products, sorted in descending order.

Example

For the input string "banana", the output should be [294, 222, 99].

The string "banana" will be shifted to "cbobob".

Calculating the product of frequency and ASCII value for each character:

The ASCII value for 'c' is 99, it appears once in the string so its product is 99x1 = 99.
The ASCII value for 'b' is 98, it appears three times in the string so its product is 98x3 = 294.
The ASCII value for 'o' is 111, it appears twice in the string so its product is 111x2 = 222.
Collecting these products into a list gives [99, 294, 222]. Sorting this list in descending order results in [294, 222, 99].

## Solution Building: Step 1 - Mapping each character to the next alphabetical character
Our first step involves mapping each character of the input string to the next alphabetical character. For this, we define the next_string as an empty string, storing the result of the shift operation. We then iterate over each character of the input string. If a character is not z, we replace it with the next alphabetical character using the built-in chr and ord functions. If it is z, we replace it with a.

Here's the updated function:

Python
Copy to clipboard
def character_frequency_encoding(word):
    next_string = ''
    for letter in word:
        next_string += 'a' if letter == 'z' else chr(ord(letter) + 1)

## Solution Building: Step 2 - Counting the frequency of characters in next_string
The next step is to track the frequency of each character in next_string. We start by initializing an empty dictionary, frequency_dict. Then, we iterate over next_string. If the current character exists in frequency_dict, we increment its frequency by 1. If it doesn't exist, we add it to frequency_dict with a frequency of 1.

Incorporating this step into the function, our code now looks like this:

Python
Copy to clipboard
def character_frequency_encoding(word):
    next_string = ''
    for letter in word:
        next_string += 'a' if letter == 'z' else chr(ord(letter) + 1)
    frequency_dict = {}
    for letter in next_string:
        if letter in frequency_dict:
            frequency_dict[letter] += 1
        else:
            frequency_dict[letter] = 1

## Solution Building: Step 3 - Building the product list
Next, we calculate the numerical representation for each unique character. We initialize an empty list, combined_values, to store these numbers. For each character in frequency_dict, we calculate the product of its ASCII representation and its frequency in next_string and append this to combined_values.

Here's the updated function:

Python
Copy to clipboard
def character_frequency_encoding(word):
    next_string = ''
    for letter in word:
        next_string += 'a' if letter == 'z' else chr(ord(letter) + 1)
    frequency_dict = {}
    for letter in next_string:
        if letter in frequency_dict:
            frequency_dict[letter] += 1
        else:
            frequency_dict[letter] = 1
    combined_values = []
    for letter, freq in frequency_dict.items():
        combined_values.append(ord(letter) * freq)

## Solution Building: Step 4 - Sorting the final values
The final step is to sort the list combined_values in descending order. We use Python's built-in sort function. Here's our complete function:

Python
Copy to clipboard
def character_frequency_encoding(word):
    next_string = ''
    for letter in word:
        next_string += 'a' if letter == 'z' else chr(ord(letter) + 1)
    frequency_dict = {}
    for letter in next_string:
        if letter in frequency_dict:
            frequency_dict[letter] += 1
        else:
            frequency_dict[letter] = 1
    combined_values = []
    for letter, freq in frequency_dict.items():
        combined_values.append(ord(letter) * freq)
    combined_values.sort(reverse=True)
    return combined_values

## Lesson Summary
Well done! You've successfully tackled an intricate problem which required you to exercise multiple topics such as string manipulation, dictionary processing, and list sorting. This task underscored the importance of reusing already calculated values. I encourage you to apply what you've learned today to other tasks. There are many more exciting challenges waiting for you in the upcoming practice sessions. Happy coding!


****
```
``
`
```
