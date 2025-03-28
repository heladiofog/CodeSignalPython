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


## Al preguntar si se podría con un solo ciclo for...
# Hacerlo en un solo ciclo `for` no es factible si queremos mantener la lógica de transferencias simultáneas. Esto se debe a que las transferencias deben calcularse basándose en el estado original de las casas al inicio del paso, y luego aplicarse a las casas receptoras. Si intentamos hacerlo en un solo ciclo, las modificaciones en las casas receptoras afectarían las transferencias posteriores, rompiendo la simultaneidad.

# Por qué no es factible en un solo ciclo
# 1. Simultaneidad:

#   - Las transferencias deben basarse en el estado original de las casas (antes de que se realicen las modificaciones). Si usamos un solo ciclo, las modificaciones en las casas receptoras afectarían las transferencias de las siguientes casas.

# 2. Separación de Cálculo y Aplicación:

#   - En el diseño actual, primero calculamos los dígitos a transferir (transfers) y luego los aplicamos. Esto asegura que todas las transferencias se basen en el mismo estado inicial.

# 3. Dependencia entre Casas:

#   - Cada casa depende de la transferencia de la casa anterior. Si modificamos las casas receptoras en el mismo ciclo en el que calculamos las transferencias, perderemos la consistencia.

# Alternativa: Mantener Dos Ciclos
# El diseño actual, con dos ciclos separados (uno para calcular las transferencias y otro para aplicarlas), es la forma más clara y correcta de implementar esta lógica. Sin embargo, podemos optimizar el código para que sea más legible y eficiente, pero sin romper la separación de responsabilidades.

# Código Optimizado (Manteniendo Dos Ciclos)
def house_game_2(houses):
    # Convertimos los números de las casas en listas de caracteres para manipularlos fácilmente
    houses = [list(str(house)) for house in houses]
    n = len(houses)  # Número de casas
    pos = 1  # Comenzamos con la posición del dígito más a la derecha (1-indexed)

    while True:
        # Creamos una copia de las casas como enteros para verificar si hay cambios al final del paso
        prev_houses = [int("".join(house)) for house in houses]

        # Calculamos y aplicamos las transferencias en dos pasos
        transfers = [
            donor[len(donor) - pos] if len(donor) >= pos else None
            for donor in houses
        ]

        for i in range(n):
            if transfers[i] is not None:
                # Extraemos el dígito de la casa donante
                houses[i].pop(len(houses[i]) - pos)
                # Añadimos el dígito al frente de la casa receptora
                houses[(i + 1) % n].insert(0, transfers[i])

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
print(f"house_game([155, 261, 31]) is {house_game_2([155, 261, 31])}")

# Cambios Realizados
# 1. Cálculo de Transferencias con List Comprehension:

#   - Usamos una comprensión de listas para calcular los dígitos a transferir:

# transfers = [
#     donor[len(donor) - pos] if len(donor) >= pos else None
#     for donor in houses
# ]

# - Esto simplifica el cálculo de las transferencias y elimina la necesidad de un ciclo explícito.
# 2. Aplicación de Transferencias:

#   - Mantenemos un ciclo separado para aplicar las transferencias, asegurando que las modificaciones no afecten el cálculo.

# Conclusión
# Aunque no es factible hacerlo en un solo ciclo sin romper la lógica de simultaneidad, esta versión optimizada mantiene la separación de responsabilidades y mejora la legibilidad del código. Si tienes más preguntas o necesitas más optimizaciones, no dudes en pedírmelo.