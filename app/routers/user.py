from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.models.user import User
from app.schemas.user import UserCreate, UserResponse



router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.get("/")
def get_users():
    return {
        "message": "Get all users"
    }


@router.post("/", response_model=UserResponse)
def create_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    
    db_user = User(
        username=user.username,
        email=user.email,
        password=user.password
    )

    db.add(db_user)

    db.commit()

    db.refresh(db_user)

    return db_user