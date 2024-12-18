from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, locator, timeout=10):
        # Ожидание появления элемента в DOM и его видимости.

        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def wait_for_clickable_element(self, locator, timeout=10):
        # Ожидание, пока элемент станет кликабельным.

        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def wait_for_text_in_element(self, locator, text, timeout=10):
        # Ожидание появления заданного текста внутри элемента.

        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(locator, text)
        )

    def click_element(self, locator):
        # Клик по элементу после ожидания его кликабельности.

        element = self.wait_for_clickable_element(locator)
        element.click()

    def scroll_to_element(self, locator):
        # Прокрутка страницы до элемента.

        element = self.wait_for_element(locator)
        self.driver.execute_script("arguments[0]"
                                   ".scrollIntoView(true);", element)

    def click_with_scroll(self, locator):
        # Прокрутка до элемента и клик по нему.

        element = self.wait_for_clickable_element(locator)
        self.scroll_to_element(locator)
        self.driver.execute_script("arguments[0].click();", element)
