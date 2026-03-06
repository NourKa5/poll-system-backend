from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.db.database import get_db
from app.schemas.question import QuestionCreate, QuestionUpdate, QuestionResponse
from app.controllers import question_controller

router = APIRouter(prefix="/questions", tags=["Questions"])

@router.get("/", response_model=List[QuestionResponse])
def get_all(db: Session = Depends(get_db)):
    return question_controller.get_all_questions(db)

@router.get("/{question_id}", response_model=QuestionResponse)
def get_one(question_id: int, db: Session = Depends(get_db)):
    return question_controller.get_question_by_id(question_id, db)

@router.post("/", response_model=QuestionResponse, status_code=201)
def create(data: QuestionCreate, db: Session = Depends(get_db)):
    return question_controller.create_question(data, db)

@router.put("/{question_id}", response_model=QuestionResponse)
def update(question_id: int, data: QuestionUpdate, db: Session = Depends(get_db)):
    return question_controller.update_question(question_id, data, db)

@router.delete("/{question_id}")
def delete(question_id: int, db: Session = Depends(get_db)):
    return question_controller.delete_question(question_id, db)
