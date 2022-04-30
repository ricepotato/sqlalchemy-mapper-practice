from dataclasses import dataclass
from typing import List


@dataclass
class Address:
    name: str
    address: str


@dataclass
class User:
    def __init__(self, name: str, email: str, addresses: List[Address] = []):
        self.name = name
        self.email = email
        self.addresses = addresses

    def __str__(self):
        return f"{self.name}, {self.email}"
