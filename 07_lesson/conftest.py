import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="session")
def browser():
    """Инициализация браузера для сессии."""
    driver = webdriver.Chrome(service=ChromeService
                              (ChromeDriverManager().install()))
    yield driver
    driver.quit()  # Закрытие браузера после выполнения всех тестов
