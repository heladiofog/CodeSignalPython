# ChatGPT solution
def add_days(date, n):
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # Descomponer la fecha inicial
    date_parts = [int(part) for part in date.split("-")]
    current_year, current_month, current_day = date_parts
    
    # Actualizar febrero si el año es bisiesto
    days_in_month[2] = 29 if is_leap_year(current_year) else 28

    while n > 0:
        # Calcular los días restantes del mes actual (incluyendo el día actual)
        month_remaining_days = days_in_month[current_month] - current_day + 1
        
        if n > month_remaining_days:
            # Saltar al siguiente mes
            n -= month_remaining_days
            current_day = 1
            if current_month == 12:  # Si es diciembre, cambia de año
                current_month = 1
                current_year += 1
                days_in_month[2] = 29 if is_leap_year(current_year) else 28
            else:
                current_month += 1
        else:
            # Ajustar el día dentro del mes actual
            current_day += n
            break
    
    # Formatear la fecha final
    final_date = f"{current_year:04d}-{current_month:02d}-{current_day:02d}"
    print(f"Final date: {final_date}")
    return final_date

def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            return year % 400 == 0  # Evalúa si es divisible entre 400
        return True  # Divisible entre 4 pero no entre 100
    return False  # No divisible entre 4

# print(f"Adding days: {add_days('2099-12-31', 50000)}")
add_days('2099-12-31', 50000)
add_days('2000-12-31', 1)
add_days('2000-01-01', 365)
add_days('1999-01-01', 365)
add_days('2000-12-31', 365)
add_days('2004-01-01', 1461)