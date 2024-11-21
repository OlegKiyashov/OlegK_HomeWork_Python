from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time  # Импортируем модуль time для использования sleep()

# Настройка браузера
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Открытие страницы
driver.get("http://uitestingplayground.com/dynamicid")

# Задержка 1 секунда перед кликом
time.sleep(1)

# Клик по кнопке
driver.find_element(By.XPATH, "//button[contains(text(),'Button with Dynamic ID')]").click()

# Задержка 1 секунда после клика
time.sleep(1)

# Вывод сообщения
print("Скрипт выполнен успешно")

# Закрытие браузера
driver.quit()
