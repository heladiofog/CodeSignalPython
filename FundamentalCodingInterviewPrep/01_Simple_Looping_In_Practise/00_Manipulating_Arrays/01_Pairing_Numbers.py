# Skip to main content
# You are provided with a list of `n` integers, where `n` ranges from `2` to `200`, inclusive. The task is to return a list of tuples, each containing a pair of an integer and **its reverse counterpart**.

# In this context, the reverse counterpart of a number is the number with its digits reversed. For example, the reverse counterpart of `123` is `321`.

# You must iterate through the list to find the reverse counterpart for each integer. If this reversed number exists in the list, create a tuple with the original number and its reverse counterpart. If not, skip it.

# Your output should be a list of tuples with the original numbers and their reverse counterparts. The integers in the given list will range from 10 to 9999, inclusive, and each integer in the list is unique.

# Note: The reverse counterpart of a single digit number is the same number. For numbers that result in leading zeros when reversed (e.g., 100 becomes 001, which is 1), consider only the integer value (i.e., 1). It's guaranteed that the original list will not contain integers with leading zeros.

# For example, for numbers = [12, 21, 34, 43, 56, 65], the output should be solution(numbers) = [(12, 21), (21, 12), (34, 43), (43, 34), (56, 65), (65, 56)].

def solution(numbers):
    # TODO: implement solution here
    pass

# Soluiton:
#string_numbers = [str(number) for number in numbers]
# "Hello World"[::-1]

def counterparts_solution(numbers):
  counterpart_tuples = []
  position = 0
  reversed_numbers = [int(str(number)[::-1]) for number in numbers]
  
  for reversed_number in reversed_numbers:
    # Only apend reverse counterpart tuple if the reversed number exists in the original list
    if (reversed_number in numbers):
      counterpart_tuples.append((numbers[position], reversed_number))
    # Always updates position
    position += 1
    
  print(counterpart_tuples)
  return counterpart_tuples
