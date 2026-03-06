from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate

def get_all_users(db: Session):
    return db.query(User).all()

def get_user_by_id(user_id: int, db: Session):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail=f"User with id {user_id} not found")
    return user

def get_user_by_email(email: str, db: Session):
    user = db.query(User).filter(User.email == email).first()
    if not user:
        raise HTTPException(status_code=404, detail=f"User with email {email} not found")
    return user

def create_user(data: UserCreate, db: Session):
    existing = db.query(User).filter(User.email == data.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="A user with this email already exists")
    user = User(**data.model_dump())
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def update_user(user_id: int, data: UserUpdate, db: Session):
    user = get_user_by_id(user_id, db)
    update_data = data.model_dump(exclude_unset=True)
    if "email" in update_data:
        conflict = db.query(User).filter(User.email == update_data["email"], User.id != user_id).first()
        if conflict:
            raise HTTPException(status_code=400, detail="Email already in use by another user")
    for key, value in update_data.items():
        setattr(user, key, value)
    db.commit()
    db.refresh(user)
    return user

def delete_user(user_id: int, db: Session):
    user = get_user_by_id(user_id, db)
    db.delete(user)
    db.commit()
    return {"message": f"User {user_id} deleted successfully"}

def check_user_registered(user_id: int, db: Session):
    user = get_user_by_id(user_id, db)
    return {"user_id": user.id, "is_registered": user.is_registered}
