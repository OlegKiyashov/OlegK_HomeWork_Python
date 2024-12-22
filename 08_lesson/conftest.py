import os
import pytest
from dotenv import load_dotenv
# Загружаем переменные из .env
load_dotenv()


@pytest.fixture(scope="session")
def base_url():
    return os.getenv("BASE_URL")
    # Берём BASE_URL из переменных окружения
