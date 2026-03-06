from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    age: Optional[int] = None
    is_registered: bool = False

class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    age: Optional[int] = None
    is_registered: Optional[bool] = None

class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    age: Optional[int]
    is_registered: bool
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        from_attributes = True
