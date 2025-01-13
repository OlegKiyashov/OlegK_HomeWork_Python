import allure
from pages.calc_page import CalcPage


@allure.epic("Калькулятор")
@allure.feature("Функциональность калькулятора")
@allure.severity("critical")
@allure.title("Тест работы калькулятора")
@allure.description("Проверяем работу калькулятора с задержкой.")
def test_calc(browser):
    """
    Тестирует функциональность калькулятора.

    Args:
        browser: WebDriver для тестов.
    """
    calc = CalcPage(browser)

    with allure.step("Открываем страницу калькулятора"):
        calc.open()

    with allure.step("Устанавливаем задержку"):
        calc.set_delay("45")

    with allure.step("Скроллим к кнопке '='"):
        calc.scroll_to_equals()

    with allure.step("Выполняем вычисление 7 + 8"):
        calc.click_buttons(["7", "+", "8", "="])

    with allure.step("Получаем и проверяем результат"):
        result = calc.get_result()
        assert result == "15", f"Ожидался результат '15', но найден '{result}'"
