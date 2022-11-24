from sqlalchemy.orm import Session

from db.models.course import Course

def get_courses(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Course).all()