from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from calc_page import CalcPage


def test_calc():
    # Создаем драйвер
    driver = webdriver.Chrome(service=ChromeService
                              (ChromeDriverManager().install()))
    calc = CalcPage(driver)

    try:
        # Шаг 1: Открываем страницу
        calc.open()

        # Шаг 2: Устанавливаем задержку
        calc.set_delay("45")

        # Шаг 3: Прокручиваем до кнопки "="
        calc.scroll_to_equals()

        # Шаг 4: Нажимаем кнопки "7", "+", "8", "="
        calc.click_buttons(["7", "+", "8", "="])

        # Шаг 5: Проверяем результат
        result = calc.get_result()
        assert result == "15", f"Ожидался результат '15', но найден '{result}'"

        print("Тест прошел успешно!")

    finally:
        # Закрываем браузер
        driver.quit()


if __name__ == "__main__":
    test_calc()
