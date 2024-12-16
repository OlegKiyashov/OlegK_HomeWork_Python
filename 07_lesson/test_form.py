from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from form_page import FormPage


def test_form_submission():
    driver = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()))
    page = FormPage(driver)

    try:
        # Open the page
        page.open()

        # Fill form fields
        page.fill_field("first-name", "Иван")
        page.fill_field("last-name", "Петров")
        page.fill_field("address", "Ленина, 55-3")
        page.fill_field("e-mail", "test@skypro.com")
        page.fill_field("phone", "+7985899998787")
        page.fill_field("zip-code", "")  # Оставляем пустым для проверки ошибки
        page.fill_field("city", "Москва")
        page.fill_field("country", "Россия")
        page.fill_field("job-position", "QA")
        page.fill_field("company", "SkyPro")

        # Submit the form
        page.submit_form()

        # Check zip code error background color
        zip_code_color = page.get_element_background_color('#zip-code')
        assert zip_code_color == "rgba(248, 215, 218, 1)", \
            (f"Цвет фона Zip Code: {zip_code_color} "
             f"(ожидалось rgba(248, 215, 218, 1))")

        # Check success alert background colors
        alert_success = page.get_alerts('div.alert.py-2.alert-success')
        for alert in alert_success:
            bg_color = alert.value_of_css_property("background-color")
            assert bg_color == "rgba(209, 231, 221, 1)", \
                (f"Цвет успешного сообщения: {bg_color}"
                 f" (ожидалось rgba(209, 231, 221, 1))")

    finally:
        driver.quit()


# Run test
if __name__ == "__main__":
    test_form_submission()
