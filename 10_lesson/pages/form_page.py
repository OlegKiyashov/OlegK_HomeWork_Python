import allure
from selenium.webdriver.common.by import By
from base_page import BasePage


class FormPage(BasePage):
    """
    Страница формы.

    Атрибуты:
        url (str): URL страницы формы.
    """

    def __init__(self, driver):
        """
        Инициализирует страницу формы.

        Args:
            driver: WebDriver для взаимодействия с браузером.
        """
        super().__init__(driver)
        self.url = ("https://bonigarcia.dev/selenium-webdriver-"
                    "java/data-types.html")

    @allure.step("Открываем страницу формы")
    def open(self) -> None:
        """Открывает страницу формы."""
        self.driver.get(self.url)

    @allure.step("Заполняем поле '{field_name}' значением '{value}'")
    def fill_field(self, field_name: str, value: str) -> None:
        """
        Заполняет указанное поле.

        Args:
            field_name (str): Имя поля для заполнения.
            value (str): Значение для ввода в поле.
        """
        field = self.wait_for_element((By.NAME, field_name))
        field.clear()
        field.send_keys(value)

    @allure.step("Закрываем всплывающее окно, если оно есть")
    def close_popup_if_exists(self) -> None:
        """
        Закрывает всплывающее окно, если оно присутствует.

        Returns:
            None
        """
        try:
            popup_close_button = self.wait_for_element(
                (By.CSS_SELECTOR, '.popup-close'), timeout=3)
            popup_close_button.click()
        except Exception:
            pass  # Игнорируем, если всплывающее окно отсутствует

    @allure.step("Отправляем форму")
    def submit_form(self) -> None:
        """
        Отправляет форму.

        Returns:
            None
        """
        self.scroll_to_element((By.CSS_SELECTOR, '[type="submit"]'))
        try:
            self.click_element((By.CSS_SELECTOR, '[type="submit"]'))
        except Exception:
            element = self.wait_for_element((By.CSS_SELECTOR,
                                             '[type="submit"]'))
            self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Получаем цвет фона элемента '{css}'")
    def get_element_background_color(self, css: str) -> str:
        """
        Возвращает цвет фона элемента.

        Args:
            css (str): CSS-селектор элемента.

        Returns:
            str: Цвет фона элемента в формате rgba.
        """
        element = self.wait_for_element((By.CSS_SELECTOR, css))
        return element.value_of_css_property("background-color")
