from sqlalchemy.orm import Session
from fastapi import HTTPException

from db.models.user import User, Profile
from pydantic_schemas.user import UserCreate
from pydantic_schemas.profile import ProfileCreate


def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()  

def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(User).offset(skip).limit(limit).all()      

def create_user(db: Session, user: UserCreate):
    db_user = User(email=user.email, role=user.role)  
    db.add(db_user) #adding db_user to queue
    db.commit() 
    db.refresh(db_user)
    return db_user


def user_delete(id: int, db: Session):
    user = db.query(User).get(id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    db.delete(user)
    db.commit()    
    return user



def get_profile(db: Session, user_id: int):
    return db.query(Profile).filter(Profile.user_id == user_id).first()  


def create_profile(db: Session, user: ProfileCreate):
    mapped_user = Profile(**{
        k: v for k, v in user.__dict__.items()
        if v is not None
    })

    db.add(mapped_user)
    db.commit()
    db.refresh(mapped_user)

    return mapped_user
