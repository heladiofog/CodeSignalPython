# In our final task, you will process space exploration crew members' data for command assignments! You have been given a string of crew details separated by semicolons. Your mission is to split, clean, and display each member's information correctly. Are you ready, Space Voyager? Let's make this crew list shine!

# Space exploration crew members' data, containing their names, missions, and roles
crew_data = "Neil,Armstrong,Apollo 11,C;Buzz,Aldrin,Apollo 11,P;Michael,Collins,Apollo 11,CM"

# TODO: Split the crew_data string into a list of individual crew member information using the appropriate delimiter

# TODO: Iterate over the list of crew member data

    # TODO: For each member, split their data string using commas as delimiters

    # TODO: Print the crew member's details in a formatted string

# Expected output:
# Neil Armstrong Apollo 11 C
# Buzz Aldrin Apollo 11 P
# Michael Collins Apollo 11 CM

# Solution with and without cleanning:
# # TODO: Split the crew_data string into a list of individual crew member information using the appropriate delimiter
# individual_crew_member_information = crew_data.split(';')

# # TODO: Iterate over the list of crew member data
# for crew_member in individual_crew_member_information:
#     # TODO: For each member, split their data string using commas as delimiters
#     #name, last_name, mission, role = crew_member.split(',')
#     # In the case of data needing some clean up:
#     name, last_name, mission, role = [field.strip() for field in crew_member.split(',')]

#     # TODO: Print the crew member's details in a formatted string
#     print(f"{name} {last_name} {mission} {role}")