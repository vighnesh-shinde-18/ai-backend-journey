from uuid import UUID, uuid4
from app.database import users_db
from fastapi import HTTPException

def create_user(user_data):
    new_id = uuid4()
    new_user = {
        "id":new_id,
        "name":user_data.name,
        "email":user_data.email,
        "age":user_data.age
        }
    users_db.append(new_user)
    return new_user

def get_users():
    return users_db

def get_count():
    count = len(users_db)
    return {
    "total_users": count
    }

def get_user(user_id):
    for user in users_db:
        if user["id"] == user_id:
            return user
    return HTTPException(status_code=404, detail="User not found")

def delete_user(user_id):
    for user in users_db:
        if user["id"] == user_id:
            return {"message":"User deleted","user":user}
    return HTTPException(status_code=404, detail="User not found")