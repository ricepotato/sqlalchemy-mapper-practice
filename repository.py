from typing import List
from abc import abstractmethod
from models import Address, User


class Repository:
    @abstractmethod
    def add(self, obj) -> int:
        pass

    @abstractmethod
    def get_user(self, user_id: int) -> User:
        pass

    @abstractmethod
    def get_users(self) -> List[User]:
        pass


class SqlalchemyRepository(Repository):
    def __init__(self, session):
        self.session = session

    def add(self, obj) -> int:
        self.session.add(obj)
        self.session.flush()
        return obj.id

    def get_user(self, user_id) -> User:
        return self.session.query(User).filter(User.id == user_id).one()

    def get_users(self) -> List[User]:
        return self.session.query(User).all()

    def get_addresses(self) -> List[Address]:
        return self.session.query(Address).all()

    def get_addresses_by_user(self, user: User) -> List[Address]:
        return self.session.query(Address).filter(Address.user_id == user.id).all()
