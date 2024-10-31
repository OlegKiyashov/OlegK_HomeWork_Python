def is_year_leap(year):
    if year % 4 == 0:
        return True
    else:
        return False

year = 2024
result = is_year_leap(year)

if result:
    print(f"год {year}: True (високосный)")
else:
    print(f"год {year}: False (не високосный)")