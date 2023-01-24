from config.database import Base

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey


class Project(Base):
    __tablename__ = "project"

    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(255), nullable=False)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=False)
    user_id = Column(Integer, ForeignKey("user.id"))
    institution_id = Column(Integer, ForeignKey("institution.id"))