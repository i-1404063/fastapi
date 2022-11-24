from sqlalchemy.orm import relationship
from sqlalchemy import String, Integer, ForeignKey, Column, Text
from sqlalchemy_utils import URLType

from ..db_setup import Base
from .mixins import Timestamp


class Course(Timestamp,Base):
    title = Column(String(100), nullable=False)
    description = Column(Text, nullable=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
 
    created_by = relationship("User", back_populates="courses")

    def __repr__(self) -> str:
        return f"<Course {self.title}>"
