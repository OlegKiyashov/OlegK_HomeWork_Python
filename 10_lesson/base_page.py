from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """
    Базовый класс для всех страниц.

    Атрибуты:
        driver: WebDriver, используемый для работы с браузером.
    """

    def __init__(self, driver):
        """
        Инициализирует базовый класс.

        Args:
            driver: WebDriver, используемый для взаимодействия с браузером.
        """
        self.driver = driver

    def wait_for_element(self, locator: tuple[str, str],
                         timeout: int = 10) -> WebElement:
        """
        Ожидает появления элемента в DOM и возвращает его.

        Args:
            locator (tuple[str, str]): Локатор элемента в
             формате (By, "значение").
            timeout (int): Время ожидания элемента в секундах.

        Returns:
            WebElement: Найденный элемент.
        """
        return (WebDriverWait(self.driver, timeout).
                until(EC.presence_of_element_located(locator)))

    def wait_for_clickable_element(self, locator: tuple[str, str],
                                   timeout: int = 10) -> WebElement:
        """
        Ожидает, пока элемент станет кликабельным.

        Args:
            locator (tuple[str, str]): Локатор элемента
            в формате (By, "значение").
            timeout (int): Время ожидания элемента в секундах.

        Returns:
            WebElement: Кликабельный элемент.
        """
        return (WebDriverWait(self.driver, timeout).
                until(EC.element_to_be_clickable(locator)))

    def wait_for_text_in_element(self, locator: tuple[str, str],
                                 text: str, timeout: int = 10) -> None:
        """
        Ожидает появления заданного текста внутри элемента.

        Args:
            locator (tuple[str, str]): Локатор элемента в
             формате (By, "значение").
            text (str): Ожидаемый текст.
            timeout (int): Время ожидания текста в секундах.

        Returns:
            None
        """
        (WebDriverWait(self.driver, timeout).
         until(EC.text_to_be_present_in_element(locator, text)))

    def click_element(self, locator: tuple[str, str]) -> None:
        """
        Кликает по элементу после его ожидания.

        Args:
            locator (tuple[str, str]): Локатор элемента в
             формате (By, "значение").

        Returns:
            None
        """
        element = self.wait_for_clickable_element(locator)
        element.click()

    def scroll_to_element(self, locator: tuple[str, str]) -> None:
        """
        Прокручивает страницу до элемента.

        Args:
            locator (tuple[str, str]): Локатор элемента в
             формате (By, "значение").

        Returns:
            None
        """
        element = self.wait_for_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);",
                                   element)

    def click_with_scroll(self, locator: tuple[str, str]) -> None:
        """
        Прокручивает до элемента и кликает по нему.

        Args:
            locator (tuple[str, str]): Локатор элемента
             в формате (By, "значение").

        Returns:
            None
        """
        self.scroll_to_element(locator)
        element = self.wait_for_clickable_element(locator)
        self.driver.execute_script("arguments[0].click();", element)
