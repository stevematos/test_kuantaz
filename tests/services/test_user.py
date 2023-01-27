from unittest.mock import patch

from models import User
from schemas.user import UserGetSchema
from services.user import read_all_users
from datetime import date


@patch("services.user.get_all_users")
def test_read_all_users(mock_get_all_users):

    list_users = [
        User(
            id=1,
            name="User 1",
            surname="Surname 1",
            age=27,
            date_of_birth=date(1994, 2, 24),
            position="Position 1",
        ),
        User(
            id=1,
            name="User 2",
            surname="Surname 2",
            age=25,
            date_of_birth=date(1996, 2, 12),
            position="Position 2",
        )
    ]

    mock_get_all_users.return_value = list_users

    schema = UserGetSchema(many=True)
    expected = schema.dump(list_users)

    result = read_all_users()

    assert result == expected

