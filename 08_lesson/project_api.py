import requests


class ProjectAPI:

    def __init__(self, base_url, token):
        # Инициализация класса ProjectAPI.
        if not base_url:
            raise ValueError("Необходимо указать базовый URL.")
        self.BASE_URL = base_url  # Сохраняем базовый URL
        self.headers = {
            "Authorization": f"Bearer {token}",
            # Добавляем токен в заголовок Authorization
            "Content-Type": "application/json",
            # Указываем формат отправляемых данных
        }

    def create_project(self, payload):
        # Создание нового проекта.

        url = f"{self.BASE_URL}/projects"  # Формируем URL для создания проекта
        response = requests.post(url, headers=self.headers, json=payload)
        # Отправляем POST-запрос
        return response

    def get_projects(self):
        # Получение списка всех проектов.

        return requests.get(f"{self.BASE_URL}/projects", headers=self.headers)
        # GET-запрос к API

    def update_project(self, project_id, payload):
        # Обновление данных проекта.

        return requests.put(
            f"{self.BASE_URL}/projects/{project_id}",
            # Формируем URL с ID проекта
            json=payload,  # Передаем данные для обновления
            headers=self.headers,  # Указываем заголовки
        )

    def get_project(self, project_id):
        # Получение данных одного проекта по его ID.

        return requests.get(
            f"{self.BASE_URL}/projects/{project_id}",
            # Формируем URL с ID проекта
            headers=self.headers,  # Указываем заголовки
        )
