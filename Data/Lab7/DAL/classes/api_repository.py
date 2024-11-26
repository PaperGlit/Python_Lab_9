"""Utilizes the repository design principle"""
import requests
from Data.Lab7.DAL.classes.repository import Repository


class ApiRepository(Repository):
    """A class that utilizes the repository design principle"""
    def __init__(self, base_url):
        self.base_url = base_url

    def get_all(self):
        """Performs a GET-ALL request"""
        response = requests.get(self.base_url, timeout=10)
        response.raise_for_status()
        return response.json()

    def get_by_id(self, entity_id):
        """Performs a GET-BY request"""
        response = requests.get(f"{self.base_url}/{entity_id}", timeout=10)
        response.raise_for_status()
        return response.json()

    def add(self, data):
        """Performs a POST request"""
        response = requests.post(self.base_url, json=data, timeout=10)
        response.raise_for_status()
        return response.json()

    def update(self, entity_id, data):
        """Performs a PATCH request"""
        response = requests.patch(f"{self.base_url}/{entity_id}", json=data, timeout=10)
        response.raise_for_status()
        return response.json()

    def delete(self, entity_id):
        """Performs a DELETE request"""
        response = requests.delete(f"{self.base_url}/{entity_id}", timeout=10)
        response.raise_for_status()
        return response.ok
