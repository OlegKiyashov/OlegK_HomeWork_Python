import allure
from selenium.webdriver.common.by import By
from base_page import BasePage


class ShopPage(BasePage):
    """
    Страница интернет-магазина.

    Методы:
        open_site: Открывает указанный URL.
        login: Авторизуется с заданными данными.
        add_products_to_cart: Добавляет товары в корзину.
        go_to_cart: Переходит в корзину.
        checkout: Начинает процесс оформления заказа.
        fill_checkout_form: Заполняет форму оформления заказа.
        get_total_label: Возвращает текст общей суммы.
    """

    @allure.step("Открываем сайт: {url}")
    def open_site(self, url: str) -> None:
        """
        Открывает указанный URL.

        Args:
            url (str): URL для открытия.
        """
        self.driver.get(url)

    @allure.step("Авторизуемся с логином '{username}' и паролем '{password}'")
    def login(self, username: str, password: str) -> None:
        """
        Авторизуется на сайте.

        Args:
            username (str): Имя пользователя.
            password (str): Пароль.
        """
        username_input = self.wait_for_element((By.ID, "user-name"))
        password_input = self.wait_for_element((By.ID, "password"))
        login_button = self.wait_for_clickable_element((By.ID, "login-button"))
        username_input.send_keys(username)
        password_input.send_keys(password)
        login_button.click()

    @allure.step("Добавляем продукты в корзину: {product_ids}")
    def add_products_to_cart(self, product_ids: list[str]) -> None:
        """
        Добавляет товары в корзину по ID.

        Args:
            product_ids (list[str]): Список ID товаров для добавления.
        """
        for product_id in product_ids:
            self.click_element((By.ID, product_id))

    @allure.step("Переходим в корзину")
    def go_to_cart(self) -> None:
        """Переходит в корзину."""
        self.click_element((By.CLASS_NAME, "shopping_cart_link"))

    @allure.step("Начинаем оформление заказа")
    def checkout(self) -> None:
        """Начинает процесс оформления заказа."""
        self.click_element((By.ID, "checkout"))

    @allure.step("Заполняем форму оформления заказа")
    def fill_checkout_form(self, first_name: str, last_name: str,
                           zip_code: str) -> None:
        """
        Заполняет форму оформления заказа.

        Args:
            first_name (str): Имя.
            last_name (str): Фамилия.
            zip_code (str): Почтовый индекс.
        """
        first_name_input = self.wait_for_element((By.ID, "first-name"))
        last_name_input = self.wait_for_element((By.ID, "last-name"))
        zip_code_input = self.wait_for_element((By.ID, "postal-code"))
        continue_button = self.wait_for_clickable_element((By.ID, "continue"))
        first_name_input.send_keys(first_name)
        last_name_input.send_keys(last_name)
        zip_code_input.send_keys(zip_code)
        continue_button.click()

    @allure.step("Получаем итоговую сумму")
    def get_total_label(self) -> str:
        """
        Возвращает текст общей суммы.

        Returns:
            str: Текст общей суммы.
        """
        total_label = self.wait_for_element((By.CLASS_NAME,
                                             "summary_total_label"))
        return total_label.text
