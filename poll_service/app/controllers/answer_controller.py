from sqlalchemy.orm import Session
from fastapi import HTTPException, status
import httpx
import os
from app.models.answer import Answer
from app.schemas.answer import AnswerCreate, AnswerUpdate

USER_SERVICE_URL = os.getenv("USER_SERVICE_URL", "http://user_service:8000")

def _verify_user_registered(user_id: int):
    try:
        response = httpx.get(f"{USER_SERVICE_URL}/users/{user_id}/registration-status", timeout=5.0)
        if response.status_code == 404:
            raise HTTPException(status_code=404, detail=f"User {user_id} does not exist")
        data = response.json()
        if not data.get("is_registered"):
            raise HTTPException(status_code=403, detail=f"User {user_id} is not registered and cannot submit answers")
    except httpx.RequestError:
        raise HTTPException(status_code=503, detail="User Service is unavailable")

def get_all_answers(db: Session):
    return db.query(Answer).all()

def get_answer_by_id(answer_id: int, db: Session):
    answer = db.query(Answer).filter(Answer.id == answer_id).first()
    if not answer:
        raise HTTPException(status_code=404, detail=f"Answer {answer_id} not found")
    return answer

def submit_answer(data: AnswerCreate, db: Session):
    _verify_user_registered(data.user_id)
    existing = db.query(Answer).filter(Answer.user_id == data.user_id, Answer.question_id == data.question_id).first()
    if existing:
        raise HTTPException(status_code=409, detail="User already answered this question. Use PUT to update.")
    answer = Answer(**data.model_dump())
    db.add(answer)
    db.commit()
    db.refresh(answer)
    return answer

def update_answer(user_id: int, question_id: int, data: AnswerUpdate, db: Session):
    _verify_user_registered(user_id)
    answer = db.query(Answer).filter(Answer.user_id == user_id, Answer.question_id == question_id).first()
    if not answer:
        raise HTTPException(status_code=404, detail="Answer not found for this user and question")
    answer.selected_option = data.selected_option
    db.commit()
    db.refresh(answer)
    return answer

def delete_answer(answer_id: int, db: Session):
    answer = get_answer_by_id(answer_id, db)
    db.delete(answer)
    db.commit()
    return {"message": f"Answer {answer_id} deleted successfully"}
