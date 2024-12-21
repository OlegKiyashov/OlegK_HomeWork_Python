import requests


class ProjectAPI:
    def __init__(self, base_url, token):
        self.BASE_URL = base_url
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        }

    def create_project(self, payload):
        url = f"{self.BASE_URL}/projects"
        response = requests.post(url, headers=self.headers, json=payload)
        return response

    def get_projects(self):
        return requests.get(f"{self.BASE_URL}/projects", headers=self.headers)

    def update_project(self, project_id, payload):
        return requests.put(f"{self.BASE_URL}/projects/{project_id}",
                            json=payload, headers=self.headers)

    def get_project(self, project_id):
        return requests.get(f"{self.BASE_URL}/projects/"
                            f"{project_id}", headers=self.headers)
