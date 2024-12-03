from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time  # Импортируем библиотеку для задержки

# Настройка драйвера Chrome
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Открытие страницы
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

# Добавление элементов с задержкой 1 секунда
for _ in range(5):
    driver.find_element(By.XPATH, "//button[text()='Add Element']").click()
    time.sleep(1)  # Задержка в 1 секунду после каждого клика

# Подсчет кнопок Delete
delete_buttons = driver.find_elements(By.XPATH, "//button[text()='Delete']")
print(f"Количество кнопок 'Delete': {len(delete_buttons)}")

# Закрытие браузера
driver.quit()
