from fastapi import APIRouter, status,Depends
from app.services import user_service
from app.schemas import CreateUser, ReturnUser
from uuid import UUID
from app.database import get_db
from sqlalchemy.orm import Session
 
router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/",response_model=ReturnUser, status_code=status.HTTP_201_CREATED)
async def create(user_data:CreateUser, db:Session=Depends(get_db)):
    return user_service.create_user(user_data,db)

@router.get("/",response_model=list[ReturnUser])
async def get(skip: int = 0, limit: int = 10, db:Session=Depends(get_db)):
    return user_service.get_users(skip, limit,db)

@router.get("/count")
async def count(db:Session=Depends(get_db)):
    return user_service.get_count(db)

@router.get("/{user_id}",response_model=ReturnUser)
async def user(user_id:UUID, db:Session=Depends(get_db)):
    return user_service.get_user(user_id,db)

@router.delete("/{user_id}")
async def delete(user_id:UUID,db:Session=Depends(get_db)):
    return user_service.delete_user(user_id,db)
