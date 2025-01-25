# You are given an initial date as a string in the format `YYYY-MM-DD`, along with an integer `n` which represents a number of days. Your task is to calculate the date after adding the given number of days to the initial date and return the result in the `YYYY-MM-DD` format.

# Keep these points in mind when resolving the task:

# - The initial date string is always valid, formatted as `YYYY-MM-DD`, where `YYYY` denotes the year, `MM` the month, and `DD` the day.
# - The given integer `n` is the number of days you have to add to the initial date and will be up to `50,000`.
# The output should be a string showcasing the final date after adding n days, in the `YYYY-MM-DD` format.
# Your function will be in the form `add_days(date: str, n: int) -> str`.

# Constraints

# - `date` = the date string in the `YYYY-MM-DD` format. The year `YYYY` will be from `1900` to `2100`, inclusive. The month `MM` and the day `DD` will be valid for the given year.
# - `n` = the integer representing the number of days you have to add to the initial date. `n` ranges from `1` to `50,000`, inclusive.
# - You should consider **leap years** in the calculation. A year is a leap year if it is divisible by 4, but century years (years divisible by 100) are not leap years unless they are divisible by 400. This means that the year 2000 was a leap year, although 1900 was not.
# - The month and day result should always be two digits long, padding with a 0 if necessary. For example, July 9th should be formatted as "07-09".
# Example

# For date = '1999-01-01' and n = 365, the output should be '2000-01-01'.

def add_days(date, n):
  days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  # TODO: Implement
  pass

# Solution:
def add_days(date, n):
  days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  # TODO: Implement
  date_parts = [int(part) for part in date.split("-")]
  current_year, current_month, current_day = date_parts
  # leap year
  days_in_month[2] = 29 if is_leap_year(current_year) else 28
  #
  final_date = ''
  
  while n > 0:
    month_remaining_days = days_in_month[current_month] - current_day
    
    if n > month_remaining_days:
      n -= month_remaining_days
    else:
      current_day = n     # remaining_days
      break
        
    # update months and year
    if current_month == 12:
      current_month = 1
      current_year += 1
      current_day = 0
      # leap year update
      days_in_month[2] = 29 if is_leap_year(current_year) else 28
    else:
      current_month += 1
      current_day = 0
  
  final_date = f"{current_year:04d}-{current_month:02d}-{current_day:02d}"
  
  print(f"Final date: {final_date}")
  return final_date
  pass
    
def is_leap_year(year):
  if year % 4 == 0:
    if year % 100 == 0:
      return year % 400 == 0  # Evalúa si es divisible entre 400
    return True  # Divisible entre 4 pero no entre 100
  return False  # No divisible entre 4


"""
def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True  # Divisible entre 400 -> bisiesto
            else:
                return False  # Divisible entre 100 pero no entre 400 -> no bisiesto
        else:
            return True  # Divisible entre 4 pero no entre 100 -> bisiesto
    else:
        return False  # No divisible entre 4 -> no bisiesto

"""

"""
def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
"""
# Not efficient way:
# taking account restrictions
""" def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 == 0:
            return True
        elif year % 100 == 0:
            return False
        return True
    else:
        return False """

add_days('2000-12-31', 365)