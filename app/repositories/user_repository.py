from sqlalchemy.orm import Session

from app.models.user import User


class UserRepository:

    @staticmethod
    def create(
        db: Session,
        username: str,
        email: str,
        password: str
    ):
        user = User(
            username=username,
            email=email,
            password=password
        )

        db.add(user)
        db.commit()
        db.refresh(user)

        return user

    @staticmethod
    def get_all(db: Session):
        return db.query(User).all()

    @staticmethod
    def get_by_id(
        db: Session,
        user_id: int
    ):
        return (
            db.query(User)
            .filter(User.id == user_id)
            .first()
        )

    @staticmethod
    def delete(
        db: Session,
        user: User
    ):
        db.delete(user)
        db.commit()

    @staticmethod
    def get_by_email(
        db: Session,
        email: str
    ):
        return (
            db.query(User)
            .filter(User.email == email)
            .first()
        )