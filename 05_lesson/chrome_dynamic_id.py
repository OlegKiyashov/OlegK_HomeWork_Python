from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time  # Для добавления задержек


# Функция для выполнения одного запуска
def run_script():
    # Настройка драйвера
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # Шаг 1: Открыть страницу
    driver.get("http://uitestingplayground.com/dynamicid")

    # Задержка для ожидания загрузки страницы
    time.sleep(1)

    # Шаг 2: Кликнуть на синюю кнопку
    driver.find_element(By.XPATH, "//button[contains(text("
                                  "),'Button with Dynamic ID')]").click()

    # Шаг 3: Вывести сообщение в консоль
    print("Клик по синей кнопке выполнен успешно")

    # Закрыть браузер
    driver.quit()


# Запуск скрипта 3 раза
for i in range(3):
    print(f"Запуск #{i + 1}")
    run_script()
    # Задержка между запусками (опционально)
    time.sleep(1)
