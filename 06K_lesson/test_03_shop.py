from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_shop_checkout():
    # Инициализация драйвера
    driver = webdriver.Chrome()

    try:
        # Шаг 1: Открыть сайт магазина
        driver.get("https://www.saucedemo.com/")

        # Шаг 2: Авторизоваться
        username_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "user-name"))
        )
        password_input = driver.find_element(By.ID, "password")
        login_button = driver.find_element(By.ID, "login-button")

        username_input.send_keys("standard_user")
        password_input.send_keys("secret_sauce")
        login_button.click()

        # Шаг 3: Добавить товары в корзину
        products_to_add = [
            "add-to-cart-sauce-labs-backpack",
            "add-to-cart-sauce-labs-bolt-t-shirt",
            "add-to-cart-sauce-labs-onesie",
        ]
        for product_id in products_to_add:
            add_to_cart_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, product_id))
            )
            add_to_cart_button.click()

        # Шаг 4: Перейти в корзину
        cart_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))
        )
        cart_button.click()

        # Шаг 5: Нажать Checkout
        checkout_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "checkout"))
        )
        checkout_button.click()

        # Шаг 6: Заполнить форму своими данными
        first_name_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "first-name"))
        )
        last_name_input = driver.find_element(By.ID, "last-name")
        zip_code_input = driver.find_element(By.ID, "postal-code")
        continue_button = driver.find_element(By.ID, "continue")

        first_name_input.send_keys("Oleg")
        last_name_input.send_keys("K")
        zip_code_input.send_keys("20150")
        continue_button.click()

        # Шаг 7: Проверить итоговую сумму
        total_label = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME,
                                            "summary_total_label"))
        )
        total_text = total_label.text
        expected_total = "Total: $58.29"
        assert total_text == expected_total, (f"Ожидалось '{expected_total}'"
                                              f", но получено '{total_text}'")

    finally:
        # Закрыть браузер
        driver.quit()
