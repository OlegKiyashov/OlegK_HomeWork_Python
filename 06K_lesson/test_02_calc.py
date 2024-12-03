from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_calculator():
    # Инициализация драйвера
    driver = webdriver.Chrome()

    try:
        # Шаг 1: Открываем страницу
        driver.get("https://bonigarcia.dev/selenium-webdriver-java"
                   "/slow-calculator.html")

        # Шаг 2: Вводим значение 45 в поле с локатором #delay
        delay_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#delay"))
        )
        delay_input.clear()
        delay_input.send_keys("45")

        # Шаг 3: Прокручиваем страницу до кнопки "="
        equals_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//span[text()="="]'))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);",
                              equals_button)

        # Шаг 4: Нажимаем кнопки 7, +, 8, =
        button_7 = driver.find_element(By.XPATH, '//span[text()="7"]')
        button_plus = driver.find_element(By.XPATH, '//span[text()="+"]')
        button_8 = driver.find_element(By.XPATH, '//span[text()="8"]')

        # Нажимаем кнопки
        button_7.click()
        button_plus.click()
        button_8.click()
        equals_button.click()

        # Шаг 5: Ожидаем появления результата и проверяем его
        WebDriverWait(driver, 60).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR,
                                              ".screen"), "15")
        )

        # Проверяем текст результата
        screen = driver.find_element(By.CSS_SELECTOR, ".screen")
        assert screen.text == "15", (f"Ожидался результат '15',"
                                     f" но найден '{screen.text}'")

        print("Тест прошел успешно!")

    finally:
        # Закрываем браузер после выполнения теста
        driver.quit()
