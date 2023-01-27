from config.database import Base
from sqlalchemy import Column, Date, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class Project(Base):
    __tablename__ = "project"

    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(255), nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    user_id = Column(Integer, ForeignKey("user.id"))
    institution_id = Column(Integer, ForeignKey("institution.id"))
    responsible_user = relationship("User", back_populates="projects")
    institution = relationship("Institution", back_populates="projects")
