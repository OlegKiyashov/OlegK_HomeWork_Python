from selenium.webdriver.common.by import By
from base_page import BasePage


class CalcPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = ("https://bonigarcia.dev/"
                    "selenium-webdriver-java/slow-calculator.html")

    def open(self):
        self.driver.get(self.url)

    def set_delay(self, delay_value):
        delay_input = self.wait_for_element((By.CSS_SELECTOR, "#delay"))
        delay_input.clear()
        delay_input.send_keys(delay_value)

    def scroll_to_equals(self):
        self.scroll_to_element((By.XPATH, '//span[text()="="]'))

    def click_buttons(self, buttons):
        for button_text in buttons:
            self.click_element((By.XPATH, f'//span[text()="{button_text}"]'))

    def get_result(self):
        # Ожидание результата в поле экрана
        self.wait_for_text_in_element(
            (By.CSS_SELECTOR, ".screen"), "15", timeout=60)
        screen = self.wait_for_element((By.CSS_SELECTOR, ".screen"))
        return screen.text
