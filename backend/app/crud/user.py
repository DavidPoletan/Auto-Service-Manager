from sqlalchemy.orm import Session
from backend.app.models.user import User
from backend.app.schemas.user import UserCreate, UserUpdate

def get_user(db: Session, id: int):
    return db.get(User, id)


def get_all_users(db: Session):
    return db.query(User).all()


def create_user(db: Session, user: UserCreate):
    db_user = UserCreate(
        username=user.username,
        email=user.email,
        password_hash=user.password_hash,
        first_name=user.first_name,
        last_name=user.last_name,
        role=user.role,
        active=user.active
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


def update_user(db: Session, id: int, user: UserUpdate):
    db_user = db.get(User, id)

    if db_user is None:
        return None

    for field, value in user.model_dump(exclude_unset=True, exclude={"updated_at"}).items():
        setattr(db_user, field, value)

    db.commit()
    db.refresh(db_user)

    return db_user


def delete_user(db: Session, id: int):
    db_user = db.get(User, id)

    if db_user is None:
        return False

    db.delete(db_user)
    db.commit()

    return True