from config.database import db_session
from models import Project


@db_session
def get_all_projects(db):
    return db.query(Project).all()
