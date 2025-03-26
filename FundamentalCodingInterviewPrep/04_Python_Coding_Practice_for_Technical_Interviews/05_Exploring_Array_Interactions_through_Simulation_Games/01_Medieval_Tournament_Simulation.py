# Imagine a medieval tournament where knights participate in jousting matches. The knights are arranged in a circular formation (represented as an array in your program), and each knight is initially assigned strength, represented as integers from 1 to 100, determined randomly.

# The game consists of rounds. On each round, each knight fights the knight on his right side by subtracting the strength of his opponent from his own. Since this is a circular game, the knight on the right side of the last knight in the array is the first knight. Note that all matches are played in parallel, so the strengths are updated only after all matches are played. If after a match, a knight's strength becomes equal to or less than zero, symbolizing the knight's defeat, the knight is removed from the game in the next round.

# The game continues until a situation develops in which no more moves can be made. This happens either when there is just one knight standing or all remaining knights have equal strength meaning no knight can win a match.

# Given the list of knights' strengths in the initial order, your program should calculate the number of rounds in the tournament.

def tournament(knights):
  # TODO: Implement the function to simulate the tournament
  pass

# Solving the Medieval Tournament Simulation problem.

def tournament(knights):
  # TODO: Implement the function to simulate the tournament
  rounds = 0
  knights_len = len(knights)
  
  while knights_len > 1:
    first_knight_strength = knights[0]
    knights_after_fight = []

    for i in range(knights_len):
      if i == knights_len - 1:
        knights[i] -= first_knight_strength
      else:
        knights[i] -= knights[i + 1]
      
      if knights[i] > 0:
        knights_after_fight.append(knights[i])
    rounds += 1
    if len(knights_after_fight) == 1 or knights == knights_after_fight:
        break
    knights = knights_after_fight
    knights_len = len(knights)

  print(f"Rounds {rounds}, knights: {knights}")
  return rounds
  pass