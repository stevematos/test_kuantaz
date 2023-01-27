from config.exceptions import UserNotFound
from queries.user import get_all_users, get_user_by_rut
from schemas.user import UserGetSchema
from sqlalchemy.exc import NoResultFound


def read_all_users() -> list[dict]:
    schema = UserGetSchema(many=True)
    return schema.dump(get_all_users())


def read_user_by_rut(rut: str) -> list[dict]:
    try:
        user = get_user_by_rut(rut, is_dump=True)
    except NoResultFound:
        raise UserNotFound()

    return user
