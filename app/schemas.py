from pydantic import BaseModel, Field, EmailStr
from uuid import UUID

class CodeSubmission(BaseModel):
    language: str
    code: str = Field(..., min_length=10)
    max_tokens: int = 500

class CreateUser(BaseModel):
    name:str
    email:EmailStr
    age:int

class ReturnUser(BaseModel):
    id:UUID
    name:str
    email:EmailStr
    age:int
      
    class Config:
        from_attributes = True  # Allows Pydantic to read SQLAlchemy ORM objects

 