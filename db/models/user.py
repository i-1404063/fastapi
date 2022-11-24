import enum

from sqlalchemy.orm import relationship
from sqlalchemy import Boolean, String, Integer, ForeignKey, Enum, Column,Text

from ..db_setup import Base
from .mixins import Timestamp

# class syntax of Enum
class Role(str,enum.Enum):
    teacher = "teacher"
    student = "student"

# functional syntax of Enum 
# Role = enum.IntEnum('Role', ['teacher', 'student'])  
       

class User(Timestamp,Base):
    email = Column(String(100), unique=True, index=True, nullable=False)
    role = Column(Enum(Role))
    is_active = Column(Boolean, default=False)
    profile = relationship("Profile", cascade="all, delete-orphan", back_populates="owner", uselist=False)
    courses = relationship("Course", cascade="all, delete-orphan", back_populates="created_by", uselist=True)

    def __str__(self) -> str:
        return "{} {} {}\n".format(self.email, self.role, self.is_active)

class Profile(Timestamp,Base):
    username = Column(String(100), unique=True, nullable=False)
    first_name = Column(String(50), nullable=True)
    last_name = Column(String(50), nullable=True)
    bio = Column(Text, nullable=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)

    owner = relationship("User", back_populates="profile")
    
    def __str__(self) -> str:
        return "{}\n".format(self.username)