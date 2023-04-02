from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.exceptions import UserNotFoundException
from app.schemas.users import User, UserCreate, UserUpdate
from app.crud.crud_user import get_user, get_users, create_user, update_user, delete_user

router = APIRouter()

@router.get("/", response_model=list[User])
async def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(SessionLocal)):
    users = get_users(db, skip=skip, limit=limit)
    return users

@router.get("/{user_id}", response_model=User)
async def read_user(user_id: int, db: Session = Depends(SessionLocal)):
    user = get_user(db, user_id=user_id)
    if not user:
        raise UserNotFoundException(user_id)
    return user

@router.post("/", response_model=User)
async def create_user(user: UserCreate, db: Session = Depends(SessionLocal)):
    db_user = create_user(db, user)
    return db_user

@router.put("/{user_id}", response_model=User)
async def update_user(user_id: int, user_update: UserUpdate, db: Session = Depends(SessionLocal)):
    db_user = get_user(db, user_id=user_id)
    if not db_user:
        raise UserNotFoundException(user_id)
    updated_user = update_user(db, db_user, user_update)
    return updated_user

@router.delete("/{user_id}")
async def delete_user(user_id: int, db: Session = Depends(SessionLocal)):
    db_user = get_user(db, user_id=user_id)
    if not db_user:
        raise UserNotFoundException(user_id)
    delete_user(db, db_user)
    return {"message": "User deleted successfully"}
