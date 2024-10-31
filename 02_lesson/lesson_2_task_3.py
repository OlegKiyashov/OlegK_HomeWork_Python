
import math

def square(side):
    # Вычисляем площадь квадрата

    area = side * side
    return math.ceil(area)  # Округляем вверх

side_length = 5.3
result = square(side_length)

print(f"Площадь квадрата со стороной {side_length} равна {result}")
