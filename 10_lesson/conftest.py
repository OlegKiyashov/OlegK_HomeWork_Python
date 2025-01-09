import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="session")
def browser():
    """
    Фикстура для инициализации браузера.

    Yields:
        WebDriver: Объект браузера.
    """
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().
                                                    install()))
    yield driver
    driver.quit()
