
def month_to_season(month):
#Функция, которая принимает номер месяца и возвращает название сезона.
# Аргументы:month -- номер месяца (1-12)
# Возвращает:Название сезона или сообщение об ошибке, если номер месяца некорректен.

    if month in [12, 1, 2]:
        return "Зима"
    elif month in [3, 4, 5]:
        return "Весна"
    elif month in [6, 7, 8]:
        return "Лето"
    elif month in [9, 10, 11]:
        return "Осень"
    else:
        return "Некорректный номер месяца"

# Список месяцев для тестирования
month_numbers = [2, 4, 6, 11, 13]

for month_number in month_numbers:
    season = month_to_season(month_number)
    print(f"Месяц {month_number}: {season}")
