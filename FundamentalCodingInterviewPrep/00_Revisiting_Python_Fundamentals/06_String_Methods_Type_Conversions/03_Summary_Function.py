# Great progress, Space Voyager! Now, please add the code to process a string of astronaut names and planets to print out their exploration summary.

# This function processes astronaut names and planets from a string 
# then prints out a neat summary of who is exploring which planet.
def process_astronaut_data(data):
    astronaut_details = data.split(';')
    for detail in astronaut_details:
        # TODO: Extract the astronaut name and explored planet from the detail, strip away the whitespace.
        
        # TODO: Print the statement in the format "Astronaut [name] is exploring [planet]."

        # Solution:
        # # TODO: Extract the astronaut name and explored planet from the detail, strip away the whitespace.
        # astronaut_name, planet = [field.strip() for field in detail.split('-')]
        # # TODO: Print the statement in the format "Astronaut [name] is exploring [planet]."
        # print(f"Astronaut {astronaut_name} is exploring {planet}.")
        print(f"Astronaut {astronaut_name} is exploring {planet}.")

# String containing astronaut names and planets, separated by semicolons.
# Each astronaut-planet pair is separated by a dash.
astronaut_data = "    Neil-Mars; Buzz-Jupiter; Sally-Venus    "
process_astronaut_data(astronaut_data)