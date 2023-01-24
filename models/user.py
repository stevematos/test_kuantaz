from config.database import Base

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(255), nullable=False)
    surname = Column(String(255), nullable=False)
    age = Column(Integer, nullable=False)
    RUT = Column(String(25), nullable=False)
    position = Column(String(25), nullable=False)
    date_of_birth = Column(DateTime, nullable=False)

    projects = relationship('project', backref='user')