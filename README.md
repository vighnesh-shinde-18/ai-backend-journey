# FastAPI - Python Framework for AI

FastAPI is Python Framework for Backend which receive HTTP request and call python funtion then return response

## Features
- Modern
- Automatic validation
- Faster
- Swagger UI built in
- Full type hints

## Steps for Setup
- Create project
  ```bash
  cd ai-backend-journey
  ```

- Install FastApi & Dependencies 
  ```bash 
  pip install fastapi uvicorn pydantic python-dotenv httpx requests
  ```

- Create a virtual environment for Windows
  ```bash
  python -m venv venv
  ```

- Activate virtual environment
  ```bash 
  `venv\Scripts\activate`
  ```

- Install packages
  ```bash 
  pip install fastapi uvicorn
  ```

- Save dependencies
  ```bash 
  pip freeze > requirements.txt
  ```

- Deactivate virtual environment
  ```bash 
  deactivate
  ``` 

## Run Server
  ```bash
  uvicorn app.main:app --reload
  ```

### API Endpoint - http://127.0.0.1:8000
### Swagger UI - http://127.0.0.1:8000/docs

## Pydantic 
- It is used for Validation for data that is sent through request and response
- Syntax : 
    ```bash
    from pydantic import BaseModel, Field
    class schema(BaseModel):
    language: str
    code: str = Field(..., min_length=10)
    max_tokens: int = 500
    ``` 
- Then we use them like this :-
  ```bash
  from app.schemas import CodeSubmission
  @app.post("/",response_model=CodeSubmission)
  async def submit(code:CodeSubmission)
  ```

## Router
- Syntax:
  creating router
  ```bash
  router = APIRouter(prefix="/users", tags=["Users"])
  ```
  importing and using router
  ```bash
  from app.routers.users import router as users_router
  app.include_router(users_router)
  ```

## Project Architecture 
```bash
app/
├── main.py
│
├── database.py
│
├── schemas.py
│
├── models.py
│
├── config.py
│
├── routers/
│      users.py
│
├── services/
│      user_service.py
│
├── repositories/
│      user_repository.py
│
└── utils/
example.env

```

## Service Layer
- Instead of Writing Controllers code in Router we move it to the service layer for separation of Concern
- The Service Layer have Function which called by Router Layer

## Dependency Injection
- Dependency Injection (DI) allows FastAPI to automatically manage and instantiate service objects like `UserService` using `Depends()`, removing the need to create them manually.
- This loose coupling makes your application incredibly modular; swapping a backend provider (like moving from OpenAI to Gemini) requires changing code in only one single place.

## Environment Variable
- Instead of hardcoding sensitive values directly in code we store them in env file 
  ```bash
  pip install python-dotenv
  ```
- Then we access it in config file and export it
  ```bash
  from pydantic_settings import BaseSettings, SettingsConfigDict

  class Settings(BaseSettings):
      app_name: str = "AI Backend Journey"
      debug: bool = True
      OPENAI_API_KEY: str  
 
      model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

  settings = Settings()

  ```
