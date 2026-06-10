from sqlalchemy.orm import Session
from app.models.user import User


class UserRepository:

    @staticmethod
    def get_all(db: Session):
        return db.query(User).all()

    @staticmethod
    def get_by_id(db: Session, user_id: int):
        return db.query(User).filter(
            User.id == user_id
        ).first()