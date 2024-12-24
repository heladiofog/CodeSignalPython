# Great job managing the HR data! Your next challenge is to reconstruct the information for each employee in a more concise format. Examine the employee data, split the information correctly, and if an employee is a Developer or Designer, add a note indicating they are eligible for the junior position.

# A tiny piece of code that represents an HR Employee Data Management system.
# This code will manage a simple string that contains employee data.

employee_data = "Alice,Developer,30|Bob,Manager,45|Charlie,Designer,25"
# Splitting the employee data by '|' to separate each employee's info
employee_list = employee_data.split('|')

# TODO: For each employee, create a formatted string with stripped details and role eligibility for a junior position
for employee in employee_list:
    # TODO: Parse the employee data and add eligibility note if applicable
    # Solution:
    # name, role, age = employee.split(',')
    # eligibility = ' - Eligible for junior position' if (role == 'Developer' or role == 'Designer') else ''
    print("Name: {name} - Role: {role} - Age: {age}{eligibility}")
    # Example: Name: Alice - Role: Developer - Age: 30 - Eligible for junior position
