#In this task, you are given a string `s`, and your goal is to produce a new string following a specific pattern. You are to take characters in sets of three, reverse the characters in each set, and then place them back into the string in their original positions, preserving the reverse order within each set. If 1 or 2 characters remain at the end (because the length of the string is not divisible by 3), they should be left as they are.

# The string `s` contains only lowercase English letters, with its length ranging from `1` to `300`, inclusive.

# For example, if you are given the input 'abcdef', the output should be 'cbafed'. For the input 'abcdefg', your function should provide 'cbafedg'.

def reversed_triple_chars(s: str) -> str:
  # TODO: Implement the function that reform the string as described above
  pass

# Solution:
def reversed_triple_chars(s: str) -> str:
  # TODO: Implement the function that reform the string as described above
  whole_reversed_string = ''
  
  # start in 2 for at least one iteration
  for i in range(2, len(s), 3):
    print(f"initial position {i-2}, triplet is {s[i] +  s[i - 1] + s[i - 2]}")
    whole_reversed_string += s[i] +  s[i - 1] + s[i - 2]    # the reversed string
  
  if len(s) % 3 != 0:
    whole_reversed_string += s[-(len(s) % 3)::]
  
  print(f"From {s} - length: {len(s)} To Final reversed string: {whole_reversed_string}")
  return whole_reversed_string
  pass
