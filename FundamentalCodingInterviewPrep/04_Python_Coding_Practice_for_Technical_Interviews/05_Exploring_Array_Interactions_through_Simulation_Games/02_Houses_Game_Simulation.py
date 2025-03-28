# n a unique town, there's a popular game that involves the town's houses and their numbers. What's special about this town is that each house is sequentially numbered from 1 to n. The game is played based on an interesting rule regarding these house numbers.

# At each step of the game, every house number must "donate" one of its digits to the house on its right (or in the case of the last house, to the first house). The particular digit to be transferred in each step is dependent on the current game step: during the i-th step, the i-th digit from the right of each house number (1-indexed) is transferred. If a house number doesn't have the specified number of digits for a step, it doesn't donate any digit in that step.

# During the transfer, the chosen digit is removed from its position in the donor house number and then added to the front (leftmost side) of the receiving house number. All numbers change simultaneously.

# The function, house_game(houses), should simulate each step of the game, starting from transferring the rightmost (1st digit) and proceeding one digit position towards the left in each successive step, until there is no change in the house numbers from one step to the next. It should return the sequence of house numbers at the end.

# It is guaranteed that there are at least two houses and there is no digit 0 in the numbers.

# For instance, if houses = [123, 234, 345, 456], the function performs as follows:

# Step 1 -> Transfer the 1st digit from the right (rightmost digit):

# Before Transfer:

# House 1: 12**3**
# House 2: 23**4**
# House 3: 34**5**
# House 4: 45**6**
# Digit Transfer:

# Transfer '3' from House 1 to the front of House 2
# Transfer '4' from House 2 to the front of House 3
# Transfer '5' from House 3 to the front of House 4
# Transfer '6' from House 4 to the front of House 1
# After Transfer: [612, 323, 434, 545]

# Step 2 -> Transfer the 2nd digit from the right:

# Before Transfer:

# House 1: 6**1**2
# House 2: 3**2**3
# House 3: 4**3**4
# House 4: 5**4**5
# Digit Transfer:

# Transfer '1' from House 1 to the front of House 2
# Transfer '2' from House 2 to the front of House 3
# Transfer '3' from House 3 to the front of House 4
# Transfer '4' from House 4 to the front of House 1
# After Transfer: [462, 133, 244, 355]

# Step 3 -> Transfer the 3rd digit from the right (leftmost digit):

# Before Transfer: [**4**62, **1**33, **2**44, **3**55]

# After Transfer: [362, 433, 144, 255]

# In Step 4, no further changes occur, so the final output is [362, 433, 144, 255].

# This sequence of transformations leads to the final set of house numbers, [362, 433, 144, 255].

def house_game(houses):
  # TODO: implement
  pass

# Solving Houses Game Simulation problem. Tryout no. 2.

def house_game(houses):
  # Convertimos los números de las casas en listas de caracteres para manipularlos fácilmente
  houses = [list(str(house)) for house in houses]
  n = len(houses)  # Número de casas
  pos = 1  # Comenzamos con la posición del dígito más a la derecha (1-indexed)

  while True:
    # Creamos una copia de las casas como enteros para verificar si hay cambios al final del paso
    prev_houses = [int("".join(house)) for house in houses]

    # Lista temporal para almacenar los dígitos que se transferirán
    transfers = [None] * n

    # Iteramos sobre cada casa para determinar los dígitos a transferir
    for i in range(n):
      donor = houses[i]  # Casa donante
      # Determinamos el índice del dígito a transferir (el más a la derecha)
      digit_index = len(donor) - pos

      # Si la casa donante tiene al menos un dígito para donar
      if digit_index >= 0:
        # Respalda el dígito a transferir
        transfers[i] = donor[digit_index]

    # Aplicamos las transferencias a las casas receptoras
    for i in range(n):
      receiver = houses[(i + 1) % n]  # Casa receptora (la siguiente, o la primera si es la última)
      if transfers[i] is not None:
        # Extraemos el dígito de la casa donante
        donor = houses[i]
        donor.pop(len(donor) - pos)
        # Añadimos el dígito al frente de la casa receptora
        receiver.insert(0, transfers[i])

    # Convertimos las casas actuales a enteros para comparar con el estado previo
    current_houses = [int("".join(house)) for house in houses]

    # Si después de un paso no hay cambios, terminamos el bucle
    if prev_houses == current_houses:
        break

    # Incrementamos la posición para el siguiente dígito
    pos += 1

  # Convertimos las listas de caracteres de vuelta a enteros
  return [int("".join(house)) for house in houses]

# Prueba del caso proporcionado
print(f"house_game([155, 261, 31]) is {house_game([155, 261, 31])}")

## My WRONG solution:
# def house_game(houses):
#   # Convertimos los números de las casas en listas de caracteres para manipularlos fácilmente
#   houses = [list(str(house)) for house in houses]
#   n = len(houses)  # Número de casas
#   pos = 1

#   while True:
#     # Creamos una copia de las casas como enteros para verificar si hay cambios al final del paso
#     prev_houses = [int("".join(house)) for house in houses]
    
#     # Iteramos sobre cada casa para realizar la transferencia
#     for i in range(n):
#       donor = houses[i]  # Casa donante
#       receiver = houses[(i + 1) % n]  # Casa receptora (la siguiente, o la primera si es la última)
#       # Determinamos el índice del dígito a transferir (el más a la derecha)
#       digit_index = len(donor) - pos

#       # Si la casa donante tiene al menos un dígito para donar
#       if digit_index >= 0:
#         # Extraemos el dígito a transferir
#         digit = donor.pop(digit_index)
#         # Lo añadimos al frente de la casa receptora
#         receiver.insert(0, digit)
#     pos += 1
#     # Convertimos las casas actuales a enteros para comparar con el estado previo
#     current_houses = [int("".join(house)) for house in houses]
#     # print(f"Current houses: {current_houses}, pos {pos}")
#     print(f"Step {pos}:")
#     print(f"  Donor: {donor}")
#     print(f"  Receiver: {receiver}")
#     print(f"  Digit Index: {digit_index}")
#     print(f"  Current Houses: {current_houses}")
#     # Si después de un paso no hay cambios, terminamos el bucle
#     if prev_houses == current_houses:
#       break
      
#   # Convertimos las listas de caracteres de vuelta a enteros
#   return [int("".join(house)) for house in houses]

# # Prueba del caso proporcionado
# print(f"house_game([155, 261, 31]) is {house_game([155, 261, 31])}")


## WRONG Solution:
# def house_game(houses):
#   # TODO: implement
#   # Convertimos los números de las casas en listas de caracteres para manipularlos fácilmente
#   houses = [list(str(house)) for house in houses]
#   n = len(houses)  # Número de casas

#   while True:
#       # Creamos una copia de las casas para verificar si hay cambios al final del paso
#       prev_houses = [house[:] for house in houses]

#       # Iteramos sobre cada casa para realizar la transferencia
#       for i in range(n):
#           donor = houses[i]  # Casa donante
#           receiver = houses[(i + 1) % n]  # Casa receptora (la siguiente, o la primera si es la última)

#           # Determinamos el índice del dígito a transferir (el más a la derecha)
#           digit_index = len(donor) - 1

#           # Si la casa donante tiene al menos un dígito para donar
#           if digit_index >= 0:
#               # Extraemos el dígito a transferir
#               digit = donor.pop(digit_index)
#               # Lo añadimos al frente de la casa receptora
#               receiver.insert(0, digit)

#       # Si después de un paso no hay cambios, terminamos el bucle
#       if prev_houses == houses:
#           break
#   # Convertimos las listas de caracteres de vuelta a enteros
#   return [int("".join(house)) for house in houses]
#   pass

# print(f"house_game([155, 261, 31]) is {house_game([155, 261, 31])}")