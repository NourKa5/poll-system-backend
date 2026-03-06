from pydantic import BaseModel, field_validator
from typing import Optional
from datetime import datetime

class AnswerCreate(BaseModel):
    user_id: int
    question_id: int
    selected_option: str

    @field_validator("selected_option")
    @classmethod
    def validate_option(cls, v):
        v = v.upper()
        if v not in ("A", "B", "C", "D"):
            raise ValueError("selected_option must be one of: A, B, C, D")
        return v

class AnswerUpdate(BaseModel):
    selected_option: str

    @field_validator("selected_option")
    @classmethod
    def validate_option(cls, v):
        v = v.upper()
        if v not in ("A", "B", "C", "D"):
            raise ValueError("selected_option must be one of: A, B, C, D")
        return v

class AnswerResponse(BaseModel):
    id: int
    user_id: int
    question_id: int
    selected_option: str
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        from_attributes = True
