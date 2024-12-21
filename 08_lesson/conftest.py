import pytest


@pytest.fixture(scope="session")
def base_url():
    return "https://ru.yougile.com/api-v2"
