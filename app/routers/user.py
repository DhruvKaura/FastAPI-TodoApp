from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate, UserResponse, EditUser

router = APIRouter(
prefix="/users",
tags=["Users"]
)

@router.post("/", response_model=UserResponse)
def create_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    return UserRepository.create(
    db=db,
    username=user.username,
    email=user.email,
    password=user.password
)

@router.get("/", response_model=List[UserResponse])
def get_users(
    db: Session = Depends(get_db)
):
    return UserRepository.get_all(db)

@router.get("/{user_id}", response_model=UserResponse)
def get_user(
    user_id: int,
    db: Session = Depends(get_db)
):
    user = UserRepository.get_by_id(db, user_id)

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )
    return user


@router.put("/{user_id}", response_model=UserResponse)
def update_user(
    user_id: int,
    user_data: EditUser,
    db: Session = Depends(get_db)
):
    user = UserRepository.get_by_id(db, user_id)

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )
    user.username = user_data.username
    user.email = user_data.email

    db.commit()
    db.refresh(user)
    return user


@router.delete("/{user_id}")
def delete_user(
    user_id: int,
    db: Session = Depends(get_db)
):
    user = UserRepository.get_by_id(db, user_id)


    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )
    UserRepository.delete(db, user)

    return {
        "message": "User deleted successfully"
    }
