from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Настройка WebDriver
driver = webdriver.Chrome()

try:
    # Шаг 1: Перейти на страницу
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

    # Шаг 2: Ожидать появления текста "Done!" в элементе с id="text", что указывает на завершение загрузки картинок
    WebDriverWait(driver, 30).until(
        EC.text_to_be_present_in_element((By.ID, "text"), "Done!")
    )

    # Шаг 3: Найти все картинки на странице
    images = driver.find_elements(By.TAG_NAME, "img")

    # Проверка, есть ли хотя бы 3 картинки
    if len(images) >= 3:
        # Шаг 4: Получить атрибут src у 3-й картинки
        third_image_src = images[3].get_attribute("src")

        # Вывести значение атрибута src третьей картинки в консоль
        print("Значение атрибута 'src' у 3-й картинки:", third_image_src)
    else:
        print("На странице меньше 3-х картинок.")

finally:
    # Закрыть браузер
    driver.quit()
