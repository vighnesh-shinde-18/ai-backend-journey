from pydantic import BaseModel, Field

class CodeSubmission(BaseModel):
    language: str
    code: str = Field(..., min_length=10)
    max_tokens: int = 500