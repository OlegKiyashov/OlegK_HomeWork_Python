import os
import pytest
from project_api import ProjectAPI
from faker import Faker
from dotenv import load_dotenv

# Загрузка переменных окружения из файла .env
load_dotenv()

# Инициализация Faker для генерации случайных данных
fake = Faker()


@pytest.fixture
def api():
    # Использует базовый URL и токен из переменных окружения.
    base_url = os.getenv("BASE_URL")  # Базовый URL из .env файла
    token = os.getenv("API_TOKEN")  # Токен из .env файла
    return ProjectAPI(base_url, token)


@pytest.mark.parametrize("payload, expected_status", [
    ({"title": fake.catch_phrase()}, 201),
    # Валидный payload, ожидаемый статус 201
    ({}, 400),  # Пустой payload, ожидаемый статус 400
    ({"description": "Missing name"}, 400),
    # Payload без обязательного поля title, ожидаемый статус 400
])
def test_create_project(api, payload, expected_status):
    # Проверяет, что API возвращает ожидаемый статус ответа.

    response = api.create_project(payload)
    # Отправка запроса на создание проекта
    assert response.status_code == expected_status
    # Проверка статуса ответа


@pytest.mark.parametrize("payload", [
    {"title": fake.catch_phrase()},
    # Случайный валидный payload
    {"title": fake.catch_phrase()}
    # Еще один случайный валидный payload
])
def test_create_project_positive(api, payload):
    # Проверяет, что ответ содержит корректный ID.

    response = api.create_project(payload)
    # Отправка запроса на создание проекта
    assert response.status_code == 201
    # Успешный статус ответа

    response_data = response.json()
    # Парсинг ответа
    assert "id" in response_data, "Ответ не содержит 'id'"
    # Проверка наличия 'id'
    assert isinstance(response_data["id"], str), "'id' должен быть строкой"
    # Проверка типа 'id'
    assert response_data["id"], "'id' не должен быть пустым"
    # Проверка, что 'id' не пустой


@pytest.mark.parametrize("payload", [{}, {"description": "Missing name"}])
def test_create_project_negative(api, payload):
    # Проверяет, что API возвращает ошибку.

    response = api.create_project(payload)
    # Отправка запроса с некорректным payload
    assert response.status_code == 400
    # Ожидаемый статус ошибки


def test_get_projects(api):
    # Проверяет корректность структуры ответа.

    response = api.get_projects()
    # Запрос списка проектов
    assert response.status_code == 200
    # Успешный статус ответа

    response_data = response.json()
    # Парсинг ответа
    assert isinstance(response_data, dict), "Ответ должен быть словарем"
    # Проверка структуры
    assert "content" in response_data, "Ответ должен содержать 'content'"
    # Проверка наличия ключа
    assert isinstance(response_data["content"], list), \
        "'content' должен быть списком"
    # Проверка типа данных

    # Если есть проекты, проверяем их структуру
    if response_data["content"]:
        project = response_data["content"][0]
        assert "id" in project, "Проект должен содержать 'id'"
        assert "title" in project, "Проект должен содержать 'title'"


def test_update_project_positive(api):
    # Создает проект, а затем проверяет, что он может быть обновлен.

    create_response = api.create_project({"title": "Update Test"})
    # Создание проекта
    response_json = create_response.json()
    project_id = response_json.get("id")
    # Получение ID созданного проекта

    if not project_id:
        raise ValueError(f"ID не найден в ответе: {response_json}")
        # Ошибка, если ID отсутствует


def test_update_project_negative(api):
    # Проверяет, что попытка обновить проект с
    # некорректным ID возвращает ошибку.

    response = api.update_project("invalid_id",
                                  {"name": "Updated Name"})
    # Некорректный ID
    assert response.status_code == 400
    # Ожидаемый статус ошибки


def test_get_project_positive(api):
    # Создает проект, а затем проверяет, что его можно получить по ID.

    create_response = api.create_project({"title": "Single Project Test"})
    # Создание проекта
    assert create_response.status_code == 201, \
        f"Не удалось создать проект, статус: {create_response.status_code}"

    response_json = create_response.json()
    project_id = response_json.get("id")
    # Извлечение ID созданного проекта

    if not project_id:
        raise ValueError(f"ID не найден в ответе: {response_json}")
        # Ошибка, если ID отсутствует


def test_get_project_negative(api):
    # Проверяет, что запрос с некорректным ID возвращает ошибку 404.

    response = api.get_project("invalid_id")
    # Некорректный ID
    assert response.status_code == 404
    # Ожидаемый статус ошибки
