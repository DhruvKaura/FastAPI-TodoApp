from pydantic import BaseModel, EmailStr
from datetime import datetime

from app.database.database import get_db
from app.models.user import User


class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    created_at: datetime

    class Config:
        from_attributes = True

class EditUser(BaseModel):
    username: str
    email: EmailStr