import pytest
from string_utils import StringUtils


@pytest.fixture
def string_utils():
    return StringUtils()


# Тест для метода capitalize
@pytest.mark.parametrize(
    "input_text, expected_output",
    [
        # Позитивные тесты:
        ("Тест", "Тест"),     # строка с первой заглавной буквой
        ("skypro", "Skypro"),  # делает первую букву заглавной
        ("123", "123"),       # числа как строка
        ("15 ноября 2024", "15 ноября 2024"),  # строка с пробелами и числами
        ("тЕст", "Тест"),     # смешанный регистр
        ("ТЕСТ", "Тест"),     # заглавная первая, остальные нижний регистр

        # Негативные тесты:
        ("", ""),            # пустая строка
        (" ", " "),          # строка с одним пробелом
        ("!@#$%", "!@#$%"),  # строка только с символами — без изменений
        ("  тест", "  тест"),  # строка, начинающаяся с пробелов
    ]
)
def test_capitalize(input_text, expected_output):
    string_utils = StringUtils()
    assert string_utils.capitilize(input_text) == expected_output


# Тест для проверки, что метод выбрасывает AttributeError при передаче None
def test_capitalize_none():
    string_utils = StringUtils()
    with pytest.raises(AttributeError):  # при передаче None AttributeError
        string_utils.capitilize(None)


# Тест для метода trim
@pytest.mark.parametrize(
    "input_text, expected_output",
    [
        # Позитивные тесты:
        ("   skypro", "skypro"),   # удаляет пробелы в начале
        ("skypro   ", "skypro   "),   # пробелы в конце, остаются
        ("   skypro   ", "skypro   "),  # пробелы удаляются только с начала
        ("   123   ", "123   "),  # с числами и пробелами, удаляется с начала
        ("15 ноября 2024", "15 ноября 2024"),  # строка с датой и пробелами
        ("skypro", "skypro"),    # нет пробелов — строка остается без изменений

        # Негативные тесты:
        ("", ""),   # пустая строка
        (" ", ""),  # только пробел
        ("\t\n skypro", "\t\n skypro"),  # не удаляет символы табуляции
        # и перевода строки перед строкой
        ("\t\n", "\t\n"),  # Только табуляция и перевод строки не удаляются
        ("123   456", "123   456"),  # пробелы между числами остаются
    ]
)
def test_trim(string_utils, input_text, expected_output):
    assert string_utils.trim(input_text) == expected_output


# Тест для проверки, что метод выбрасывает AttributeError при передаче None
def test_trim_none_error():
    string_utils = StringUtils()
    with pytest.raises(AttributeError):  # Ожидаем AttributeError
        string_utils.trim(None)  # None как входной параметр (пустая строка)


# Тест для метода to_list
@pytest.mark.parametrize(
    "input_text, delimeter, expected_output",
    [
        # Позитивные тесты:
        ("a,b,c", ",", ["a", "b", "c"]),  # разделитель запятая
        ("1:2:3", ":", ["1", "2", "3"]),  # разделитель двоеточие
        ("1-2-3", "-", ["1", "2", "3"]),  # разделитель тире
        ("apple|banana|cherry", "|", ["apple", "banana", "cherry"]),  # черта
        ("apple, nut ,cherry", ",", ["apple", " nut ", "cherry"]),  # пробелы
        ("abc", "x", ["abc"]),   # нет разделителей, целая строка
        ("", ",", []),     # пустая строка
        ("a,,b", ",", ["a", "", "b"]),    # строка с двойным разделит
        ("a,b,c,", ",", ["a", "b", "c", ""]),  # строка заканчивается разделит

        # Негативные тесты:
        ("", ",", []),     # пустая строка
        ("a,,b", ",", ["a", "", "b"]),   # с двойным разделителем
        ("", "|", []),     # пустая строка с любым разделителем
        ("a,,b", ";", ["a,,b"]),  # разделит, который не присутствует в строке
        ("abc|def", " ", ["abc|def"]),  # нет пробела, вернуться целая строка
        ("123123", ",", ["123123"]),  # нет запятых — строка без изменений
    ]
)
def test_to_list(string_utils, input_text, delimeter, expected_output):
    assert string_utils.to_list(input_text, delimeter) == expected_output


# Тест для проверки, что метод выбрасывает AttributeError
# при передаче None и вызове 'startswith'
def test_to_list_none_error():
    string_utils = StringUtils()
    with pytest.raises(AttributeError):  # Ожидаем AttributeError
        string_utils.to_list(None, ",")  # None вернется пустой список


# Тест для метода contains
@pytest.mark.parametrize(
    "input_text, symbol, expected_output",
    [
        # Позитивные тесты:
        ("SkyPro", "S", True),  # строка с заглавной буквой
        ("123", "3", True),   # символ число есть
        ("Sky Pro", " ", True),  # строка с пробелом есть

        # Негативные тесты:
        ("SkyPro", "U", False),  # символ не найден в строке
        ("", "S", False),  # пустая строка
        ([], "P", False),  # пустой список
        (" ", "S", False),  # строка с пробелом символ не найден
    ]
)
def test_contains(string_utils, input_text, symbol, expected_output):
    assert string_utils.contains(input_text,
                                 symbol) == expected_output


# тест для проверки появления исключения AttributeError при передаче None
def test_contains_none_error():
    string_utils = StringUtils()
    with pytest.raises(AttributeError):  # Ожидаем AttributeError
        string_utils.contains(None, "T")  # None вместо строки


# Тест для метода delete_symbol
@pytest.mark.parametrize(
    "input_text, symbol, expected_output",
    [
        # Позитивные тесты:
        ("SkyPro", "k", "SyPro"),  # удаление одного символа
        ("SkyPro", "Pro", "Sky"),  # удаление подстроки
        ("12345", "3", "1245"),    # удаление числа из строки
        ("12345", "5", "1234"),    # удаление символа в конце
        ("a,b,c,d", ",", "abcd"),  # удаление разделителя
        ("apple", "p", "ale"),    # удаление повторяющегося символа
        ("apple", "e", "appl"),   # удаление последнего символа
        ("hello world", "o", "hell wrld"),  # удаление символа,
        # который встречается несколько раз

        # Негативные тесты:
        ("SkyPro", "X", "SkyPro"),  # символа нет в строке, без изменений
        ("", "a", ""),          # пустая строка, результат тоже пустой
        ("123456", "0", "123456"),  # число, которое не присутствует в строке
        ("test", "", "test"),   # пустой символ не должен изменять строку
        ("!!!", "!", ""),     # удаление всех одинаковых символов
        ("  ", " ", ""),      # Удаление пробелов
    ]
)
def test_delete_symbol(string_utils, input_text, symbol, expected_output):
    assert string_utils.delete_symbol(input_text, symbol) == expected_output


# Тест для проверки, что метод выбрасывает AttributeError при None и 'index'
def test_delete_symbol_none_error():
    string_utils = StringUtils()
    with pytest.raises(AttributeError):  # Ожидаем AttributeError
        string_utils.delete_symbol(None, "a")  # строка None, результат None


# Тест для метода starts_with
@pytest.mark.parametrize(
    "input_text, symbol, expected_output",
    [
        # Позитивные тесты:
        ("SkyPro", "S", True),        # начинается с S
        ("SkyPro", "P", False),       # не начинается с P
        ("   SkyPro", " ", True),     # начинается с пробела
        ("SkyPro", "Sk", True),       # начинается с 'Sk'
        ("12345", "1", True),         # начинается с числа '1'
        ("apple", "a", True),         # начинается с буквы 'а'
        ("apple", "p", False),        # не начинается с буквы 'p'
        ("hello world", "h", True),   # начинается с 'h'
        ("hello world", "H", False),  # учитывается регистр (строка с маленькой
        # буквы, символ с заглавной)

        # Негативные тесты:
        ("abc", "d", False),   # символ отсутствует в начале строки
        ("abc", "abcd", False),  # подстрока длиннее строки
        ("apple", "apples", False),  # подстрока длиннее строки
        ("test", "", True),    # пустой символ всегда True
        ("!!!", "!", True),   # начинается с символа '!'
        ("   ", " ", True),  # начинается с пробела (строка из пробелов)
        ("", "S", False),   # пустая строка
    ]
)
def test_starts_with(string_utils, input_text, symbol, expected_output):
    assert string_utils.starts_with(input_text, symbol) == expected_output


# Тест для проверки, что метод выбрасывает AttributeError
# при передаче None и вызове 'startswith'
def test_starts_with_none_error():
    string_utils = StringUtils()
    with pytest.raises(AttributeError):  # Ожидаем AttributeError
        string_utils.starts_with(None, "S")  # None не начинается с "S"


# Тест для метода end_with
@pytest.mark.parametrize(
    "input_text, symbol, expected_output",
    [
        # Позитивные тесты:
        ("SkyPro", "o", True),        # заканчивается на о
        ("SkyPro", "y", False),       # не заканчивается на y
        ("SkyPro ", " ", True),       # заканчивается на пробел
        ("12345", "5", True),         # заканчивается на число '5'
        ("hello world", "d", True),   # заканчивается на 'd'
        ("hello world", " ", False),  # не заканчивается на пробел
        ("hello", "o", True),         # заканчивается на 'о'
        ("apple", "E", False),        # учитывается регистр
        # (строка заканчивается на 'e', не на 'E')

        # Негативные тесты:
        ("abc", "d", False),          # символ отсутствует в конце строки
        ("apple", "p", False),        # не заканчивается на 'p'
        ("apple", "le", True),        # заканчивается на подстроку 'le'
        ("apple", "ples", False),     # подстрока длиннее строки
        ("hello world", "world", True),  # заканчивается на подстроку 'world'
        ("!!!", "?", False),       # не заканчивается на '?'
        ("apple", "", True),     # пустой символ всегда True
        ("   ", " ", True),   # заканчивается на пробел (строка из пробелов)
    ]
)
def test_end_with(string_utils, input_text, symbol, expected_output):
    assert string_utils.end_with(input_text, symbol) == expected_output


# Тест для проверки, что метод выбрасывает AttributeError
# при передаче None и вызове 'endswith'
def test_end_with_none_error():
    string_utils = StringUtils()
    with pytest.raises(AttributeError):  # Ожидаем AttributeError
        string_utils.end_with(None, "o")
        # None не может заканчиваться символом


# Тест для метода is_empty
@pytest.mark.parametrize(
    "input_text, expected_output",
    [
        # Позитивные тесты:
        ("", True),  # пустая строка
        (" ", True),  # строка с пробелом
        ("\t", False),  # строка с табуляцией
        ("\n", False),  # строка с переводом строки
        ("    ", True),  # строка, состоящая только из пробелов
        ("\n\t ", False),  # строка с пробелами,
        # табуляцией и переводом строки

        # Негативные тесты:
        ("SkyPro ", False),  # пробелы в конце строки
        ("S", False),  # строка с одним символом
        ("0", False),  # строка с числовым символом
        ("False", False),   # строка с текстом 'False'
        ("   SkyPro   ", False),  # строка с пробелами и текстом
        ("SkyPro", False),   # непустая строка
        (" SkyPro", False),   # пробелы в начале строки
    ]
)
def test_is_empty(string_utils, input_text, expected_output):
    assert string_utils.is_empty(input_text) == expected_output


# Тест для проверки, что метод выбрасывает AttributeError
# при передаче None и вызове 'startswith'
def test_is_empty_none_error():
    string_utils = StringUtils()
    with pytest.raises(AttributeError):  # Ожидаем AttributeError
        string_utils.is_empty(None)  # None как пустой


def test_is_empty_invalid_input():
    string_utils = StringUtils()
    with pytest.raises(AttributeError):  # Ожидаем AttributeError
        string_utils.is_empty(123)
    with pytest.raises(AttributeError):  # Ожидаем AttributeError
        string_utils.is_empty(['a', 'b'])


# Тест для метода list_to_string
@pytest.mark.parametrize(
    "input_list, joiner, expected_output",
    [
        # Позитивные тесты:
        ([1, 2, 3, 4], ", ", "1, 2, 3, 4"),  # по умолчанию
        (["Sky", "Pro"], "-", "Sky-Pro"),  # разделитель тире
        ([5], ", ", "5"),   # один элемент
        ([], ", ", ""),    # пустой список
        (["a", "b", "c"], "", "abc"),  # пустой разделитель
        # (объединение без разделителя)
        ([None, "b", None], "-", "None-b-None"),  # Список с None,
        # None в строку

        # Негативные тесты:
        (["Sky", "", "Pro"], "-", "Sky--Pro"),  # пустая строка как
        # элемент списка
        ([None, None], ", ", "None, None"),  # список, состоящий только из None
        ([123, "456"], " + ", "123 + 456"),  # смешанный тип (числа и строки)
        ([True, False], ", ", "True, False"),  # булевы значения
        ([""], ", ", ""),  # список с пустой строкой
    ]
)
def test_list_to_string(string_utils, input_list, joiner, expected_output):
    assert string_utils.list_to_string(input_list, joiner) == expected_output
