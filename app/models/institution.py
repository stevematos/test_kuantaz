from config.database import Base
from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func


class Institution(Base):
    __tablename__ = "institution"

    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(255), nullable=False)
    description = Column(String(255), nullable=False)
    address = Column(String(255), nullable=False)
    created_at = Column(
        DateTime,
        nullable=False,
        default=func.now(),
        server_default=func.now(),
    )

    projects = relationship("Project", back_populates="institution")
