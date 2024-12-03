from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
import time  # Для добавления задержек

# Настройка браузера
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

# Открытие страницы
driver.get("http://the-internet.herokuapp.com/inputs")

# Задержка перед взаимодействием с полем ввода
time.sleep(1)

# Поиск поля ввода
input_field = driver.find_element(By.TAG_NAME, "input")

# Ввод данных с задержками
input_field.send_keys("1000")
time.sleep(1)  # Задержка перед очисткой поля
input_field.clear()
time.sleep(1)  # Задержка перед вводом новых данных
input_field.send_keys("999")

# Вывод результата в консоль
print("Данные успешно введены")

# Задержка перед завершением
time.sleep(1)

# Закрытие браузера
driver.quit()
