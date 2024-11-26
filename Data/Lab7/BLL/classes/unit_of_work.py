"""A utilization of the unit-of-work design principle"""
from dataclasses import dataclass
from Data.Lab7.DAL.classes.api_repository import ApiRepository


@dataclass
class UnitOfWork:
    """A class that utilizes the unit-of-work design principle"""
    def __init__(self, base_api_url):
        self.base_api_url = base_api_url
        self.posts = ApiRepository(f"{base_api_url}/posts")
        self.comments = ApiRepository(f"{base_api_url}/comments")
        self.albums = ApiRepository(f"{base_api_url}/albums")
        self.photos = ApiRepository(f"{base_api_url}/photos")
        self.todos = ApiRepository(f"{base_api_url}/todos")
        self.users = ApiRepository(f"{base_api_url}/users")
