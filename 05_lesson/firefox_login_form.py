from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
import time  # Для добавления задержек

# Настройка Firefox через webdriver_manager
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

# Открываем страницу
driver.get("http://the-internet.herokuapp.com/login")

# Задержка перед вводом данных
time.sleep(1)

# Вводим данные в поля
driver.find_element(By.ID, "username").send_keys("tomsmith")
time.sleep(1)  # Задержка перед вводом пароля
driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
time.sleep(1)  # Задержка перед нажатием на кнопку

# Нажимаем на кнопку отправки
driver.find_element(By.XPATH, "//button[@type='submit']").click()

# Задержка перед завершением
time.sleep(1)

print("Форма авторизации отправлена")

# Закрываем браузер
driver.quit()
