from uuid import uuid4, UUID
from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.database import engine, Base
from app.models import User
from app.schemas import CreateUser
from app.repositories import user_repository

# Create the SQLite tables cleanly
Base.metadata.create_all(bind=engine)


def create_user(user_data: CreateUser, db: Session):
    new_user = User(
            id=uuid4(),  # Generate native python UUID object cleanly
            name=user_data.name,
            email=user_data.email,
            age=user_data.age
        )
    return user_repository.save(db,new_user)
 

def get_users(skip: int, limit: int, db: Session):
    return user_repository.find_all(db,skip, limit)
     

def get_count(db: Session):
    total_users = user_repository.count_all(db)
    return {
        "total_users": total_users
    } 


def get_user(user_id: UUID, db: Session):
    user = user_repository.find_by_id(db,user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user


def delete_user(user_id: UUID, db: Session):
    user = user_repository.find_by_id(db,user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        
    user_repository.delete(db,user)
    return {"message": "User deleted successfully"}