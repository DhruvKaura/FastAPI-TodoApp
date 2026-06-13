from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.core.security import get_current_user

from app.repositories.todo_repository import TodoRepository

from app.schemas.todo import (
    TodoCreate,
    TodoResponse
)

router = APIRouter(
    prefix="/todos",
    tags=["Todos"]
)

@router.post(
    "/",
    response_model=TodoResponse
)
def create_todo(
    todo: TodoCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    return TodoRepository.create(
        db=db,
        title=todo.title,
        user_id=current_user.id
    )


@router.get(
    "/",
    response_model=List[TodoResponse]
)
def get_my_todos(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    return TodoRepository.get_user_todos(
        db,
        current_user.id
    )