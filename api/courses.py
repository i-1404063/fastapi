from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from api.utils.course import get_courses
from pydantic_schemas.course import Course

from typing import List
from db.db_setup import get_db


router = APIRouter(
    prefix="/courses",
    tags=["courses"],
    responses={ 404: { "description": "Not found." }, 201: { "description": "Successfully Created." } }
)

@router.get("/", response_model=List[Course])
async def get_all_courses(db: Session = Depends(get_db)):
    courses = get_courses(db=db)

    return courses

