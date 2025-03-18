def calculate_jump(forest, start, direction):

  jump = 1

  while (direction * jump) + start >= 0 and (direction * jump) + start < len(forest):
    pos = start
    while 0 <= pos < len(forest):
      if forest[pos] == 1:
          break
      pos += jump * direction
    else:
      return jump

    jump += 1
  return -1

forest = [0, 1, 0, 0, 0, 0, 1, 1]
start = 0
direction = 1
print(calculate_jump(forest, start, direction)) # 2 

## while loop - else block
#Certainly! In Python, the while-else construct is a unique feature. Here's how it works:

# while loop: Executes as long as the condition is True.
# else block: Executes only if the while loop completes normally (i.e., not interrupted by a break statement).
# Here's a simple example:

# ```Python
i = 0
while i < 5:
    print(i)
    i += 1
else:
    print("Loop completed without break")

# In this example, the else block runs because the loop finishes without encountering a break. If a break were used, the else block would be skipped. Does that help clarify?