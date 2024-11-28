from selenium import webdriver
from selenium.webdriver.common.by import By

# Настройка WebDriver
driver = webdriver.Chrome()

try:
    # Шаг 1: Перейти на сайт
    driver.get("http://uitestingplayground.com/textinput")

    # Шаг 2: Указать текст "SkyPro" в поле ввода
    input_field = driver.find_element(By.ID, "newButtonName")
    input_field.send_keys("SkyPro")

    # Шаг 3: Нажать на синюю кнопку
    blue_button = driver.find_element(By.ID, "updatingButton")
    blue_button.click()

    # Шаг 4: Получить текст кнопки и вывести в консоль
    button_text = blue_button.text
    print(button_text)  # Ожидаемый текст: "SkyPro"

finally:
    # Закрыть браузер
    driver.quit()
