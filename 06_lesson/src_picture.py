from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Настройка WebDriver
driver = webdriver.Chrome()

try:
    # Шаг 1: Перейти на сайт
    driver.get("https://bonigarcia.dev/selenium-webdriver-java"
               "/loading-images.html")

    # Шаг 2: Дождаться появления изображения с id "award"
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.ID, "award"))
    )

    # Шаг 3: Вывести значение атрибута src в консоль
    print(driver.find_element(By.ID, "award").get_dom_attribute("src"))

finally:
    # Закрыть браузер
    driver.quit()
