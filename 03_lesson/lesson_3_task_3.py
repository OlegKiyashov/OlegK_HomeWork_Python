from address import Address
from mailing import Mailing

# Создаем два адреса
to_address = Address('123456', 'Калининград', 'Ленина', '10', '12')
from_address = Address('654321', 'Н Челны', 'Г Тукая', '24', '8')

# Создаем экземпляр класса Mailing
mailing = Mailing(
    to_address,
    from_address,
    500,
    'TR123456789RU'
)

# Печатаем почтовое отправление
print(mailing)
