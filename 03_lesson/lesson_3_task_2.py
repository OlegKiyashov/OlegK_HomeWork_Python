
from smartphone import Smartphone

# Создаем список с пятью экземплярами класса Smartphone
catalog = [
    Smartphone('Apple', 'iPhone 14ProMax', '+79161234567'),
    Smartphone('Samsung', 'Galaxy S21Ultra', '+79261234568'),
    Smartphone('Google', 'Pixel 6', '+79361234569'),
    Smartphone('Xiaomi', 'Mi 11', '+79461234570'),
    Smartphone('OnePlus', '9 Pro', '+79561234571')
]

# Печатаем каталог
for phone in catalog:
    print(phone)
