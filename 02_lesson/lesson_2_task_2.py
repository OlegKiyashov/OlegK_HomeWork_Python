def is_year_leap(year):
    # Проверяем, является ли год високосным
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False


year = 2024
result = is_year_leap(year)

if result:
    print(f"Год {year}: True (високосный)")
else:
    print(f"Год {year}: False (не високосный)")
