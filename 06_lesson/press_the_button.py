
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Настройка WebDriver
driver = webdriver.Chrome()

try:
    # Шаг 1: Перейти на страницу
    driver.get("http://uitestingplayground.com/ajax")

    # Шаг 2: Нажать на синюю кнопку
    blue_button = driver.find_element(By.CSS_SELECTOR, "button#ajaxButton")
    blue_button.click()

    # Шаг 3: Ожидать появления зеленой плашки и получить текст
    green_banner = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR,
                                          "div#content > p.bg-success"))
    )
    print(green_banner.text)  # Ожидаемый текст:
    # "Data loaded with AJAX get request."

finally:
    # Закрыть браузер
    driver.quit()