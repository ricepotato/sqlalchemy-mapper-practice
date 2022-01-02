from models import User


def test_user_create():
    user = User(name="sukjun.sagong", email="ricepotato40@gmail.com")
    assert user

    user = User("sukjun.sagong", "ricepotato40@gmail.com")
    assert user
