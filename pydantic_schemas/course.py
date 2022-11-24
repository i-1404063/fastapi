from pydantic import BaseModel

class CourseBase(BaseModel):
    title: str
    user_id: int


class CourseCreate(CourseBase):
    ...

class Course(CourseBase):
    title: str

    class Config:
        orm_mode = True        