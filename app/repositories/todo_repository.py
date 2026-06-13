from sqlalchemy.orm import Session

from app.models.todo import Todo


class TodoRepository:

    @staticmethod
    def create(
        db: Session,
        title: str,
        user_id: int
    ):
        todo = Todo(
            title=title,
            user_id=user_id
        )

        db.add(todo)
        db.commit()
        db.refresh(todo)

        return todo

    @staticmethod
    def get_user_todos(
        db: Session,
        user_id: int
    ):
        return (
            db.query(Todo)
            .filter(Todo.user_id == user_id)
            .all()
        )