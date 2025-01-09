import allure
from pages.form_page import FormPage


@allure.epic("Форма")
@allure.feature("Проверка валидации формы")
@allure.severity("major")
@allure.title("Тест валидации формы")
@allure.description("Проверяем отображение ошибок валидации формы.")
def test_form(browser):
    """
    Тестирует валидацию формы.

    Args:
        browser: WebDriver для тестов.
    """
    page = FormPage(browser)

    with allure.step("Открываем страницу"):
        page.open()

    with allure.step("Заполняем поля формы"):
        page.fill_field("first-name", "Иван")
        page.fill_field("last-name", "Петров")
        page.fill_field("address", "Ленина, 55-3")
        page.fill_field("e-mail", "test@skypro.com")
        page.fill_field("phone", "+7985899998787")
        page.fill_field("zip-code", "")  # Пустое поле для проверки ошибки
        page.fill_field("city", "Москва")
        page.fill_field("country", "Россия")
        page.fill_field("job-position", "QA")
        page.fill_field("company", "SkyPro")

    with allure.step("Закрываем всплывающее окно"):
        page.close_popup_if_exists()

    with allure.step("Отправляем форму"):
        page.submit_form()

    with allure.step("Проверяем цвет фона ошибки почтового индекса"):
        zip_code_color = page.get_element_background_color('#zip-code')
        assert zip_code_color == "rgba(248, 215, 218, 1)", \
            (f"Цвет фона Zip Code: {zip_code_color} "
             f"(ожидалось rgba(248, 215, 218, 1))")
