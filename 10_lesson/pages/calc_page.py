import allure
from selenium.webdriver.common.by import By
from base_page import BasePage


class CalcPage(BasePage):
    """
    Страница калькулятора.

    Атрибуты:
        url (str): URL страницы калькулятора.
    """

    def __init__(self, driver):
        """
        Инициализирует страницу калькулятора.

        Args:
            driver: WebDriver для взаимодействия с браузером.
        """
        super().__init__(driver)
        self.url = ("https://bonigarcia.dev/selenium-webdriver-"
                    "java/slow-calculator.html")

    @allure.step("Открываем страницу калькулятора")
    def open(self) -> None:
        """Открывает страницу калькулятора."""
        self.driver.get(self.url)

    @allure.step("Устанавливаем задержку: {delay_value}")
    def set_delay(self, delay_value: str) -> None:
        """
        Устанавливает задержку выполнения.

        Args:
            delay_value (str): Значение задержки в секундах.
        """
        delay_input = self.wait_for_element((By.CSS_SELECTOR, "#delay"))
        delay_input.clear()
        delay_input.send_keys(delay_value)

    @allure.step("Скроллим к кнопке '='")
    def scroll_to_equals(self) -> None:
        """Прокручивает страницу до кнопки '='."""
        self.scroll_to_element((By.XPATH, '//span[text()="="]'))

    @allure.step("Нажимаем кнопки: {buttons}")
    def click_buttons(self, buttons: list[str]) -> None:
        """
        Нажимает последовательность кнопок.

        Args:
            buttons (list[str]): Список кнопок для нажатия.
        """
        for button_text in buttons:
            self.click_element((By.XPATH, f'//span[text()="{button_text}"]'))

    @allure.step("Получаем результат")
    def get_result(self) -> str:
        """
        Возвращает результат вычислений.

        Returns:
            str: Результат, отображаемый на экране калькулятора.
        """
        self.wait_for_text_in_element((By.CSS_SELECTOR, ".screen"),
                                      "15", timeout=60)
        screen = self.wait_for_element((By.CSS_SELECTOR, ".screen"))
        return screen.text
