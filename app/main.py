from fastapi import FastAPI
from app.schemas import CodeSubmission

app = FastAPI()

@app.get("/")
async def root():
    return{
        "message":"Hello AI Engineer!"
    }

@app.get("/about")
async def about():
    return{
        "name": "Vighnesh",
        "role": "AI Engineer"
    }

@app.get("/users/{user_id}")
async def get_user(user_id:int):
    return {
        "user_id":user_id,
        "name": "username"
    }

@app.get("/search")
async def search(name:str):
    return {
        "name" : name 
    }

@app.post("/review")
async def review_code(submission: CodeSubmission):
    return {
        "message": "Code received successfully!",
        "language": submission.language,
        "length": len(submission.code),
        "max_tokens": submission.max_tokens
    }