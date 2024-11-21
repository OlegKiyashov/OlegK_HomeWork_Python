from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time  # Импортируем модуль time для добавления задержки


# Функция для выполнения одного запуска
def run_script():
    # Настройка браузера
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # Открытие страницы
    driver.get("http://uitestingplayground.com/classattr")

    # Задержка 1 секунда перед выполнением клика
    time.sleep(1)

    # Поиск кнопки с классом 'btn-primary' и клик по ней
    driver.find_element(By.XPATH,
                        "//button[contains(@class,'btn-primary')]").click()

    # Задержка 1 секунда после клика
    time.sleep(1)

    # Вывод сообщения в консоль
    print("Клик по кнопке выполнен")

    # Закрытие браузера
    driver.quit()


# Запуск скрипта три раза
for i in range(3):
    print(f"Запуск #{i + 1}")
    run_script()
    # Задержка между запусками (опционально)
    time.sleep(2)
