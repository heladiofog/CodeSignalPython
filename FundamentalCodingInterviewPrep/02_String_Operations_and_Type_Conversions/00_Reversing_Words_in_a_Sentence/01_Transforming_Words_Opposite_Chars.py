# Given a string consisting of words separated by whitespace, your task is to write a Python function that accepts this string. It then replaces each character in the words with the corresponding character opposite in the English alphabet and stitches them all together to form a new string.

# Here's what you need to consider:

# The input string will include between 1 and 100 words.
# Each word consists of characters separated by white space.
# A word is composed of characters ranging from a to z or A to Z. So, if a word contains a lowercase 'a', for instance, it should be replaced with 'z', 'b' with 'y', 'c' with 'x', and so on, maintaining the same case. For words with an uppercase 'A', it should be replaced with 'Z', 'B' with 'Y', 'C' with 'X', and so forth, while preserving the uppercase.
# The given string will not start or end with a space, and there will be no occurrence of double spaces.
# After transforming the characters of the words, form a new string by taking the last word first and appending the remaining words in their original order, each separated by spaces.
# Note: The opposite letter mappings are as follows: a ↔ z, b ↔ y, c ↔ x, ..., m ↔ n, n ↔ m, ..., x ↔ c, y ↔ b, z ↔ a. The mapping is case-sensitive.

# Example

# For the input string `"CapitaL letters"`, the output should be `"ovggvih XzkrgzO"`.

def solution(input_str):
    # TODO: implement the string transformation function
    pass

# Solution:
def solution(input_str):
  # TODO: implement the string transformation function
  transformed_string = ''
  words_list = input_str.split()
  transformed_words = []
  
  for word in words_list:
    transformed_words.append(transform_word(word))
  
  # rearrange words
  transformed_string = ' '.join(transformed_words[-1::] + transformed_words[:-1:])
  
  print(f"Transformed string is {transformed_string}")
  return transformed_string
  pass
    
    
def transform_word(word):
  opposite_chars_word = ''
  A_position = ord('A')
  Z_position = ord('Z')
  a_position = ord('a')
  z_position = ord('z')
  
  for letter in word:
    # for 'A' to 'Z' and for 'a' to 'z'
    # letter - a = (distance)
    # opposite = z - distance
    if letter.isupper():
      opposite_chars_word += chr(Z_position - (ord(letter) - A_position))
    else:
      opposite_chars_word += chr(z_position - (ord(letter) - a_position))
  
  # Transform original word
  pass