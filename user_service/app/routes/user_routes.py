from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.db.database import get_db
from app.schemas.user import UserCreate, UserUpdate, UserResponse
from app.controllers import user_controller

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/", response_model=List[UserResponse])
def get_all_users(db: Session = Depends(get_db)):
    return user_controller.get_all_users(db)

@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    return user_controller.get_user_by_id(user_id, db)

@router.get("/email/{email}", response_model=UserResponse)
def get_user_by_email(email: str, db: Session = Depends(get_db)):
    return user_controller.get_user_by_email(email, db)

@router.post("/", response_model=UserResponse, status_code=201)
def create_user(data: UserCreate, db: Session = Depends(get_db)):
    return user_controller.create_user(data, db)

@router.put("/{user_id}", response_model=UserResponse)
def update_user(user_id: int, data: UserUpdate, db: Session = Depends(get_db)):
    return user_controller.update_user(user_id, data, db)

@router.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    return user_controller.delete_user(user_id, db)

@router.get("/{user_id}/registration-status")
def check_registration(user_id: int, db: Session = Depends(get_db)):
    return user_controller.check_user_registered(user_id, db)
