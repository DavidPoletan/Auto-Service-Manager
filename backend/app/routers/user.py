from fastapi import APIRouter, Depends, HTTPException, status
from typing import List, Optional
from sqlalchemy.orm import Session
from backend.app.database import get_db
from backend.app.schemas.user import User, UserCreate, UserUpdate
from backend.app.crud.user import (
    get_user,
    get_all_users,
    create_user,
    update_user,
    delete_user as delete_user_record
)

router = APIRouter()

@router.get("/user/{id}", response_model=User)
def read_user(id: int, db: Session = Depends(get_db)):
    user = get_user(db, id)

    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return user


@router.get("/", response_model=List[User])
def read_users(first_n: Optional[int] = None, db: Session = Depends(get_db)):
    users = get_all_users(db)
    return users[:first_n] if first_n else users


@router.post("/user/{id}", response_model=User)
def add_user(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)


@router.put("/user/{id}", response_model=User)
def put_user(id: int, user: UserUpdate, Session = Depends(get_db)):
    updated_user = update_user(db, id, user)

    if updated_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return updated_user


@router.delete("/user/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(id: int, db: Session = Depends(get_db)) -> None:
    deleted = delete_user_record(db, id)

    if not deleted:
        raise HTTPException(status_code=404, detail="User not found")