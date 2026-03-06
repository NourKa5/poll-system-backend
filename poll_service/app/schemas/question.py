from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class QuestionCreate(BaseModel):
    text: str
    option_a: str
    option_b: str
    option_c: str
    option_d: str

class QuestionUpdate(BaseModel):
    text: Optional[str] = None
    option_a: Optional[str] = None
    option_b: Optional[str] = None
    option_c: Optional[str] = None
    option_d: Optional[str] = None

class QuestionResponse(BaseModel):
    id: int
    text: str
    option_a: str
    option_b: str
    option_c: str
    option_d: str
    created_at: datetime

    class Config:
        from_attributes = True
