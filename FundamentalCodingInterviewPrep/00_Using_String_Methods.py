# Your mission is to practice the `join()` method you've recently learned. Modify the given code to combine the astronaut's name and year of birth using `join()` instead of string concatenation. Can you implement a solution that works for any number of variables (e.g., if the astronaut info includes not just name and year of birth but also a year of death)?
# `

astronauts_data = "Buzz Aldrin, 1930;Yuri Gagarin, 1934;Valentina Tereshkova, 1937"

# Splitting the string into a list of astronaut info and stripping any whitespace
astronauts_list = astronauts_data.split(";")
cleaned_astronauts = []

for astronaut in astronauts_list:
    name, year = astronaut.split(",")
    cleaned_astronauts.append(name.strip() + " " + year.strip())  # Modify this line to use the join() method
    # # Solution: Remove 2 above lines and:
    # cleaned_info = [astro_field.strip() for astro_field in astronaut.split(",")]
    # cleaned_astronauts.append(' '.join(cleaned_info))
    # # Solution en una línea:
    # cleaned_astronauts.append(' '.join([astro_field.strip() for astro_field in astronaut.split(",")]))

print(cleaned_astronauts)  # ['Buzz Aldrin 1930', 'Yuri Gagarin 1934', 'Valentina Tereshkova 1937']