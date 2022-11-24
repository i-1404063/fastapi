from pydantic import BaseModel
from typing import Optional

class ProfileBase(BaseModel):
    username: str
    user_id: int
    bio: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None


class ProfileCreate(ProfileBase):
    ...


class Profile(BaseModel):
    id: int
    username: str

    class Config:
        orm_mode = True    

