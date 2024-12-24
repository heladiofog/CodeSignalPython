# Great job, Space Explorer! In your latest task, you will debug a piece of code from the Employee Information Management System. Here is some code meant to format employee data neatly, but it's not working as expected. Can you spot what's wrong and fix it?

# Employee Information Management System

# A list of employee data
employee_data = "Name: John Doe, Age: 30, Role: Engineer"

employee_info = employee_data.split()
# Solution:
# employee_info = employee_data.split(',')

# Use strip to clean data and join to create a string with newlines
cleaned_data = "\n".join(info.strip() for info in employee_info)

print(cleaned_data)