from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.db.database import get_db
from app.schemas.answer import AnswerCreate, AnswerUpdate, AnswerResponse
from app.controllers import answer_controller

router = APIRouter(prefix="/answers", tags=["Answers"])

@router.get("/", response_model=List[AnswerResponse])
def get_all(db: Session = Depends(get_db)):
    return answer_controller.get_all_answers(db)

@router.get("/{answer_id}", response_model=AnswerResponse)
def get_one(answer_id: int, db: Session = Depends(get_db)):
    return answer_controller.get_answer_by_id(answer_id, db)

@router.post("/", response_model=AnswerResponse, status_code=201)
def submit(data: AnswerCreate, db: Session = Depends(get_db)):
    return answer_controller.submit_answer(data, db)

@router.put("/user/{user_id}/question/{question_id}", response_model=AnswerResponse)
def update(user_id: int, question_id: int, data: AnswerUpdate, db: Session = Depends(get_db)):
    return answer_controller.update_answer(user_id, question_id, data, db)

@router.delete("/{answer_id}")
def delete(answer_id: int, db: Session = Depends(get_db)):
    return answer_controller.delete_answer(answer_id, db)
