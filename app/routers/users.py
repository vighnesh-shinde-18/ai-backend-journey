from fastapi import APIRouter
from app.services import user_service
from app.schemas import CreateUser, ReturnUser
from uuid import UUID
 
router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/",response_model=ReturnUser)
async def create(user_data:CreateUser):
    return user_service.create_user(user_data)

@router.get("/",response_model=list[ReturnUser])
async def get():
    return user_service.get_users()

@router.get("/count")
async def count():
    return user_service.get_count()

@router.get("/{user_id}",response_model=ReturnUser)
async def user(user_id:UUID):
    return user_service.get_user(user_id)

@router.delete("/{user_id}")
async def delete(user_id:UUID):
    return user_service.delete_user(user_id)
