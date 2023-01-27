from config.environment import (
    DATABASE_DIALECT,
    DATABASE_HOSTNAME,
    DATABASE_NAME,
    DATABASE_PASSWORD,
    DATABASE_PORT,
    DATABASE_USERNAME,
    DEBUG_MODE,
)
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool

if DATABASE_DIALECT == "sqlite":
    DATABASE_URL = f"sqlite:///./{DATABASE_NAME}.db"
else:
    DATABASE_URL = (
        f"{DATABASE_DIALECT}://{DATABASE_USERNAME}:"
        f"{DATABASE_PASSWORD}@{DATABASE_HOSTNAME}:"
        f"{DATABASE_PORT}/{DATABASE_NAME}"
    )


# Create Database Engine
Engine = create_engine(DATABASE_URL, echo=DEBUG_MODE, future=True, poolclass=NullPool)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=Engine)

Base = declarative_base()


def db_session(f):
    def with_session_(*args, **kwargs):
        with SessionLocal() as session:
            return f(session, *args, **kwargs)

    return with_session_


def init_db():
    from models import Institution, Project, User  # noqa: F401

    Base.metadata.create_all(bind=Engine)


@db_session
def dummy_data(db):
    from models import Institution, Project, User  # noqa: F401

    institution_1 = Institution(
        name="Institution 1", description="Description 1", address="Address 1"
    )

    user_1 = User(
        name="User 1",
        surname="Surname 1",
        age=28,
        rut="30.686.957-1",
        position="Position 1",
        date_of_birth="1994-02-24",
    )

    project_1 = Project(
        name="Project 1",
        start_date="2023-01-13",
        end_date="2023-01-21",
        user_id=1,
        institution_id=1,
    )

    project_2 = Project(
        name="Project 2",
        start_date="2023-01-03",
        end_date="2023-02-02",
        user_id=1,
        institution_id=1,
    )

    db.add(institution_1)
    db.add(user_1)
    db.add(project_1)
    db.add(project_2)
    db.commit()
