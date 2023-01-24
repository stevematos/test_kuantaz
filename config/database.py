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
# from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base



if DATABASE_DIALECT == "sqlite":
    DATABASE_URL = f"sqlite:///./{DATABASE_NAME}.db"
else:
    DATABASE_URL = (
        f"{DATABASE_DIALECT}://{DATABASE_USERNAME}:"
        f"{DATABASE_PASSWORD}@{DATABASE_HOSTNAME}:"
        f"{DATABASE_PORT}/{DATABASE_NAME}"
    )


# Create Database Engine
Engine = create_engine(DATABASE_URL, echo=DEBUG_MODE, future=True)

# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=Engine)

Base = declarative_base()


def init_db():
    from models import Institution, Project, User
    Base.metadata.create_all(bind=Engine)