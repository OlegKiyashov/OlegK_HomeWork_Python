import allure
from pages.shop_page import ShopPage


@allure.epic("Магазин")
@allure.feature("Оформление заказа")
@allure.severity("blocker")
@allure.title("Тест оформления заказа")
@allure.description("Проверяем процесс покупки товаров от добавления"
                    " в корзину до оформления заказа.")
def test_shop(browser):
    """
    Тестирует процесс оформления заказа.

    Args:
        browser: WebDriver для тестов.
    """
    shop = ShopPage(browser)

    with allure.step("Открываем сайт магазина"):
        shop.open_site("https://www.saucedemo.com/")

    with allure.step("Авторизуемся"):
        shop.login("standard_user", "secret_sauce")

    with allure.step("Добавляем товары в корзину"):
        products_to_add = [
            "add-to-cart-sauce-labs-backpack",
            "add-to-cart-sauce-labs-bolt-t-shirt",
            "add-to-cart-sauce-labs-onesie",
        ]
        shop.add_products_to_cart(products_to_add)

    with allure.step("Переходим в корзину"):
        shop.go_to_cart()

    with allure.step("Начинаем оформление заказа"):
        shop.checkout()

    with allure.step("Заполняем форму оформления заказа"):
        shop.fill_checkout_form("Oleg", "K", "20150")

    with allure.step("Проверяем итоговую сумму"):
        total_text = shop.get_total_label()
        expected_total = "Total: $58.29"
        assert total_text == expected_total, \
            f"Ожидалось '{expected_total}', но получено '{total_text}'"
