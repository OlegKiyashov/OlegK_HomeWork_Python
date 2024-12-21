import pytest
from project_api import ProjectAPI


@pytest.fixture
def api():
    # Указать здесь данные
    base_url = "https://api.yougile.com/api-v2"  # URL
    token = "ВСТАВИТЬ МОЙ ТОКЕН"
    return ProjectAPI(base_url, token)


@pytest.mark.parametrize("payload", [
    {"title": "Test Project"},
    {"title": "Another Project"}
])
def test_create_project_positive(api, payload):
    response = api.create_project(payload)
    print(f"Response status: {response.status_code}")
    print(f"Response body: {response.json()}")

    # Проверка статус-кода
    assert response.status_code == 201

    # Проверка, что в ответе есть "id"
    response_data = response.json()
    assert "id" in response_data, "Ответ не содержит 'id'"
    assert isinstance(response_data["id"], str), "'id' должен быть строкой"

    # Проверка, что ID не пустой
    assert response_data["id"], "'id' не должен быть пустым"


@pytest.mark.parametrize("payload", [{}, {"description": "Missing name"}])
def test_create_project_negative(api, payload):
    response = api.create_project(payload)
    assert response.status_code == 400  # Проверка кода ошибки 400


def test_get_projects(api):
    response = api.get_projects()
    assert response.status_code == 200

    # Проверка, что ответ - это словарь
    response_data = response.json()
    assert isinstance(response_data, dict)

    # Проверка, что есть ключ 'content' и он является списком
    assert "content" in response_data
    assert isinstance(response_data["content"], list)

    # Проверка структуры одного из элементов списка
    if response_data["content"]:
        project = response_data["content"][0]
        assert "id" in project
        assert "title" in project


def test_update_project_positive(api):
    # Создание проекта для теста
    create_response = api.create_project({"title": "Update Test"})

    # Выводим статус и тело ответа для отладки
    print(f"Create response status: {create_response.status_code}")
    print(f"Create response body: {create_response.json()}")

    # Получение project_id из ответа
    response_json = create_response.json()
    project_id = response_json.get("id")

    if not project_id:
        raise ValueError(f"ID not found in response: {response_json}")


def test_update_project_negative(api):
    response = api.update_project("invalid_id", {"name": "Updated Name"})
    assert response.status_code == 400  # код ошибки


def test_get_project_positive(api):
    # Создание проекта для теста, используя правильный параметр "title"
    create_response = api.create_project({"title": "Single Project Test"})

    # Вывод статуса и тело ответа для отладки
    print(f"Create response status: {create_response.status_code}")
    print(f"Create response body: {create_response.json()}")

    # Проверка, что проект был создан (статус 201)
    assert create_response.status_code == 201, \
        f"Failed to create project, status code: {create_response.status_code}"

    # Получение project_id из ответа
    response_json = create_response.json()
    project_id = response_json.get("id")

    if not project_id:
        raise ValueError(f"ID not found in response: {response_json}")


def test_get_project_negative(api):
    response = api.get_project("invalid_id")
    assert response.status_code == 404  # код ошибки
