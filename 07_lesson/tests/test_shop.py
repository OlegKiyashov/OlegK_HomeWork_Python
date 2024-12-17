from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.shop_page import ShopPage


from pages.shop_page import ShopPage

def test_shop(browser):
    shop = ShopPage(browser)

    # Шаг 1: Открыть сайт магазина
    shop.open_site("https://www.saucedemo.com/")

    # Шаг 2: Авторизоваться
    shop.login("standard_user", "secret_sauce")

    # Шаг 3: Добавить товары в корзину
    products_to_add = [
        "add-to-cart-sauce-labs-backpack",
        "add-to-cart-sauce-labs-bolt-t-shirt",
        "add-to-cart-sauce-labs-onesie",
    ]
    shop.add_products_to_cart(products_to_add)

    # Шаг 4: Перейти в корзину
    shop.go_to_cart()

    # Шаг 5: Нажать Checkout
    shop.checkout()

    # Шаг 6: Заполнить форму своими данными
    shop.fill_checkout_form("Oleg", "K", "20150")

    # Шаг 7: Проверить итоговую сумму
    total_text = shop.get_total_label()
    expected_total = "Total: $58.29"
    assert total_text == expected_total, \
        f"Ожидалось '{expected_total}', но получено '{total_text}'"
