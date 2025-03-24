# You are given a string `s` containing only uppercase letters, with its length `n` ranging from `1` to `100`, inclusive. Your task involves series of sequential comparisons resulting in the removal of certain characters, following this process:

# Form neighbouring pairs in the string sequentially (pair the first and second characters, the third and fourth, and so forth). If the string length is odd, keep the last character unpaired.
# For each pair, compare the characters and remove the character that comes earlier in the lexicographical order. If they are the same, remove the first character in the pair.
# These two steps define a round of operation. Perform these rounds until the string becomes empty.
# If the string length after a round is 1, in the next round the last remaining character is removed and the process terminates.
# Your task is to implement a Python function, `solution(s)`, where `s` is the initial input string. The function should follow the described process and return a list of the removed letters in the order of their removal.

# Each character of the string is an uppercase letter from `A` to `Z`, inclusive.

# As an example, if `s = "BCAAB"`, the output should be `['B', 'A', 'A', 'B', 'C']`.

# The rounds would occur as follows:

# - After the first round, the pairs are `(B,C)`, `(A,A)`, `(B)` and the resulting string is `CAB` with `'B'` and `'A'` being removed. The removed characters list becomes `['B', 'A']`.
# After the second round, the pairs are `(C,A)` and `(B)`, and the resulting string is `CB` with 'A' being removed. The removed characters list becomes `['B', 'A', 'A']`.
# After the third round, `B` is removed and the string becomes `C`. The removed characters list becomes `['B', 'A', 'A', 'B']`.
# After the fourth round, there are no pairs, and thus `'C'` is removed, and the resulting string is empty. The removed characters list becomes `['B', 'A', 'A', 'B', 'C']`.

def solution(s):
  # TODO: implement the solution here
  pass

# Solving the String Processing Through Sequential Pairing problem.

def solution(s):
  # TODO: implement the solution here
  removed_letters = []
  s_len = len(s)
  current_string = s[:]
  
  while True:
    current_string_len = len(current_string)
    remainding_char = '' if current_string_len % 2 == 0 else current_string[current_string_len - 1]
    print(f"current string({current_string}) length: {current_string_len}")
    
    new_string = ''  # to store new current string
    for i in range(0, current_string_len - 1 - (current_string_len % 2), 2):
      if current_string[i] == current_string[i + 1]:
        new_string += current_string[i + 1]
        removed_letters.append(current_string[i])
      elif current_string[i] < current_string[i + 1]:
        removed_letters.append(current_string[i])
        new_string += current_string[i + 1]
      else:
        removed_letters.append(current_string[i + 1])
        new_string += current_string[i]
    # update current String
    current_string = new_string + remainding_char
    if current_string_len == 1:
      removed_letters.append(current_string[0])
      break
  print(f"Removed letters are {removed_letters}")
  return removed_letters
  pass

# Another way to solve the problem by the AI assistant on the platform.
def solution(s):
  removed_letters = []
  current_string = s[:]
  
  while len(current_string) > 1:
    new_string = ''
    for i in range(0, len(current_string) - 1, 2):
        if current_string[i] <= current_string[i + 1]:
          removed_letters.append(current_string[i])
          new_string += current_string[i + 1]
        else:
          removed_letters.append(current_string[i + 1])
          new_string += current_string[i]
    
    # Append the last character if the length is odd
    if len(current_string) % 2 == 1:
      new_string += current_string[-1]
    
    current_string = new_string
  
  # Append the last remaining character
  if current_string:
    removed_letters.append(current_string[0])
  
  return removed_letters