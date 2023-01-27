from config.database import db_session
from models import User
from schemas.user import UserFullGetSchema


@db_session
def get_all_users(db):
    return db.query(User).all()


@db_session
def get_user_by_rut(db, rut: str, is_dump: bool = False):
    user = db.query(User).filter(User.rut == rut).one()

    if is_dump:
        schema = UserFullGetSchema()
        user = schema.dump(user)

    return user
