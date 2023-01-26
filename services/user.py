from config.exceptions import UserNotFound
from queries.user import get_user_by_rut, get_all_users
from sqlalchemy.exc import NoResultFound

from schemas.user import UserGetSchema


def read_all_users() -> list[dict]:
    schema = UserGetSchema(many=True)
    return schema.dump(get_all_users())


def read_user(rut: str) -> list[dict]:
    try:
        user = get_user_by_rut(rut, is_dump=True)
    except NoResultFound:
        raise UserNotFound()

    return user
