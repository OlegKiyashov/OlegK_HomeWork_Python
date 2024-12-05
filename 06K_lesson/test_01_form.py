from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService


def wait_of_element_located(css, driver):
    element = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, css)
        )
    )
    return element


def click_element(css, driver):
    # Ждем, пока элемент станет доступным для нажатия
    element = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, css))
    )

    # Прокручиваем в область видимости, если элемент скрыт
    driver.execute_script("arguments[0].scrollIntoView(true);", element)

    # Нажимаем по элементу
    driver.execute_script("arguments[0].click();", element)


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager()
                                                .install()))
driver.get('https://bonigarcia.dev/selenium-webdriver-java/data-types.html')

# Находит элементы и сохраняет их в переменные.
first_name = wait_of_element_located(css='[name="first-name"]', driver=driver)
last_name = wait_of_element_located(css='[name="last-name"]', driver=driver)
address = wait_of_element_located(css='[name="address"]', driver=driver)
e_mail = wait_of_element_located(css='[name="e-mail"]', driver=driver)
phone = wait_of_element_located(css='[name="phone"]', driver=driver)
zip_code = wait_of_element_located(css='[name="zip-code"]', driver=driver)
city = wait_of_element_located(css='[name="city"]', driver=driver)
country = wait_of_element_located(css='[name="country"]', driver=driver)
job_position = wait_of_element_located(css='[name="job-position"]',
                                       driver=driver)
company = wait_of_element_located(css='[name="company"]', driver=driver)

# Заполнение полей
first_name.send_keys('Иван')
last_name.send_keys('Петров')
address.send_keys('Ленина, 55-3')
e_mail.send_keys('test@skypro.com')
phone.send_keys('+7985899998787')
zip_code.send_keys()
city.send_keys('Москва')
country.send_keys('Россия')
job_position.send_keys('QA')
company.send_keys('SkyPro')

# Нажатие по кнопке submit
click_element(css='[type="submit"]', driver=driver)


# Проверка фона при ошибке
def test_alert_danger():
    zip_code_color = (wait_of_element_located
                      (css='#zip-code', driver=driver)
                      .value_of_css_property("background-color"))
    assert zip_code_color == "rgba(248, 215, 218, 1)"


test_alert_danger()


# Проверка фона при успешной отправке данных
def test_alert_success():
    alert_success = driver.find_elements(By.CSS_SELECTOR,
                                         'div.alert.py-2.alert-success')
    for form in alert_success:
        assert (form.value_of_css_property("background-color")
                == "rgba(209, 231, 221, 1)")


test_alert_success()
