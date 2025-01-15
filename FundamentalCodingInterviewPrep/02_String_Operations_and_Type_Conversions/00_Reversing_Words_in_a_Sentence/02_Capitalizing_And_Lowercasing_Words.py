# You are given a string filled with words. Your task is to write a Python function that takes this string as input. Your function should then capitalize the first letter of each word while making the rest of the letters lowercase. Finally, it should recombine the words into a new string where every word starts with a capital letter.

# Here's what to keep in mind:

# The input string will contain between 1 and 100 words.
# Each word is a sequence of characters separated by white space.
# Words consist of characters ranging from a to z, A to Z, 0 to 9, or even an underscore _.
# The provided string will not start or end with a space, and it will not contain double spaces.
# After capitalizing the first character of each word and converting the rest to lowercase, the program should return a single string in which the words maintain their original order.
# If the first character of a word is not a letter (like a number or an underscore), keep it as is.
# Ignore cases where punctuation marks are attached to words (such as "Hello," or "world!"). Words and punctuation should retain their original places in your final output. You are not required to separate punctuation marks from the words in your solution.

# Example

# For the input string "SoME rAndoM _TeXT", the output should be "Some Random _text".

def solution(input_str):
    # TODO: implement the function
    pass

# Solution:
def solution(input_str):
  # TODO: implement the function
  word_list = input_str.split()
  capitalized_string = ''
  capitalized_words = []
  
  for word in word_list:
    capitalized_word = ''
    
    if word[0].isalpha():
      capitalized_word += word[0].upper() + word.lower()[1::]
    else:
      capitalized_word += word.lower()
        
    capitalized_words.append(capitalized_word)
      
  capitalized_string = ' '.join(capitalized_words)
  print(f"Capitalized string: {capitalized_string}")
  return capitalized_string
  pass