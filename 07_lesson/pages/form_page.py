from selenium.webdriver.common.by import By
from base_page import BasePage


class FormPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = ("https://bonigarcia.dev/"
                    "selenium-webdriver-java/data-types.html")

    def open(self):
        self.driver.get(self.url)

    def fill_field(self, field_name, value):
        field = self.wait_for_element((By.NAME, field_name))
        field.clear()
        field.send_keys(value)

    def submit_form(self):
        self.scroll_to_element((By.CSS_SELECTOR, '[type="submit"]'))
        try:
            self.click_element((By.CSS_SELECTOR, '[type="submit"]'))
        except Exception:
            # Если кнопка недоступна, используем JavaScript
            element = self.wait_for_element((By.CSS_SELECTOR,
                                             '[type="submit"]'))
            self.driver.execute_script("arguments[0].click();", element)

    def get_element_background_color(self, css):
        element = self.wait_for_element((By.CSS_SELECTOR, css))
        return element.value_of_css_property("background-color")

    def get_alerts(self, css):
        return self.driver.find_elements(By.CSS_SELECTOR, css)
