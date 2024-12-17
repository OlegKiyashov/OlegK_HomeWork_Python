from selenium.webdriver.common.by import By
from base_page import BasePage


class ShopPage(BasePage):
    def open_site(self, url):
        self.driver.get(url)

    def login(self, username, password):
        username_input = self.wait_for_element((By.ID, "user-name"))
        password_input = self.wait_for_element((By.ID, "password"))
        login_button = self.wait_for_clickable_element((By.ID, "login-button"))

        username_input.send_keys(username)
        password_input.send_keys(password)
        login_button.click()

    def add_products_to_cart(self, product_ids):
        for product_id in product_ids:
            self.click_element((By.ID, product_id))

    def go_to_cart(self):
        self.click_element((By.CLASS_NAME, "shopping_cart_link"))

    def checkout(self):
        self.click_element((By.ID, "checkout"))

    def fill_checkout_form(self, first_name, last_name, zip_code):
        first_name_input = self.wait_for_element((By.ID, "first-name"))
        last_name_input = self.wait_for_element((By.ID, "last-name"))
        zip_code_input = self.wait_for_element((By.ID, "postal-code"))
        continue_button = self.wait_for_clickable_element((By.ID, "continue"))

        first_name_input.send_keys(first_name)
        last_name_input.send_keys(last_name)
        zip_code_input.send_keys(zip_code)
        continue_button.click()

    def get_total_label(self):
        total_label = self.wait_for_element((By.CLASS_NAME,
                                             "summary_total_label"))
        return total_label.text
