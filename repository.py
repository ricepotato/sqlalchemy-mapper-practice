from typing import List
from abc import abstractmethod
from sqlalchemy.orm.session import Session
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

    @abstractmethod
    def delete_user_by_id(self, user_id: int) -> bool:
        pass


class SqlalchemyRepository(Repository):
    def __init__(self, session: Session):
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

    def delete_user_by_id(self, user_id: int) -> bool:
        return self.session.query(User).filter(User.id == user_id).delete() == 1

    def delete_user(self, user: User) -> bool:
        self.session.delete(user)
        return True
