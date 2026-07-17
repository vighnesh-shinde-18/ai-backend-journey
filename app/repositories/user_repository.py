from uuid import UUID
from sqlalchemy.orm import Session
from sqlalchemy import select, func
from app.models import User

def save(db:Session, user: User):
        db.add(user)
        db.commit()
        db.refresh(user)
        return user

def find_all(db:Session,skip:int, limit:int):
    query = select(User).offset(skip).limit(limit)
    return db.execute(query).scalars().all()

def find_by_id(db:Session, user_id: UUID):
    # Using explicit select to ensure correct SQLite type coercion compiler rules
    query = select(User).where(User.id == user_id)
    return db.execute(query).scalar_one_or_none()
 
def find_by_email(db:Session, email: str):
    # Using explicit select to ensure correct SQLite type coercion compiler rules
    query = select(User).where(User.email == email)
    return db.execute(query).scalar_one_or_none()
 
def count_all(db):
    query = select(func.count(User.id))
    return db.execute(query).scalar_one()

def delete(db, user: User) -> None:
    db.delete(user)
    db.commit()

 
