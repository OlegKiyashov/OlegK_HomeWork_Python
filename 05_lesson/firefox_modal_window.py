from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
import time  # Для добавления задержки

# Настройка браузера
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

# Открытие страницы
driver.get("http://the-internet.herokuapp.com/entry_ad")

# Задержка 1 секунда перед закрытием модального окна
time.sleep(1)

# Закрытие модального окна
driver.find_element(By.XPATH,
                    "//div[@class='modal-footer']/p[text()='Close']").click()

# Задержка 1 секунда после закрытия окна
time.sleep(1)

# Вывод сообщения в консоль
print("Модальное окно закрыто")

# Закрытие браузера
driver.quit()
