# Bob, Alice's friend, is also interested in string manipulations. Inspired by Alice's technique, he has devised his own string encoding scheme. He takes a sentence, which is a string of n alphanumeric characters (ranging from a-z, A-Z, 0-9), including spaces and punctuation marks, with n ranging from 1 to 500, inclusive. His encoding technique consists of the following steps:

# He replaces each alphanumeric character with the previous character in their respective sequence, i.e., for alphabets, he moves in the alphabetical order, and for numbers, he moves in the ordinal sequence.

# For instance, given a string word, for each character, if it's not a or A or 0, he replaces it with the character that precedes it in the sequence.
# For the character a or A, he replaces it with z or Z, respectively.
# For the number 0, he replaces it with 9.
# Another important aspect of Bob's algorithm involves frequency analysis. After shifting the characters, he counts the frequency of each alphanumeric character in the new string. Then, he creates an association between each alphanumeric character and its frequency and ASCII value. Each character maps to a number, which is the difference between the ASCII value of the character and its frequency. Once this is done, he computes the absolute value of each of these differences.

# The task is to help Bob generate a list of these absolute differences, sorted in ascending order.

def solution(sentence):
  # TODO: Implement the solution following the task description
  pass

# Solving the Character Encoder and Frequency Analyzer problem.

def solution(sentence):
  # TODO: Implement the solution following the task description
  prev_string = ''
  frequency_dictionary = {}
  calculated_values = []
  
  for character in sentence:
      prev_character = character  # initially remains the same
      if character.isdigit():
          prev_character = '9' if character == '0' else chr(ord(character) - 1)
      elif character.isupper():
          prev_character = 'Z' if character == 'A' else chr(ord(character) - 1)
      else:
          prev_character = 'z' if character == 'a' else chr(ord(character) - 1)
      
      if character.isalnum():
          prev_string += prev_character
          if prev_character in frequency_dictionary:
              frequency_dictionary[prev_character] += 1
          else:
              frequency_dictionary[prev_character] = 1
      else:
          prev_string += character
  
  # print(f"Prev string: {prev_string}")
  # Freq differences calculation
  for character, freq in frequency_dictionary.items():
      calculated_values.append(ord(character) - freq)
  
  calculated_values.sort()
  
  print(f"Transformed sentence: {prev_string}")
  # print(f"Sorted values: {calculated_values}")
  return calculated_values
  pass