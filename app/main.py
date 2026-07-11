from fastapi import FastAPI
from app.schemas import CodeSubmission
from app.routers.users import router as users_router
from app.config import settings 


app = FastAPI(title=settings.app_name)
 
app.include_router(users_router)

@app.get("/")
async def root():
    print(settings.app_name)
    print(settings.OPENAI_API_KEY)
    return{
        "message":"Hello AI Engineer!"
    }

# @app.get("/about")
# async def about():
#     return{
#         "name": "Vighnesh",
#         "role": "AI Engineer"
#     }

# @app.get("/users/{user_id}")
# async def get_user(user_id:int):
#     return {
#         "user_id":user_id,
#         "name": "username"
#     }

# @app.get("/search")
# async def search(name:str):
#     return {
#         "name" : name 
#     }

# @app.post("/review")
# async def review_code(submission: CodeSubmission):
#     return {
#         "message": "Code received successfully!",
#         "language": submission.language,
#         "length": len(submission.code),
#         "max_tokens": submission.max_tokens
#     }

