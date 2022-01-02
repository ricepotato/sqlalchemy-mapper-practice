from abc import abstractmethod
from models import User


class Repository:
    @abstractmethod
    def add(self, obj) -> int:
        pass

    @abstractmethod
    def get_user(self, user_id: int) -> User:
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
