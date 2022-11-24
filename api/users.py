from fastapi import APIRouter, Path, Depends, Header, HTTPException
from typing import List, Union
from sqlalchemy.orm import Session

from api.utils.user import get_user, get_user_by_email, get_users, create_user, get_profile, create_profile, user_delete
from pydantic_schemas.user import User, UserCreate
from pydantic_schemas.profile import Profile, ProfileCreate
from db.db_setup import get_db


db = get_db()

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={ 404: { "description": "Not found." } }
);


@router.get('/', response_model= List[User])
async def read_users(db: Session = Depends(get_db), skip: int = 0, limit: int = 10):
    users = get_users(db, skip, limit)
    return users    

@router.post('/', response_model=User)  
async def create_new_user(user:UserCreate, db: Session = Depends(get_db)):
    new_user = create_user(db, user)
    return new_user


@router.get('/{id}', response_model=User)
async def read_user(id: int = Path(..., description="Id of the user."), db: Session = Depends(get_db)):
    user = get_user(db, id)
    return user

@router.get('/user-email/')
async def read_user_by_email(email: str, db: Session = Depends(get_db)):
    if email:
        user = get_user_by_email(db, email)
        if user:
            return user

        return { "message": "User could not found." }    
                

    return { "message": "Internal Server Error." } 


@router.delete('/{id}')
async def delete_user(id: int = Path(..., description="Id of the user to be deleted"), db: Session = Depends(get_db)):
    user = user_delete(id, db) 
    if user:
        return { "message": "User Deletion Successful." }

    return { "message": "User with the given id not found." }                   


@router.get("/profile/{id}", response_model=Profile)
async def get_user_profile(id: int = Path(..., description="user profile id"), db: Session = Depends(get_db)):
    profile = get_profile(db, user_id=id)
    if profile is None:
        raise HTTPException(status_code=404, detail="User with the given id doesn't exist.")

    return profile 

@router.post('/profile')
async def create_user_profile(user: ProfileCreate, db: Session = Depends(get_db)):
    profile = create_profile(db, user)   
    if profile is None:
        raise HTTPException(status_code=500, detail="Internal Server Error.")

    return profile     



