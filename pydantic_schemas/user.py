from pydantic import BaseModel, validator
from datetime import datetime


class UserBase(BaseModel):
    email: str
    role: str 


class UserCreate(UserBase):

    @validator('email')
    def email_validation(cls, v):
        if v != "user2@gmail.com":
            raise ValueError('Value must be "user2@gmail.com"')

        return v    



class User(BaseModel):
    email: str
    role: str
    is_active: bool


    class Config:
        orm_mode = True
