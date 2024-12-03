lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]


def filter_list(numbers):
    # Функция для фильтрации списка чисел.
    # Возвращает список чисел, которые меньше 30 и делятся на 3 без остатка.

    filtered_numbers = []

    for number in numbers:
        if number < 30 and number % 3 == 0:
            filtered_numbers.append(number)

    return filtered_numbers


result = filter_list(lst)

print("Элементы, меньше 30 и делящиеся на 3:", result)
